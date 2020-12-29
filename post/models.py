from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    publishing_date = models.DateTimeField(verbose_name='Publishing Date')

    def __str__(self):
        return self.title