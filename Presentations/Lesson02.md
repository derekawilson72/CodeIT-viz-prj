Editing The Views
=================
Edit The file polls/views.py to look like this:

```py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    name = 'Your-Name'
    respString = "Hello, %s. You're at the polls index."%(name)
    resp = HttpResponse(respString)
    return resp
```

Edit The file polls/urls.py to look like this:
```py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

```

Edit The file mysite/urls.py to look like this:
```py
from django.conf.urls import url, include
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
]
```

Edit The file mysite/settings.py to include the *INSTALLED_APPS* variable like this:
```py
INSTALLED_APPS = [
    'polls',  ##include the polls app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
Run the commands:
```bash
[user@localhost Python]$ python manage.py runserver
```
Open the browser to view this content at: http://localhost:8000/polls/
![Image of View01](https://github.com/derekawilson72/CodeIT-viz-prj/blob/master/Presentations/images/Views01.png?raw=true)


Edit The file polls/models.py to look like this:

```py
from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Question(models.Model):
    """
    Database table to include questions associated with the app.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    """
    Database table to include responses to each question.  
    One question can have many choices.  
    Questions are delegated by a foreign key.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

Run the commands:
```bash
[user@localhost Python]$ python manage.py makemigrations
Migrations for 'polls':
		  polls/migrations/0001_initial.py:
    			- Create model Choice
    			- Create model Question
    			- Add field question to choice
[user@localhost Python]$ python manage.py migrate
	operations to perform:
  			Apply all migrations: admin, auth, contenttypes, polls, sessions
			Running migrations:
```
Makemigrations will create sql that will create tables for these models with all of the table attributes and formats. Migrate will then apply the database tables to the db backend through Python.

Administering models in the admin site

Edit The file polls/admin.py to look like this:
```py
from django.contrib import admin
from .models import Question, Choice
admin.site.register(Question)
admin.site.register(Choice)
```
Open the browser to view this content at: http://localhost:8000/admin/
![Image of Admin01](https://github.com/derekawilson72/CodeIT-viz-prj/blob/master/Presentations/images/Admin01.png?raw=true)

