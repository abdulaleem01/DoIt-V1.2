from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.getData),
    path('add/',views.postData),
    path('single/<int:pk>',views.getDatasingle)
]
