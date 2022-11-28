from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication

from core.permissions import CorePermission


# Create your views here.
class GoldApiView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [CorePermission]

    def get(self, request, *args):
        return Response("hello world!", status=status.HTTP_200_OK)
