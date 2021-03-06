# Generated by Django 2.2 on 2020-05-13 07:01

import agc.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailReceivers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=250, verbose_name='Почта')),
                ('is_send_email_notifications', models.BooleanField(default=True, verbose_name='Отправлять сообщения по почте')),
            ],
            options={
                'verbose_name': 'Получатель уведомлений',
                'verbose_name_plural': 'Получатели уведомлений',
            },
        ),
        migrations.CreateModel(
            name='FeedbackHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=25, verbose_name='Телефон')),
                ('data_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'История уведомлений',
                'verbose_name_plural': 'Истории уведомлений',
            },
        ),
        migrations.CreateModel(
            name='ImageStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название из инструкции')),
                ('slug', models.SlugField(blank=True, help_text='Необязательно для заполнения руками', max_length=250, verbose_name='Наименование для создания ссылки')),
                ('image', models.ImageField(blank=True, upload_to=agc.utils.get_random_filename)),
            ],
            options={
                'verbose_name': 'Изображения на странице',
                'verbose_name_plural': 'Изображения на странице',
            },
        ),
    ]
