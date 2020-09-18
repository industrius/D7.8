from django.urls import path
from . import views

urlpatterns = [
    path("", views.BooksView.as_view(), name="books"),
    path("book/<int:id>/", views.BookDetails.as_view(), name="book"),
    path("author/<int:id>/", views.AuthorDetails.as_view()),
    path("increment", views.book_increment, name="inc"),
    path("decrement", views.book_decrement, name="dec"),
    path("authors", views.AuthorsView.as_view(), name="authors"),
    path("publishers", views.PublishersView.as_view(), name="publishers"),
    path("publisher/<int:id>", views.PublisherDetail.as_view()),
    path("book/new", views.CreateBook, name="create_book"),
    path("author/new", views.CreateAuthor, name="create_author"),
    path("publisher/new", views.CreatePublisher, name="create_publisher"),
    path("author/delete", views.DeleteAuthor, name="delete_author"),
    path("publisher/delete", views.DeletePublisher, name="delete_publisher"),
    path("book/delete", views.DeleteBook, name="delete_book"),
    path("register", views.RegisterUser, name="register"),
    path("login", views.LoginUser.as_view(), name="login"),
    path("logout", views.LogoutUser.as_view(), name="logout"),
    path("reader/<int:id>", views.ReaderById.as_view(), name="reader_by_id"),
    path("readers", views.ReadersView.as_view(), name="readers"),
    path("move", views.MoveBook.as_view(), name="move")
]