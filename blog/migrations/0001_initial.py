# Generated by Django 4.0 on 2021-12-13 11:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان')),
                ('body', models.TextField(blank=True, max_length=350, null=True, verbose_name='محتوا')),
                ('thumbnail', models.ImageField(upload_to='images', verbose_name='تصویر بند انگشتی')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
            ],
            options={
                'verbose_name': 'محتوای صفحه ی اصلی',
                'verbose_name_plural': 'محتوای صفحه اصلی',
            },
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='ادرس')),
                ('position', models.IntegerField(verbose_name='به ترتیب از ')),
            ],
            options={
                'verbose_name': 'تاپیک',
                'verbose_name_plural': 'تاپیک ها',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='ادرس مقاله')),
                ('body', models.TextField(blank=True, null=True, verbose_name='محتوا')),
                ('thumbnail', models.ImageField(upload_to='images', verbose_name='تصویر بند انگشتی')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('P', 'Published'), ('D', 'Draft')], max_length=1, verbose_name='وضعیت نمایش')),
                ('topics', models.ManyToManyField(to='blog.Topics', verbose_name='تاپیک')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
            },
        ),
    ]