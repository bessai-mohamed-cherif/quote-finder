# Generated by Django 3.1.3 on 2021-04-06 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authors',
            old_name='author',
            new_name='name',
        ),
    ]
