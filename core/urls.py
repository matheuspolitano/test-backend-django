from django.urls import  path
from .views import ApiMsg


urlpatterns = [
    path("",ApiMsg.as_view(),name="api")
]

