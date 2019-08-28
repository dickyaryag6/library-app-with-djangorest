from django.urls import path
from .views import BookList, BookDetail

urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('<int:id>', BookDetail.as_view(), name='book_detail'),
]
