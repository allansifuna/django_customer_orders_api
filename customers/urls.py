from django.urls import path
from . import views


urlpatterns = [
    path('', views.CustomerListAPIView.as_view(), name="customers"),
    path('<int:id>', views.CustomerDetailAPIView.as_view(), name="customer"),
]
