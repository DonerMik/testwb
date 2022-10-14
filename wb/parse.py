import aiohttp
import asyncio

import openpyxl

from wb.models import File, DataWB

URL = 'https://basket-05.wb.ru/vol{}/part{}/{}/info/ru/card.json'


def parse_item(file):
    '''
    Save file in db.
    Create list with articles
    '''
    dok = File.objects.create(file=file)
    path_dok = dok.file.path
    book = openpyxl.open(path_dok, read_only=True)
    sheet = book.active
    list_articles = [str(row[0].value) for row in sheet.iter_rows()]
    return list_articles


def get_tasks(session: object, list_articles: list) -> list:
    tasks = []
    for i in list_articles:
        get_url = URL.format(i[:3], i[:5], i)
        tasks.append(session.get(get_url, ssl=True))
    return tasks


async def gather_data(list_articles: list, result: list) -> None:
    '''Parsing and create DataWB objects'''
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session, list_articles)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            item = await response.json()
            data = {}
            data['article'] = int(item['nm_id'])
            data['brand'] = item['selling']['brand_name']
            name_item = item['imt_name']
            data['title'] = ' / '.join([data['brand'], name_item])
            data['pk'] = data['article']
            data = DataWB.parse_obj(data)
            result.append(data.dict())


def get_data(list_articles: list, answer: list) -> list:
    asyncio.run(gather_data(list_articles, answer))
    return answer
