# Generated by Django 4.0 on 2021-12-17 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_article_body_alter_homecontent_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecontent',
            name='body',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='محتوا'),
        ),
    ]