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
![Image of Admin01](https://github.com/derekawilson72/CodeIT-viz-prj/blob/master/Presentations/images/Admin01.png)

Create, Update, Delete (CRUD) any table entries

![Image of Admin02](https://github.com/derekawilson72/CodeIT-viz-prj/blob/master/Presentations/images/Admin02.png)
![Image of Admin03](https://github.com/derekawilson72/CodeIT-viz-prj/blob/master/Presentations/images/Admin03.png)

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
    def __str__(self):
return self.question_text 

class Choice(models.Model):
    """
    Database table to include responses to each question.  One question can have many choices.  Questions are delegated by a foreign key.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
return self.choice_text 
```
Tables now appear with question text and choice text.
![Image of Admin04](https://github.com/derekawilson72/CodeIT-viz-prj/blob/master/Presentations/images/Admin04.png)
![Image of Admin05](https://github.com/derekawilson72/CodeIT-viz-prj/blob/master/Presentations/images/Admin05.png)

Run the command
```bash
[user@localhost Python]$ python manage.py shell
```
In the ipython terminal, issue the commands to test the models in the django backend.
```py
from django.utils import timezone
from polls.models import Question, Choice # Import the model classes we just wrote.
Question.objects.all() # extract the objects created
<QuerySet [<Question: This is my new question>, <Question: This is another question>]>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
q = Question(question_text="What's new?", pub_date=timezone.now())
# Save the object into the database. You have to call save() explicitly.
q.save()
q.id
q.question_text, q.pub_date
"What's new?", datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)
# Change values by changing the attributes, then calling save().
q.question_text = "What's up?"
q.save()
```

Edit the Question class in file polls/models.py to look like this:
```py
class Question(models.Model):
    """
    Database table to include questions associated with the app.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        """
        The text that appears in the object represented
        """
        return self.question_text
    def was_published_recently(self):
        """Determine if the question was published in the last day."""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
```

Test the newly created functionality in the python shell.

```py
from polls.models import Question, Choice
# Make sure our __str__() addition worked.
Question.objects.all()
<QuerySet [<Question: This is my new question>, <Question: This is another question>, <Question: What's new?>]>
q = Question.objects.get(pk=1)  ##get object by primary key
q.pub_date
datetime.datetime(2017, 6, 1, 14, 46, 32, tzinfo=<UTC>)
q.was_published_recently()
False
q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)
c
<Choice: Just hacking again>
q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
```

Run the command
```bash
[user@localhost Python]$ python manage.py dbshell
```
This will run the django project database in its native shell.  In this case, sqlite
```sql
.headers on  /* will change output to include header row */
.mode columns  /*change output to column mode */ 
.tables  /* show all tables */
/* 
auth_group                  django_admin_log          
auth_group_permissions      django_content_type       
auth_permission             django_migrations         
auth_user                   django_session            
auth_user_groups            polls_choice              
auth_user_user_permissions  polls_question  
*/
select * from polls_question;  /* execute table lookup to list all entries*/
/*
id          question_text            		pub_date           
----------  -----------------------  		-------------------
1           This is my new question  	2017-06-01 14:46:32
2           This is another questio  	2017-06-30 12:00:00
3           What's new?                		2017-06-15 15:17:03
*/
.quit  /*quit the shell*/
```
