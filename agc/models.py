import uuid
from django.db import models
from agc.utils import get_random_filename

from agc.mixins import SaveModelSlugMixin, SaveModelImageMixin


class GlassElement(SaveModelSlugMixin, models.Model):

    class Meta:
        verbose_name = 'Изображения на странице'
        verbose_name_plural = 'Изображения на странице'

    title = models.CharField(max_length=250, verbose_name="Наименование")
    slug = models.SlugField(max_length=350, blank=True,
                            verbose_name="Наименование для создания ссылки",
                            help_text="Необязательно для заполнения руками")
    description = models.TextField(verbose_name="Описание материала")

    def __str__(self):
        return f'{self.title}'


class GlassElementImage(SaveModelImageMixin, models.Model):

    class Meta:
        verbose_name = "Рендер изображения со стеклом"
        verbose_name_plural = "Рендеры изображений со стеклом"
        ordering = ['priority']

    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=250, verbose_name="Наименование цвета стекла")
    color_slug = models.SlugField(max_length=350, blank=True)
    image = models.ImageField(null=True, verbose_name="Файл с картинкой большого размера")
    sm_image = models.ImageField(null=True, verbose_name="Файл с картинкой малого размера")
    priority = models.IntegerField(default=1, verbose_name="Приоритет вывода картинки")
    element = models.ForeignKey(GlassElement, related_name='images',
                                on_delete=models.CASCADE, verbose_name="Стекло к которому привязана картинка",
                                help_text='В этом поле можно использовать автозаполнение')

    def __str__(self):
        return f'<{self.image.name}, размер большого изображения={self.image.size},' \
               f' размер малого изображения={self.sm_image.size}, стекло={self.element.title}>'


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


class BaseFormModel(models.Model):

    first_name = models.CharField(max_length=50, verbose_name="Имя")
    email = models.CharField(max_length=50, verbose_name="Email")
    phone_number = models.CharField(max_length=25, verbose_name="Телефон")
    creation_date = models.DateTimeField(auto_now_add=True, blank=True,
                                         verbose_name="Дата создания уведомления")

    def __str__(self):
        return f'{self.email}'


class FeedbackHistory(BaseFormModel):

    class Meta:
        verbose_name = 'История уведомлений'
        verbose_name_plural = 'Истории уведомлений'


class OrderHistory(BaseFormModel):

    class Meta:
        verbose_name = 'История заказов'
        verbose_name_plural = 'Истории заказов'

    zone_name = models.TextField(verbose_name="Наименование зоны")
    items = models.TextField(verbose_name="Элементы, которые необходимо изготовить")
    glass_color = models.TextField(verbose_name="Цвет стекла")
    glass_name = models.TextField(verbose_name="Наименование стекла")
