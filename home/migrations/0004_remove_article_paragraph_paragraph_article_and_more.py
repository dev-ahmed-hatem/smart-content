# Generated by Django 4.1.1 on 2022-09-15 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_paragraph_article_article_paragraph'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='paragraph',
        ),
        migrations.AddField(
            model_name='paragraph',
            name='Article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.article'),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='first_image',
            field=models.ImageField(blank=True, upload_to='media/uploads/photos/'),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='second_image',
            field=models.ImageField(blank=True, upload_to='media/uploads/photos/'),
        ),
    ]
