from django.urls import path
from .views import Singup

urlpatterns = [
    path("sing",Singup.as_view(),name="sing")
]
