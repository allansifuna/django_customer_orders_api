from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .serializers import CustomersSerializer
from .models import Customer


class CustomerListAPIView(ListCreateAPIView):
    serializer_class = CustomersSerializer
    queryset = Customer.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class CustomerDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomersSerializer
    queryset = Customer.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.all()
