# Generated by Django 2.2 on 2020-05-13 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackhistory',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
    ]
