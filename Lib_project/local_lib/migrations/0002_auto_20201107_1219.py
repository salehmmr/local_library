# Generated by Django 3.1.2 on 2020-11-07 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('local_lib', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back']},
        ),
    ]
