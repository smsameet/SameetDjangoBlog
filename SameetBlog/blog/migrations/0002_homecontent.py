# Generated by Django 4.0 on 2021-12-11 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان')),
                ('slug', models.SlugField(max_length=200, verbose_name='ادرس صفحه')),
                ('body', models.TextField(blank=True, max_length=200, null=True, verbose_name='محتوا')),
                ('thumbnail', models.ImageField(upload_to='images', verbose_name='تصویر بند انگشتی')),
            ],
            options={
                'verbose_name': 'محتوای صفحه ی اصلی',
                'verbose_name_plural': 'محتوای صفحه اصلی',
            },
        ),
    ]
