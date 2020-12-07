from django.db.models.signals import post_save, pre_save
from .models import Book, Ongoing_book, Returned_book, Issued_book, File, Ongoing_file, Returned_file, Issued_file
from django.dispatch import receiver
from datetime import datetime, timedelta
from django.utils import timezone


@receiver(post_save, sender=Issued_book)
def book_collected(sender, instance, created, **kwargs):
    if created==False:
        id=instance.id
        if instance.collected:
            book = Ongoing_book(issue_date=timezone.now() , return_date=timezone.now()+timedelta(30), book_id= instance.book_id , username_id = instance.username_id)
            book.save()
            instance.delete()
    else:
        if instance.book.availability == 1:
            book = Book.objects.get(id = instance.book.id)
            book.availability = 0
            book.save()
            instance.save()
        else:
            instance.delete()


@receiver(post_save, sender=Issued_file)
def file_collected(sender, instance, created, **kwargs):
    if created==False:
        id=instance.id
        if instance.collected:
            file = Ongoing_file(issue_date=timezone.now() , return_date=timezone.now()+timedelta(30), file_id= instance.file_id , username_id = instance.username_id)
            file.save()
            file_del= Issued_file.objects.get(id=id).delete()
    else:
        if instance.file.availability == 1:
            file = File.objects.get(id=instance.file.id)
            file.availability = 0
            file.save()
            instance.save()
        else:
            instance.delete()



@receiver(post_save, sender=Ongoing_book)
def book_returned(sender, instance, created, **kwargs):
    if created==False:
        if instance.returned:
            id=instance.id
            print(instance.returned, instance.id, instance.issue_date)
            book =Returned_book(issue_date=instance.issue_date , return_date=timezone.now() , book_id= instance.book_id , username_id = instance.username_id)
            book.save()
            book_del= Ongoing_book.objects.get(id=id).delete()
    #else:
    #    if instance.book.availability == 1:
    #        book = Book.objects.get(id=instance.book.id)
    #        book.availability = 0
    #        book.save()
    #        instance.save()
    #    else:
    #        instance.delete()




@receiver(post_save, sender=Ongoing_file)
def file_returned(sender, instance, created, **kwargs):
    if created==False:
        if instance.returned:
            id=instance.id
            print(instance.returned, instance.id, instance.issue_date)
            file =Returned_file(issue_date=instance.issue_date , return_date=timezone.now()+timedelta(30) , file_id= instance.file_id , username_id = instance.username_id)
            file.save()
            file_del= Ongoing_file.objects.get(id=id).delete()
    #else:
    #    if instance.file.availability == 1:
    #        file = Files.objects.get(id=instance.file.id)
    #        file.availability = 0
    #        file.save()
    #        instance.save()
    #    else:
    #        instance.delete()


@receiver(pre_save, sender=Ongoing_book)
def returndate(sender, instance, **kwargs):
    instance.issue_date = timezone.now()
    instance.return_date = timezone.now()+timedelta(30)


@receiver(pre_save, sender=Ongoing_file)
def returndate(sender, instance, **kwargs):
    instance.issue_date = timezone.now()
    instance.return_date = timezone.now()+timedelta(30)