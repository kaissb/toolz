from django.urls import path
from .views import *

urlpatterns = [
    path("", base64, name="base64"),
    path("md5/", hash_md5, name="md5"),
    path("url/", url_encoding, name="url"),
    path("json/", json_formatter, name="json"),
    path("timestamp/", timestamp_converter, name="timestamp"),
]
