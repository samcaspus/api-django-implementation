from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('jobs/', views.jobsView),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]