from django.urls import Path
from .import views
app_name='diary'
urlpatterns=[
    path('',views.index,name='index'),
]