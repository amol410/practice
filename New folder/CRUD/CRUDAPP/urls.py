from . import views
from django.urls import path

urlpatterns = [
    path('addshow', views.add_show, name='add_show'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('updatedata/<int:pk>/', views.updatedata, name="updatedata" )
]