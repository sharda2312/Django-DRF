from django.urls import path
from . import views

urlpatterns = [
    path("stu-info/<int:pk>", views.stu_detail)
]