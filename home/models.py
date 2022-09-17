from django.db import models


class Article(models.Model):
    article_title = models.CharField(verbose_name="Article Title", max_length=80)
    article_description = models.TextField(verbose_name="Description", max_length=200)
    date_pub = models.DateField(verbose_name="Date Published", auto_now=True)
    cover_image = models.ImageField(verbose_name="Cover Image", upload_to="uploads/photos/")
    views = models.IntegerField(editable=False, default=0)

    def visited(self):
        self.views += 1
        self.save()

    def __str__(self):
        return self.article_title


class Paragraph(models.Model):
    heading = models.CharField(max_length=200)
    text = models.TextField()
    first_image = models.ImageField(upload_to="uploads/photos/", blank=True)
    second_image = models.ImageField(upload_to="uploads/photos/", blank=True)
    order = models.IntegerField(verbose_name="Order")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.heading
