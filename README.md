# Тестовое задание для ItFox

## Шаг 1: Клонировать репозиторий
```
git clone git@github.com:aldkfjasdfasdf/itfox_test.git
```
## Шаг 2: Добавить значения в .env файл

Пример значений находится в файле .env

## Шаг 3: Запуск приложения

### При помощи Docker
```
sudo docker compose build
```
```
sudo docker compose up
```

Создастся суперюзер с логином admin и паролем admin

### Обычный запуск

Создание виртуального окружения
```
python3 -m venv venv
```

Включение виртуального окружения для macOS, linux
```
source venv/bin/activate
```

Установка зависимостей
```
pip install -r requirements.txt
```

Миграции
```
python3 manage.py migrate
```

Создание суперюзера
```
python3 manage.py createsuperuser
```

Запуск сервера
```
python3 manage.py runserver
```

#### В обоих случаях приложение будет доступно по http://127.0.0.1:8000/
<img width="1346" alt="image" src="https://github.com/aldkfjasdfasdf/itfox_test/assets/134290831/0a6daff2-d9fd-40fb-954f-4cd0fa66a406">

## Развернутый проект
Находится по адресу http://80.249.144.129/

Развертывание сделано при помощи gunicorn, nginx, supervisor

DEBUG=True

Админка по адресу http://80.249.144.129/admin  

Логин admin 

Пароль admin

### Эндпоинты

POST Аутентификация при помощи токена  
```
http://80.249.144.129/auth/
```
<img width="1071" alt="image" src="https://github.com/aldkfjasdfasdf/itfox_test/assets/134290831/946c6000-5f48-45ee-a959-498875681082">

Если тестить через postman, то для эндпоинтов с обязательной авторизацией, нужно вставить этот токен сюда
<img width="1039" alt="image" src="https://github.com/aldkfjasdfasdf/itfox_test/assets/134290831/f624e872-35a2-4b52-973a-520f5f24c405">

POST (Проверка авторизации) Создание новости 
```
http://80.249.144.129/news/
```
<img width="1039" alt="image" src="https://github.com/aldkfjasdfasdf/itfox_test/assets/134290831/6d28b342-121a-4953-b0d6-f733d587a669">

GET Список новостей с пагинацией по 10 записей, последними 10 комментариями, количеством лайков и комментариев 
```
http://80.249.144.129/news/
```

GET Просмотр новости. Так же есть последние 10 комментриев, количество лайков, количество коментариев 
```
http://80.249.144.129/news/<id_новости>/
```

PUT (Проверка авторизации) Изминение заголовка и текста новости
```
http://80.249.144.129/news/<id_новости>/
```
<img width="1039" alt="image" src="https://github.com/aldkfjasdfasdf/itfox_test/assets/134290831/86dd6047-5b53-4f51-85e3-c613d48b82db">

DELETE (Проверка авторизации) Удаление новости
```
http://80.249.144.129/news/<id_новости>/
```

GET Просмотр комментариев новости с пагинаций по 10 записей
```
http://80.249.144.129/comments/<id_новости>/
```

POST (Проверка авторизации) Создание нового комментария
```
http://80.249.144.129/comments/<id_новости>/
```
<img width="1039" alt="image" src="https://github.com/aldkfjasdfasdf/itfox_test/assets/134290831/843e9402-6a1e-4c5e-9a10-43b23c43b272">

DELETE (Проверка авторизации) Удаление комментария 
```
http://80.249.144.129/comments/<id_новости>/<id_комментария>/
```

POST (Проверка авторизации) Создание лайка для новости. Реализовано так: если в базе есть запись, то она удаляется. Если нет, то создается.
```
http://80.249.144.129/like/<id_новости>/
```
<img width="1039" alt="image" src="https://github.com/aldkfjasdfasdf/itfox_test/assets/134290831/18260370-4b01-4f70-aeef-6101ce8f6305">
