from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import plotly.graph_objects as go
from django.http import JsonResponse


@api_view(['GET'])
def home(req):
    return Response(data={"data":"data"}, status=status.HTTP_200_OK)

# Create your views here.
