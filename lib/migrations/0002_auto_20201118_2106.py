# Generated by Django 3.0.5 on 2020-11-18 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('availability', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Ongoing_book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lib.Book')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Returned_book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lib.Book')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]