### AGC Landing Page

1. склонировать репозиторий
2. создать venv `python -m venv venv`
3. активировать окружение `source venv/bin/activate`
4. уснановить зависимости `pip install -r requirements.txt`

5. `export FLASK_APP=main.py`
6. `flask db init`
7. `flask db migrate -m "init migrate"`
8. `flask db upgrade`
9. чтобы запустить `flask run` 


### Переменные окружения

```
SECRET_KEY - секретный ключ (просто любой набор символов)
DATABASE_URI - строка подключения к базе данных

MAIL_SERVER - почтовый сервер (сейчас: smtp.yandex.ru)
MAIL_PORT - порт (по умолчанию 587)
MAIL_USE_TLS - использование TLS (0 или 1, по умолчанию 1)
MAIL_SENDER - адрес отправителя (сейчас: dev@eleven-group.ru )
MAIL_USERNAME - логин пользователя  (сейчас: dev@eleven-group.ru )
MAIL_PASSWORD - пароль (сейчас: 9M5mUmL8GCээ )

CLEAR_DATABASE - флаг очистки базы данных (0 или 1, по умолчанию 0)
CREATE_ADMIN - флаг создания админа (0 или 1, по умолчанию 0)
ADMIN_MAIL - почта админа
ADMIN_PASS - пароль админа
```

На сайте есть админка с возможностью загружать (изменять, удалять) фотографии
чтобы получить права администратора, сначала нужно указать переменные окружения ADMIN_MAIL и ADMIN_PASS и 
установить флаг CREATE_ADMIN = 1


запуск контейнера `./agc_run.sh`
остановка контейнера `sudo docker stop agc_con`
удаление контейнера `sudo docker rm agc_con`

Для того чтобы вставить картинку в нужное место в нужном шаге необходимо через форму 
администратора добавить нужные изображения со следующими именами

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
