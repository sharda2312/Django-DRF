from django.urls import path
from . import views 

urlpatterns = [
    path('get-data/', views.student),
]