from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='TITLE',max_length=50)
    content = models.TextField('CONTENT')
    name = models.CharField(verbose_name='name',max_length=10)

    class meta:
        verbose_name = 'post'
        verbose_name_plural = 'post'
        db_table = 'post'

    def __str__(self):
        return self.title