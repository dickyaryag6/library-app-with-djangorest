from books.models import Book
from .serializers import bookSerializer
from rest_framework import status, generics
from django.core.paginator import Paginator
# from rest_framework.decorators import api_view


class BookList(generics.ListCreateAPIView):
    serializer_class = bookSerializer
    queryset = Book.objects.all()


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    resource_name       = 'Book'
    lookup_field        = 'id'
    serializer_class    = bookSerializer

    def get_queryset(self):
        return Book.objects.all()

    paginator = Paginator(get_queryset, 25)
