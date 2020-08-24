from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    content = models.TextField('CONTENT')
    name = models.CharField(verbose_name='NAME', max_length=10)

    class Meta:
        verbose_name = 'board'
        verbose_name_plural = 'board'
        db_table = 'board'

    def __str__(self):
        return self.title

