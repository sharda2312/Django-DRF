from django.urls import path
from . import views

urlpatterns = [
    path("stu-info/", views.de_stu_info),
]