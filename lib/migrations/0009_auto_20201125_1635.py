# Generated by Django 3.0.5 on 2020-11-25 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0008_auto_20201125_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ongoing_book',
            name='issue_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='ongoing_book',
            name='return_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='returned_book',
            name='return_date',
            field=models.DateTimeField(),
        ),
    ]
