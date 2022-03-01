from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Topics(models.Model):
    title = models.CharField(verbose_name="عنوان", max_length=200)
    slug = models.SlugField(verbose_name="ادرس", max_length=200, unique=True)
    position = models.IntegerField(verbose_name="به ترتیب از ")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "تاپیک"
        verbose_name_plural = "تاپیک ها"

class Article(models.Model):
    ArticleStatus =  (
        ("P", "Published"),
        ("D", "Draft")
    )
    title = models.CharField(verbose_name="عنوان", max_length=200)
    slug = models.SlugField(verbose_name="ادرس مقاله", max_length=200, unique=True)
    topics = models.ManyToManyField(Topics, verbose_name="تاپیک", related_name="articles")
    body = RichTextUploadingField(verbose_name="محتوا", null=True, blank=True)
    thumbnail = models.ImageField(verbose_name="تصویر بند انگشتی", upload_to="images")
    published = models.DateTimeField(verbose_name="زمان انتشار", default=timezone.now)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(verbose_name="وضعیت نمایش", max_length=1, choices=ArticleStatus)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

class HomeContent(models.Model):
    title = models.CharField(verbose_name="عنوان", max_length=200, null=True, blank=True)
    body = models.TextField(verbose_name="محتوا", max_length=250, null=True, blank=True)
    thumbnail = models.ImageField(verbose_name="تصویر بند انگشتی", upload_to="images")
    published = models.DateTimeField(verbose_name="زمان انتشار", default=timezone.now)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "محتوای صفحه ی اصلی"
        verbose_name_plural = "محتوای صفحه اصلی"
