from django.urls import path
from rest_api.views import VersionView

urlpatterns = [
    path('version/', VersionView.as_view(), name='index')
]
