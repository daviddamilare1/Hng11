from django.urls import path
from .views import temperature

urlpatterns = [
    path('hello/', temperature ),
]
