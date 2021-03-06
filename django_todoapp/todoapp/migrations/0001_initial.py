# Generated by Django 3.2 on 2021-05-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(max_length=128)),
                ('is_completed', models.BooleanField(default=False)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
