from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from wb.parse import parse_item, get_data
from wb.models import BrandData


class UploadView(APIView):
    parser_classes = (MultiPartParser, JSONParser)

    def post(self, request):
        list_articles = []
        file = request.FILES.get('file')
        article = request.data.get('article')
        if file:
            list_articles = parse_item(file)
        if article:
            list_articles.append(article)
        response = get_data(list_articles=list_articles, answer=[])
        objects = [BrandData(**i) for i in response]
        BrandData.objects.bulk_create(objects)
        return Response(response)
