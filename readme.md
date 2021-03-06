### AGC Landing Page
---

Для разработки проекта необходимо запустить PostgreSQL в Docker контейнере.
Для запуска разработки необходимо иметь Docker на машине разработчика.

Что такое докер - тут: https://www.docker.com/

1. Собрать слепок образа контейнера. <br>
Находясь в папке проекта ввести в консоли команду <br>
``$>  docker build -t agc_postgres_image -f Dockerfile_postgres .``

2. Создать экземляр контейнера. <br>
Находясь в папке проекта ввести в консоли команду <br>
``$>  docker run -p 5435:5432 -d --name agc_postgres agc_postgres_image``

3. Находясь в папке с проектом ввести команду для выполнения изначальных миграций.
``$> python manage.py migrate``

4. Создать суперпользователя
``$> python manage.py createsuperuser``
Можно пропускать шаг с введением E-mail просто нажав Enter.
Логин\Пароль также может быть просто admin/admin

5. Запустить проект.
``$> python manage.py runserver``

Ваш проект будет доступен по адресу: http:\\127.0.0.1:8000
Админка проекта будет доступна по адресу: http:\\127.0.0.1:8000\admin

---
PS
После выключения\включения компьютера как правило запущенный докер-контейнер выклучается,
но данные, которые были внутри БД созраняются, потому перед началом работы имеет смысл
проверить наличие работающего контейнера командой
``$> docker ps``
Должно быть выведено примерно следующее:
```
CONTAINER ID        IMAGE                COMMAND                  CREATED             STATUS                          PORTS                    NAMES
91008162bc59        hdl_postgres_image   "docker-entrypoint.s…"   3 hours ago         Up 3 hours                      0.0.0.0:5435->5432/tcp   agc_postgres
```
Если информации о контейнере не выводится, т.е. выдаётся пустая строка

```
CONTAINER ID        IMAGE                COMMAND                  CREATED             STATUS                          PORTS                    NAMES
```
то следует запустить контейнер командой
``$> docker start agc_postgres``

После этого снова проверить наличие запущенного контейнера.

Далее преступать к разработке воспользоваашись командой из п.5



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
