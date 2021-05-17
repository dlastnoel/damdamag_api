from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List of Officials': '/officials/',
        'Official Details': '/officials/<str:pk>/',
        'Cases': '/cases/',
        'Case Count': '/cases/count/',
        'Posts': '/posts/<str:type>',
        'Request Details': '/requests/<str:pk>',
        'Request Create': '/request-create/',
        'Request Update': '/request-update/',
    }

    return Response(api_urls)


@api_view(['GET'])
def Officials(request):
    officials = Official.objects.all()
    serializer = OfficialSerializer(officials, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def OfficialsDetail(request, pk):
    officials = Official.objects.get(id=pk)
    serializer = OfficialSerializer(officials, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def Cases(request):
    cases = Case.objects.all()
    serializer = CaseSerializer(cases, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Posts(request, pk):
    if pk == 'cases':
        posts = Post.objects.filter(hashtag='cases').order_by('-id')
    else:
        posts = Post.objects.exclude(hashtag='cases')

    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def CasesCount(request):
    cases = {
        'total': Case.objects.count(),
        'active': Case.objects.filter(status='active').count(),
        'recovered': Case.objects.filter(status='recovered').count(),
        'deaths': Case.objects.filter(status='died').count(),
    }
    serializer = CasesCountSerializer(cases, many=False)

    return Response(serializer.data)


@ api_view(['GET'])
def Requests(request, pk):
    if pk == 'all':
        requests = Request.objects.all()
        serializer = RequestSerializer(requests, many=True)
    else:
        requests = Request.objects.get(code=pk)
        serializer = RequestSerializer(requests, many=False)
    return Response(serializer.data)


@ api_view(['POST'])
def RequestCreate(request):
    serializer = RequestSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@ api_view(['POST'])
def RequestUpdate(request, pk):
    requests = Request.objects.get(code=pk)
    serializer = RequestSerializer(instance=requests, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@ api_view(['DELETE'])
def RequestDelete(request, pk):
    requests = Request.objects.get(code=pk)
    requests.delete()

    return Response('Request deleted')
