# Generated by Django 3.1 on 2020-08-24 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50, verbose_name='지역')),
            ],
            options={
                'verbose_name': '지역',
                'verbose_name_plural': '지역',
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_name', models.TextField(verbose_name='시장이름')),
                ('addr', models.TextField(null=True)),
                ('tel', models.TextField(null=True)),
                ('url', models.TextField(null=True)),
                ('ma', models.IntegerField(null=True)),
                ('store_num', models.IntegerField(null=True)),
                ('h_type', models.TextField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('famous', models.TextField(null=True)),
                ('bus', models.TextField(null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.location')),
            ],
            options={
                'verbose_name': '시장목록',
                'verbose_name_plural': '시장목록',
                'db_table': 'market_list',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=100, verbose_name='STORE NAME')),
                ('store_introduction', models.TextField(null=True, verbose_name='STORE INTRODUCTION')),
                ('open_hour', models.TimeField(blank=True, default='00:00:00', verbose_name='OPEN HOUR')),
                ('close_hour', models.TimeField(blank=True, default='23:59:59', verbose_name='CLOSE HOUR')),
                ('hour_information', models.TextField(blank=True, null=True, verbose_name='HOUR INFORMATION')),
                ('market_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.market')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='OWNER')),
            ],
            options={
                'verbose_name': '점포목록',
                'verbose_name_plural': '점포목록',
                'db_table': 'store_list',
            },
        ),
        migrations.CreateModel(
            name='StoreAttachFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='파일')),
                ('filename', models.CharField(max_length=64, null=True, verbose_name='첨부파일명')),
                ('content_type', models.CharField(max_length=128, null=True, verbose_name='MIME TYPE')),
                ('size', models.IntegerField(verbose_name='파일 크기')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='market.store', verbose_name='Store')),
            ],
            options={
                'db_table': 'store_attach_file',
            },
        ),
        migrations.CreateModel(
            name='MarketAttachFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='파일')),
                ('filename', models.CharField(max_length=64, null=True, verbose_name='첨부파일명')),
                ('content_type', models.CharField(max_length=128, null=True, verbose_name='MIME TYPE')),
                ('size', models.IntegerField(verbose_name='파일크기')),
                ('market', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='market.market', verbose_name='market')),
            ],
            options={
                'db_table': 'market_attach_file',
            },
        ),
    ]
