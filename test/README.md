#Работа с Django-Framework
Команда **django-admin startproject Название** - создает проект для работы с Django

    setting.py - настройки проекта
    urls.py - привязка url'ов к проекту
    wsgi.py - файл необходимой для загрузки готового сайта на хостинг

Команда для запуска сервера **python ./manage.py runserver**

Команда **python .\manage.py startapp Название_приложения путь** создает новое приложение в проекте

    Для того, чтобы приложения работали из папки apps/ необходимо в settings.py вписать следующее
    
    from pathlib import Path
    import sys
    import os
    
    BASE_DIR = Path(__file__).resolve().parent.parent
    PROJECT_DIR = Path(__file__).resolve().parent
    sys.path.append(str(os.path.join(PROJECT_DIR, 'apps')))

Команда для выполнения миграций **python manage.py makemigrations Название приложения**

    Модели прописываются в файле models.py
    Для того, чтобы команда makemigrations сработала, необходимо добавить
    наше приложение в переменную INSTALLED_APPS файла settings.py

Команды для формирования и применения миграций **python manage.py sqlmigrate Название приложения Номер миграции** и затем **python manage.py migrate**

Команда для запуска django shell **python manage.py shell**

Команда для создания учетной записи админа **python manage.py createsuperuser**
