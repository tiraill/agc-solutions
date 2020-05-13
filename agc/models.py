from django.db import models
from agc.utils import get_random_filename

# Create your models here.


class ImageStorage(models.Model):

    class Meta:
        verbose_name = 'Изображения на странице'
        verbose_name_plural = 'Изображения на странице'

    name = models.CharField(max_length=250, verbose_name="Название из инструкции")
    slug = models.SlugField(max_length=250, blank=True,
                            verbose_name="Наименование для создания ссылки",
                            help_text="Необязательно для заполнения руками")
    image = models.ImageField(blank=True, upload_to=get_random_filename)

    def __str__(self):
        return f'{self.name}'


class EmailReceivers(models.Model):
    class Meta:
        verbose_name = 'Получатель уведомлений'
        verbose_name_plural = 'Получатели уведомлений'

    email = models.CharField(max_length=250, verbose_name="Почта", blank=False)
    is_send_email_notifications = models.BooleanField(default=True, verbose_name="Отправлять сообщения по почте")

    def __str__(self):
        return f'{self.email}'


class FeedbackHistory(models.Model):
    class Meta:
        verbose_name = 'История уведомлений'
        verbose_name_plural = 'Истории уведомлений'

    first_name = models.CharField(max_length=50, verbose_name="Имя")
    email = models.CharField(max_length=50, verbose_name="Email")
    phone_number = models.CharField(max_length=25, verbose_name="Телефон")
    data_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Дата создания")

    def __str__(self):
        return f'{self.email}'
