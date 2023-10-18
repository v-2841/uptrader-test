# Updater Test
Тестовое задание
Переменные окружения не убирал в .env, как и не переставил DEBUG=False, так как задание тестовое)

### Как запустить проект:

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
