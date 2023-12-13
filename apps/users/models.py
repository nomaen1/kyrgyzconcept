from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized.forms import ResizedImageField

class User(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_image/', null=True, blank=True)
    fullname = models.CharField(max_length=255, verbose_name="ФИО", null=True, blank=True)
    surname = models.CharField(max_length=100, verbose_name="Отчество")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона", null=True, blank=True)
    address = models.CharField(max_length=100, verbose_name="Адрес", null=True, blank=True)


    def __str__(self):
        return f"{self.username} - {self.email}"
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class Settings(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название сайта")
    descriptions = models.TextField(verbose_name="Описание сайта")
    logo = models.URLField(verbose_name="Логотип")
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