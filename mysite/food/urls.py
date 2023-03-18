from django.contrib import admin
from django.urls import path
from . import views
app_name='food'
urlpatterns = [
    path('', views.index,name='index'),
    path('<int:item_id>/',views.detail,name='detail'),
    path('add/',views.Create_item,name='Create-item'),
    path('edit/<int:item_id>/',views.Edit_item,name='Edit_item'),
    path('delete/<int:item_id>/',views.Delete_item,name='Delete_item'),
]