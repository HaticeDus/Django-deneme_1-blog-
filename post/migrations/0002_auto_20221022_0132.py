# Generated by Django 3.2.7 on 2022-10-21 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publishing_date',
            field=models.DateTimeField(verbose_name='yayımlanma Tarihi'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Başlık'),
        ),
    ]
