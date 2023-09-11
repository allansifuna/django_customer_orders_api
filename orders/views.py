from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .serializers import OrdersSerializer
from .models import Order
from .permissions import IsOwner


class OrderListAPIView(ListCreateAPIView):
    serializer_class = OrdersSerializer
    queryset = Order.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(customer=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(customer=self.request.user)


class OrderDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrdersSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Order.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(customer=self.request.user)
