import aiohttp
import asyncio
from wb.models import File

URL = 'https://wbx-content-v2.wbstatic.net/ru/{}.json'


def parse_item():
    dok = File.objects.all()[0]
    path_dok = dok.file.path
    with open(path_dok, "rb") as excel:
        data = excel.read()
    list_articles = data.decode('utf-8').split('\n')[:-1]
    return list_articles


def get_tasks(session, list_articles):
    tasks = []
    for i in list_articles:
        tasks.append(session.get(URL.format(i), ssl=True))
    return tasks


async def gather_data(list_articles: list, result: list):
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session, list_articles)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            item = await response.json()

            article = item['nm_id']
            brand = item['selling']['brand_name']
            name_item = item['imt_name']
            title = ' / '.join([brand, name_item])

            result.append({'Article': article,
                           'Brand': brand,
                           'Title': title,
                           })


def get_data(list_articles: list, answer: list):
    asyncio.run(gather_data(list_articles, answer))
    return answer
