from django.db import models
from django.conf import settings

# Create your models here.
# BOOKS



class Book(models.Model):
    book_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    availability = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    

class Ongoing_book(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(null = True)
    return_date = models.DateTimeField(null=True)
    returned = models.BooleanField(default=False)
    email_sent = models.BooleanField(default=False)


    def __str__(self):
        return self.book.name


class Returned_book(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue_date = models.DateTimeField()
    return_date = models.DateTimeField()

    def __str__(self):
        return self.book.name

class Issued_book(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue_date = models.DateTimeField()
    collected = models.BooleanField(default=False)

    def __str__(self):
        return self.book.name




#FILES

class File(models.Model):
    project_sr_no = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    guide = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100, choices=[('Institute level','Institute level'), ('Company','Company')])
    student1 = models.CharField(max_length=100)
    student2 = models.CharField(max_length=100)
    student3 = models.CharField(max_length=100)
    year = models.IntegerField()
    availability = models.BooleanField()

    def __str__(self):
        return self.title



class Ongoing_file(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(null = True)
    return_date = models.DateTimeField(null=True)
    returned = models.BooleanField(default=False)
    email_sent = models.BooleanField(default=False)


    def __str__(self):
        return self.file.title


class Returned_file(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue_date = models.DateTimeField()
    return_date = models.DateTimeField()

    def __str__(self):
        return self.file.title

class Issued_file(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue_date = models.DateTimeField()
    collected = models.BooleanField(default=False)

    def __str__(self):
        return self.file.title



    

