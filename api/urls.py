from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('officials/', views.Officials, name='officials'),
    path('officials/<str:pk>/', views.OfficialsDetail, name='officials-detail'),
    path('cases/', views.Cases, name='cases'),
    path('cases/count/', views.CasesCount, name='cases-count'),
    path('posts/<str:pk>/', views.Posts, name='posts'),
    path('requests/<str:pk>', views.Requests, name='requests'),
    path('request-create/', views.RequestCreate, name='request-create'),
    path('request-update/<str:pk>', views.RequestUpdate, name='request-update'),
    path('request-delete/<str:pk>',
         views.RequestDelete, name='request-delete'),
]
