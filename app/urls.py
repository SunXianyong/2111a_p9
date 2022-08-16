from django.urls import path
from app.views.hello import hello

urlpatterns = [
    path('look/', hello),
]
