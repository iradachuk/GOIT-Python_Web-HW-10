# Generated by Django 4.2.3 on 2023-07-06 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_rename_description_author_bio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='born_date',
            new_name='date_born',
        ),
    ]
