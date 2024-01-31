from django.urls import path
from .import views

app_name='diary'

urlpatterns=[
        path('', views.index, name='index'),
        path('add/', views.index, name='add'),
         path('update/<int:pk>', views.index, name='update'),
]