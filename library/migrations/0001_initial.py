# Generated by Django 5.0.3 on 2024-03-11 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookborrowed', models.CharField(max_length=150, unique=True)),
                ('returned', models.BooleanField(default=False)),
            ],
        ),
    ]