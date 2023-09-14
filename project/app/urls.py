from django.urls import path

from app.views import view_func, DetailViewClass

urlpatterns = [
    path('', view_func, name='func'),
    path('class/', view_func, name='class'),
    path('class/detail/<slug:slug>', DetailViewClass.as_view(), name='class_detail'),
]
