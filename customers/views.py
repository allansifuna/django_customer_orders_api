from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CustomersSerializer
from .models import Customer


class CustomerListAPIView(ListCreateAPIView):
    serializer_class = CustomersSerializer
    queryset = Customer.objects.all()

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class CustomerDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomersSerializer
    queryset = Customer.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.all()
