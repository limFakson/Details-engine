from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.soleo_list),
    path('<int:pk>', views.soleo_details)
]
