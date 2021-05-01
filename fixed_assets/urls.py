from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('document_types',     views.document_types,    name='document_types'),
    path('document_type/new',  views.new_document_type, name='new_document_type'),
    path('document_type/<id>', views.get_document_type, name='get_document_type'),

    path('thirds',     views.thirds,    name='thirds'),
    path('third/new',  views.new_third,     name='new_third'),
    path('third/<id>', views.get_third, name='get_third'),

]