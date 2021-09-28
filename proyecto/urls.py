from django.urls import path
from rest_framework import views
from proyecto.views import *


urlpatterns = [
    path('program/list/', ProgramListAPIView.as_view(), name = 'program_list'),
    path('program/create/', ProgramCreateAPIView.as_view(), name = 'program_create'),
    path('program/detail/<int:pk>/', ProgramDetailAPIView.as_view(), name = 'program_detail'),
    path('program/update/<int:pk>/', ProgramUpdateAPIView.as_view(), name = 'program_update'),
    path('program/change/<int:pk>/', ProgramChangeStateAPIView.as_view(), name = 'program_change'),
    path('pensum/list/', PensumListAPIView.as_view(), name = 'pensum_list'),
    path('pensum/create/', PensumCreateAPIView.as_view(), name = 'pensum_create'),
    path('pensum/detail/<int:pk>/', PensumDetailAPIView.as_view(), name = 'pensum_detail'),
    path('pensum/update/<int:pk>/', PensumUpdateAPIView.as_view(), name = 'pensum_update'),
    path('pensum/change/<int:pk>/', PensumChangeStateAPIView.as_view(), name = 'pensum_change'),
    
]

"""
urlpatterns = [
    path('program/list/', ProgramListAPIView.as_view(), name = 'program_list'),
    path('pensum/list/', PensumListAPIView.as_view(), name = 'pensum_list'),
    path('program/create/', ProgramCreateAPIView.as_view(), name = 'program_create'),
    path('pensum/create/', PensumCreateAPIView.as_view(), name = 'pensum_create'),
    path('program/detail/<int:pk>/', ProgramDetailAPIView.as_view(), name = 'program_detail'),
    path('pensum/detail/<int:pk>/', PensumDetailAPIView.as_view(), name = 'pensum_detail'),
    path('pensum/delete/<int:pk>/', PensumDeleteAPIView.as_view(), name = 'pensum_delete'),
    path('program/delete/<int:pk>/', ProgramDeleteAPIView.as_view(), name = 'program_delete'),
    path('program/update/<int:pk>/', ProgramUpdateAPIView.as_view(), name = 'program_update'),
    path('pensum/update/<int:pk>/', PensumUpdateAPIView.as_view(), name = 'pensum_update'),
    path('program/change/<int:pk>/', ProgramChangeStateAPIView.as_view(), name = 'program_change'),
    
    
]"""

""""
urlpatterns = [
    path('program/', program_api_view, name = 'program_api_view'),
    path('program/<int:pk>/', program_detail_api_view, name = 'program_detail_api_view'),
    path('pensum/', pensum_api_view, name = 'pensum_api_view'),
    path('pensum/<int:pk>/', pensum_detail_api_view, name = 'pensum_detail_api_view'),
]
"""