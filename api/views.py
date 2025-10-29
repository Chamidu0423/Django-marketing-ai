from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import responses

@api_view(["GET"])
def hello_world(request):
    """
    Hello World API view.
    """
    return Response({"message": "Hello, World!"})


