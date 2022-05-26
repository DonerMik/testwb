from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from wb.parse import parse_item, get_data
from wb.serializer import FileSerializer


class UploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        serializer = FileSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        list_articles = parse_item()

        answer = []
        response = get_data(list_articles=list_articles, answer=answer)
        return Response(response)
