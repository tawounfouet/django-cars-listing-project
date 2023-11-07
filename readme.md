## Django Carzone Project


### 1. Create a virtual environment and install dependencies
```
python3 -m venv venv
# or virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Create a .env file in the root directory and add the following
```
SECRET_KEY=your_secret_key
DEBUG=True
```

### 3. Run the server
```
python manage.py runserver
```

### 4. Create a superuser
```
python manage.py createsuperuser
```

### 5. Visit the admin panel
```
http://localhost:8000/admin
```

## Static files Configuration

Go to settings.py and add the following
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



# for carzone project
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    BASE_DIR / 'carzone/static',
]

```


### 6. Run the following command to collect static files

```python
python manage.py collectstatic
```


