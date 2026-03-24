from django.urls import path
from .views import *

urlpatterns = [
    path("", ResourceView.as_view()),
]