@ECHO OFF
cd /d C:\Users\HAMZA\Desktop\python projects\AuiProgram
pip install django
pip install -r requirements.txt
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
STOP