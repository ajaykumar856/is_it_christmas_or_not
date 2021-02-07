from django.urls import path
from . import views
urlpatterns=[
    path("",views.dark,name="dark")
]