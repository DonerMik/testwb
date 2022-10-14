WBtest - приложение с одним эндпоинтом http://localhost/api/info, принимающий файл с артикулами товаров с сайта https://www.wildberries.ru/
формата xlsx(Ариткулы вводятся в первой колонке) или один артикул и возвращает данные в формате json(артикул, бренд, название товара).

Python 3.10
Django 4.1.2(фреймворк для разработки вебприложения)
Django restframework 3.14.0(API фреймворк для Django)
postgresql
aiohttp - применялись асинхронные запросы к серверу
ОСНОВНЫЕ НАСТРОЙКИ ПРОЕКТА:

1)Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/account_name/testwb/

2)Перейти в проект(где находится файл manage.py).

3)Cоздать и активировать виртуальное окружение:

python3 -m venv env

source env/bin/activate

4)Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip

pip install -r requirements.txt

Для запуска сервиса необходимо запустить его веб-приложение:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

РАБОТА СЕРВИСА API:
На эндпойнт http://localhost/api/info отправьте POST-запрос с ключем article для отправки одного артикля товара или 'file' документ(формата .xlsx)для отправки нескольких артиклей записанный в один столбец.
В ответ придет необходимая информация.

Переданный файл .env сохраните в корне папки wbtest

Автор: Микутайтис Денис. Почта: denismik92@gmail.com