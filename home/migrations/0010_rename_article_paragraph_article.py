# Generated by Django 4.1.1 on 2022-09-16 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_paragraph_first_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paragraph',
            old_name='Article',
            new_name='article',
        ),
    ]
