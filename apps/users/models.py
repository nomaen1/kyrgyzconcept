from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized.forms import ResizedImageField
# Create your models here.

class User(AbstractUser):
    surname = models.CharField(max_length=100, verbose_name="Отчество")
    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class Settings(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название сайта")
    descriptions = models.TextField(verbose_name="Описание сайта")
    logo = models.ImageField(upload_to="logo/", verbose_name="Логотип")
    phone = models.CharField(max_length=255, verbose_name='Телефон номер')
    email = models.EmailField(max_length=255, verbose_name='Почта')
    location = models.CharField(max_length=255, verbose_name='Адрес')
    tripadvisor = models.URLField(verbose_name='Tripadvisor URL', blank=True, null=True)
    instagram = models.URLField(verbose_name='Instagram URL', blank=True, null=True)
    twitter = models.URLField(verbose_name='Twitter URL', blank=True, null=True)
    facebook = models.URLField(verbose_name='Facebook URL', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
            verbose_name = "Основная настройка"
            verbose_name_plural = "Основные настройки"