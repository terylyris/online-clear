# Generated by Django 5.0.3 on 2024-03-19 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_library_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='bookborrowed',
            field=models.CharField(max_length=150),
        ),
    ]
