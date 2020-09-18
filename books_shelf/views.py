from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic.base import View
from .models import Book, Author, Publisher, Profile, User
from .forms import AuthorForm, BookForm, PublisherForm, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy  
from django.contrib.auth.models import Permission


class BooksView(View):
    """
    Вывод списка книг
    """
    def get(self, request):
        books = Book.objects.all().order_by("title")
        return render(request, "books.html", {"books_list": books, "books_active": "active"})

class BookDetails(View):
    """
    Информация о выбранной книге
    Друзья, которые эту книгу арендуют
    """
    def get(self, request, id):
        book = Book.objects.get(id=id)
        users = User.objects.exclude(is_staff=True)
        return render(request, "book_details.html", {"book": book, "readers": users, "books_active": "active"})

class AuthorsView(View):
    """
    Вывод списка авторов с количеством 
    книг, которые они написали
    """
    def get(self, request):
        authors = Author.objects.all().order_by("full_name")
        for author in authors:
            author.books_count = Book.objects.filter(author=author).count()
        return render(request, "authors.html", {"authors_list": authors, "authors_active": "active"})

class AuthorDetails(View):
    """
    Информация об выбранном авторе и количестве его книг в коллекции
    """
    def get(self, request, id):
        author = Author.objects.get(id=id)
        books = Book.objects.filter(author=author)
        return render(request, "author_details.html", {"author": author, "books_list": books, "authors_active": "active"})

class PublishersView(View):
    """
    Вывод списка издателей и количества их книг в библиотеке
    """
    def get(self, request):
        publishers = Publisher.objects.all().order_by("title")
        for publisher in publishers:
            publisher.books_count = Book.objects.filter(publisher=publisher).count()
        return render(request, "publishers.html", {"publishers_list": publishers, "publishers_active": "active"})

class PublisherDetail(View):
    """
    Информация о выбранном издателе и 
    список их книг в библиотеке
    """
    def get(self, request, id):
        publisher = Publisher.objects.get(id=id)
        books = Book.objects.filter(publisher=publisher)
        return render(request, "publisher_details.html", {"publisher": publisher, "books_list": books, "publishers_active": "active"})

class ReadersView(View):
    """
    Информация о всех читателях с возможностью выдачи права библиотекаря или удаления читателя
    Функционал доступен авторизованному библиотекарю в списке всех читетелей
    """
    def get(self, request):
        users = User.objects.exclude(is_staff=True).order_by("first_name")
        return render(request, "readers.html", {"profiles": users, "reader_active":"active"})

    def post(self, request):
        reader_id = request.POST["reader_id"]
        action = request.POST["action"]
        user_profile = Profile.objects.get(id=reader_id)
        django_user = user_profile.user
        permission = Permission.objects.get(name = "Can delete user")
        if action == "set_librarian":
            user_profile.can_manage_library = True
            django_user.user_permissions.add(permission)
            user_profile.save()

        elif action == "unset_librarian":
            user_profile.can_manage_library = False
            django_user.user_permissions.remove(permission)
            user_profile.save()

        elif action == "delete_reader":
            try:
                django_user.delete()
            except:
                pass
        
        users = User.objects.exclude(is_staff=True).order_by("first_name")
        return render(request, "readers.html", {"profiles": users, "reader_active":"active"})

class ReaderById(View):
    """
    Информация о читателе, какие книги он читает
    Функционал доступен авторизованному пользователю с главного меню
    или библиотекарю из списка всех читетелей
    """
    def get(self, request, id):
        reader = Profile.objects.get(id=id)
        books = Book.objects.exclude(copy_count=0)
        return render(request, "reader_details.html", {"reader": reader, "books_list": books, "reader_active":"active"})

class MoveBook(View):
    """
    Обработка передачи или возврата экземпляра книги в библиотеку
    Функционал со страницы читателя
    """
    def post(self, request):
        book_id = request.POST["book_id"]
        profile_id = request.POST["profile_id"]
        action = request.POST["action"]
        book = Book.objects.filter(id=book_id).first()
        profile = Profile.objects.filter(id=profile_id).first()
        if action == "return":
            book.copy_count += 1
            book.readers.remove(profile)
            book.save()
        elif action == "take":
            book.copy_count -= 1
            book.readers.add(profile)
            book.save()
        return redirect("/reader/" + str(profile_id))

def book_increment(request):
    """
    Обработка увеличения количества экземпляров книги в библиотеке
    Кнопки увеличения и уменьшения на странице книги
    """
    if request.method == "POST":
        id = request.POST["id"]
        book = Book.objects.filter(id = id).first()
        book.copy_count += 1
        book.save()
        return redirect("book/" + id)
    else:
        return HttpResponseRedirect("/")

def book_decrement(request):
    """
    Обработка уменьшения количества экземпляров книги в библиотеке
    Кнопки увеличения и уменьшения на странице книги
    """
    if request.method == "POST":
        id = request.POST["id"]
        book = Book.objects.filter(id = id).first()
        if book.copy_count > 0:
            book.copy_count -= 1
            book.save()
        return redirect("book/" + id)
    else:
        return HttpResponseRedirect("/")

def CreateBook(request):
    """
    Обработка добавления новой книги в библиотеку
    Функционал на странице списка книг
    """
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = BookForm()
    return render(request, "create_book.html", {"book_form": form, "books_active": "active"})

def CreateAuthor(request):
    """
    Обработка добавления нового автора 
    Функционал на странице списка авторов
    """
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/authors")
    else:
        form = AuthorForm()    
    return render(request, "create_author.html", {"author_form": form, "authors_active": "active"})

def CreatePublisher(request):
    """
    Обработка добавления нового издателя 
    Функционал на странице списка издателей
    """
    if request.method == "POST":
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/publishers")
    else:
        form = PublisherForm()
    return render(request, "create_publisher.html", {"publisher_form": form, "publishers_active": "active"})

def DeleteAuthor(request):
    """
    Обработка удаления автора 
    Функционал на странице списка авторов
    """
    if request.method == "POST":
        author = Author.objects.filter(id=request.POST["author_id"])
        author.delete()
    return redirect("/authors")

def DeletePublisher(request):
    """
    Обработка удаления издателя 
    Функционал на странице списка издателей
    """
    if request.method == "POST":
        publisher = Publisher.objects.filter(id=request.POST["publisher_id"])
        publisher.delete()
    return redirect("/publishers")

def DeleteBook(request):
    """
    Обработка удаления книги 
    Функционал на странице книги
    """
    if request.method == "POST":
        book = Book.objects.filter(id=request.POST["book_id"]).first()
        book.delete()
    return HttpResponseRedirect("/")


def RegisterUser(request):
    """
    Обработка регистрации нового читателя
    Функционал доступен через верхнее меню "Читатель", для анонимного пользователя
    """
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.can_manage_library = False
            user.save()
            my_password = form.cleaned_data.get("password1")
            user = authenticate(username=user.username, password=my_password)
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = UserRegisterForm()
        return render(request, "register.html", {"form": form, "login_active": "active"})


class LoginUser(FormView):
    """
    Обработка входа зарегистрированного читателя
    Функционал доступен через верхнее меню - "Читатель", для анонимного пользователя
    """
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/"
    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginUser, self).form_valid(form)    
        

class LogoutUser(View):
    """
    Обработка выхода зарегистрированного читателя
    Функционал доступен через верхнее меню - "Выход"
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")