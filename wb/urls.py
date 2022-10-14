from django.urls import path
from wb.views import UploadView

urlpatterns = [
    path('info/', UploadView.as_view())
    ]
