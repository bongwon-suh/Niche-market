# Generated by Django 3.1 on 2020-09-02 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_boardcomment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BoardComment',
        ),
    ]