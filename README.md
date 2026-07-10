## Server Side Rendering App
### Using Render for Deployment
------------------------------------
Simple Django Template for Notetaking for learning CRUD 
Steps to deploy Creating Rendering Account
Providing the Requirements along with the necessary imports
For Django to deploy i used this 

- [ ] `pip install gunicorn` # this is for server a Python app server that we will use when deploying code. 

- [ ] `pip install whitenoise` #  a library for serving static files (our CSS).

- [ ] `pip freeze > requirements.txt`

- [ ] adding middle Ware =['whitenoise.middleware.WhiteNoiseMiddleware',] in settings.py

- [ ] ALLOWED_HOSTS = ['127.0.0.1'] # need to modify this again once we deploy the app by getting the name of the url

- [ ] STATIC_URL = '/static/'
- [ ] STATIC_ROOT = BASE_DIR / 'static'

Testing locally before the server runs `gunicorn quicknotes.wsgi` in the command prompt

- [ ] `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
