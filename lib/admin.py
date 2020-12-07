from django.contrib import admin
from .models import Book, Ongoing_book, Returned_book, Issued_book, File, Ongoing_file, Returned_file, Issued_file
# Register your models here.

admin.site.register(Book)
admin.site.register(Ongoing_book)
admin.site.register(Returned_book)
admin.site.register(Issued_book)
admin.site.register(File)
admin.site.register(Ongoing_file)
admin.site.register(Returned_file)
admin.site.register(Issued_file)
admin.site.site_header = 'Library Administration'
