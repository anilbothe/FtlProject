from django.urls import path
from app import views

app_name = 'main'

urlpatterns = [
    path('', views.UserActivityApi.as_view(), name="api"),
]
