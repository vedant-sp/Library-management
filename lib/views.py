from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.db.utils import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Book, Ongoing_book, Returned_book, Issued_book, File, Ongoing_file, Returned_file, Issued_file
from django.db import connection
from django.core.mail import send_mail
from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.
def loginUser(request):
    return render(request, "login.html")


@login_required(login_url=loginUser)
def files(request):
    files =File.objects.filter(availability__exact=1)
    return render(request, "files.html", {'files': files})


@login_required(login_url=loginUser)
def ongoing(request):
    books = Ongoing_book.objects.filter(username_id__exact=request.user.id)    
    files = Ongoing_file.objects.filter(username_id__exact = request.user.id)
    return render(request, "ongoing.html", {'books':books, 'files': files})


@login_required(login_url=loginUser)
def history(request):
    books = []
    book = Book.objects.all()
    files = Returned_file.objects.filter(username_id__exact = request.user.id)
    on_books = Returned_book.objects.filter(username_id__exact=request.user.id)
    for bk in on_books:
        bk1 = book.filter(id__exact=bk.book_id)
        for bkk in bk1: 
            books.append({'id':bkk.book_id, 'name':bkk.name, 'author':bkk.author, 'issue_date':bk.issue_date, 'return_date':bk.return_date})
    return render(request, "history.html", {'books':books, 'files': files})


def validate(request):
    username = request.POST["username"]
    password = request.POST["pass"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        book=Book.objects.filter(availability__exact=1)
        return render(request, "index.html", {'books': book})
    else:
        e = "Check Username or Password"
        return render(request, "login.html", context={'e': e})


@login_required(login_url=loginUser)
def index(request):
    book=Book.objects.filter(availability__exact=1)
    return render(request, "index.html", {'books': book})


def logout_request(request):
    logout(request)
    return render(request, "login.html")


def user_reg(request):
    try:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            username = email.split("@")[0]
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,
                                            password=password1)
            user.save()
            print('user created')
            return render(request, 'login.html')
    except IntegrityError as e:
        e = 'This data already exists in the database'
        return render(request, "register.html", context={'e': e})


def signup(request):
   return render(request, 'register.html')



#Search Book
@login_required(login_url=loginUser)
def search_book(request):
    search =  request.GET.get("search")
    if search=="":
        book=Book.objects.filter(availability__exact=1)
        return render(request, "index.html", {'books': book})
    else:
        books = Book.objects.filter(name__icontains=search)
        return render(request, "index.html",{'books':books})


#Search Files
@login_required(login_url=loginUser)
def search_file(request):
    search =  request.GET.get("search")
    files=File.objects.filter(availability__exact=1)
    if search=="":
        return render(request, "files.html", {'files': files})
    else:
        files = files.filter(title__icontains=search)
        return render(request, "files.html",{'files':files})



#issue Book
@login_required(login_url=loginUser)
def issue(request):
    book_id = request.GET.get("book_id")
    book = Issued_book(issue_date=timezone.now() , book_id= book_id , username_id = request.user.id ,collected=False)
    book.save()
    books = Book.objects.filter(availability__exact = 1)
    subject = 'Book Issued from Department Library'
    message = f'Your book, {book.book.name} has been issued from the Department Library. Kindly collect the copy from the Department Library during working hours.'
    mailto = book.username.email
    send_mail(
                subject,
                message,
                "vedantp.testemail.com",
                [mailto,],
                fail_silently = False
            )
    return render(request, "index.html", {"books":books})


#issue File
@login_required(login_url=loginUser)
def issue_file(request):
    file_id = request.GET.get("file_id")
    file_iss = Issued_file(issue_date=timezone.now() , file_id= file_id , username_id = request.user.id ,collected=False)
    file_iss.save()
    files = File.objects.filter(availability__exact = 1)
    return render(request, "files.html", {"files":files})



def mail(request):
    i=0
    books = Ongoing_book.objects.filter(email_sent__exact= False)
    for book in books:
        date = datetime.strptime((str(book.return_date)[:-6]),'%Y-%m-%d %H:%M:%S.%f')
        print(date)
        if (date-datetime.now())<=timedelta(2) :
            subject = "Reminder for returning book from Department Library "
            message = f"The book {book.book.name} should be returned before {book.return_date}"
            mailto=[book.username.email]
            send_mail(
                subject,
                message,
                "vedantp.testemail.com",
                mailto,
                fail_silently = False
            )
            book.email_sent=True
            book.save()
            i=i+1
    return HttpResponse(f"{i} Mails sent")


@login_required(login_url=loginUser)
def renew(request):
    book_id = request.GET.get("book_id")
    bk = Ongoing_book.objects.get(book_id=book_id)
    bk.returned = True
    bk.save()
    book = Ongoing_book(book_id = book_id, username_id = request.user.id, issue_date= timezone.now(), return_date= timezone.now()+timedelta(30))
    book.save()
    books = Book.objects.filter(availability__exact = 1)
    return render(request, "index.html", {"books":books})