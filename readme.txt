На Linux:
В папке с проектом создать виртуальную среду:
    python3 -m venv venv
    
Активировать виртуальную среду:
    source venv/bin/activate

Установить в виртуальную среду все нужные зависимости
    pip install -r requirements.txt

Запуск
    ./manage.py runserver

По умолчанию запускается на 8000 порту
