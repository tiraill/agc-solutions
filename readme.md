### AGC Landing Page

Что такое докер - тут: https://www.docker.com/

1. Собрать слепок образа контейнера. <br>
Находясь в папке проекта ввести в консоли команду <br>
``$>  docker build -t hdl_postgres_image -f Dockerfile_postgres .``

2. Создать экземляр контейнера. <br>
Находясь в папке проекта ввести в консоли команду <br>
``$>  docker run -p 5435:5432 -d --name hdl_postgres hdl_postgres_image``

3. Находясь в папке с проектом ввести команду для выполнения изначальных миграций.
``$> python manage.py migrate``

4. Создать суперпользователя
``$> python manage.py createsuperuser``
Можно пропускать шаг с введением E-mail просто нажав Enter.
Логин\Пароль также может быть просто admin/admin

5. Запустить проект.
``$> python manage.py runserver``

### Переменные окружения

```
SECRET_KEY - секретный ключ (просто любой набор символов)

EMAIL_SENDER
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
EMAIL_HOST
EMAIL_PORT
EMAIL_USE_TLS
EMAIL_USE_SSL
```

На сайте есть админка с возможностью загружать (изменять, удалять) фотографии


```
step_1_gostinnaya
step_1_kuhnya
step_1_sanyzel
step_1_spalnya
step_1_detskaya
step_1_prihozhaya

step_2_skandinavskiy
step_2_klassika
step_2_loft
step_2_provans
step_2_modern
step_2_minimalizm

step_4_lacobel_1
step_4_lacobel_2
step_4_lacobel_3
step_4_lacobel_4
step_4_lacobel_5
step_4_lacobel_6
step_4_lacobel_7
step_4_lacobel_8
step_4_lacobel_9
step_4_lacobel_10
step_4_lacobel_11

step_4_matelac_1
step_4_matelac_2
step_4_matelac_3
step_4_matelac_4
step_4_matelac_5
step_4_matelac_6
step_4_matelac_7
step_4_matelac_8
step_4_matelac_9
step_4_matelac_10
step_4_matelac_11

step_4_mnge_1
step_4_mnge_2
step_4_mnge_3
step_4_mnge_4
step_4_mnge_5
step_4_mnge_6
step_4_mnge_7
step_4_mnge_8
step_4_mnge_9
step_4_mnge_10
step_4_mnge_11

step_4_planibel_1
step_4_planibel_2
step_4_planibel_3
step_4_planibel_4
step_4_planibel_5
step_4_planibel_6
step_4_planibel_7
step_4_planibel_8
step_4_planibel_9
step_4_planibel_10
step_4_planibel_11

step_4_laconat_1
step_4_laconat_2
step_4_laconat_3
step_4_laconat_4
step_4_laconat_5
step_4_laconat_6
step_4_laconat_7
step_4_laconat_8
step_4_laconat_9
step_4_laconat_10
step_4_laconat_11

step_4_mirox_1
step_4_mirox_2
step_4_mirox_3
step_4_mirox_4
step_4_mirox_5
step_4_mirox_6
step_4_mirox_7
step_4_mirox_8
step_4_mirox_9
step_4_mirox_10
step_4_mirox_11
```
