# Generated by Django 4.0 on 2021-12-13 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_topics_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topics',
            name='published',
        ),
    ]