from django.urls import path


from . import views



urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('<int:pk>/', views.BookDetails.as_view(), name='book_detail'),
    path('add/', views.CreateBook.as_view(), name='add_book'),
    path('<int:pk>/edit/', views.EditBook.as_view(), name='edit_book'),
    path('<int:pk>/delete/', views.DeleteBook.as_view(), name='delete_book'),
]
