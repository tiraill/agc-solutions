# Generated by Django 2.2 on 2020-05-16 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agc', '0002_auto_20200513_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseFormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=25, verbose_name='Телефон')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания уведомления')),
            ],
        ),
        migrations.RemoveField(
            model_name='feedbackhistory',
            name='data_time',
        ),
        migrations.RemoveField(
            model_name='feedbackhistory',
            name='email',
        ),
        migrations.RemoveField(
            model_name='feedbackhistory',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='feedbackhistory',
            name='id',
        ),
        migrations.RemoveField(
            model_name='feedbackhistory',
            name='phone_number',
        ),
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('baseformmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='agc.BaseFormModel')),
                ('zone_name', models.CharField(max_length=500, verbose_name='Наименование зоны')),
                ('items', models.CharField(max_length=500, verbose_name='Элементы, которые необходимо изготовить')),
                ('glass_color', models.CharField(max_length=25, verbose_name='Цвет стекла')),
                ('glass_name', models.CharField(max_length=25, verbose_name='Наименование стекла')),
            ],
            options={
                'verbose_name': 'История заказов',
                'verbose_name_plural': 'Истории заказов',
            },
            bases=('agc.baseformmodel',),
        ),
        migrations.AddField(
            model_name='feedbackhistory',
            name='baseformmodel_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='agc.BaseFormModel'),
            preserve_default=False,
        ),
    ]
