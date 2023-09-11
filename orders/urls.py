from django.urls import path
from . import views


urlpatterns = [
    path('', views.OrderListAPIView.as_view(), name="orders"),
    path('<int:id>', views.OrderDetailAPIView.as_view(), name="order"),
]
