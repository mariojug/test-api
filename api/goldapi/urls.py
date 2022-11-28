from django.urls import path
from goldapi.views import GoldApiView

urlpatterns = [
    path("view/", GoldApiView.as_view(), name="gold-api-path")
]
