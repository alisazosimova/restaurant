# Thi is Pet Project for DataRobot Kyiv Python Club

* clone project:
`git clone https://github.com/VadymKhodak/restaurant.git`
 * create file `local_settings.py` and add next lines in that file:
 ```python
 # SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'YOUR SECRET KEY'
```
* create database:

`python3 manage.py makemigrations`

`python3 manage.py migrate`

* create superuser for the project to get access to admin

`python3 manage.py createsuperuser`
* run Django project locally:

`python3 manage.py runserver`