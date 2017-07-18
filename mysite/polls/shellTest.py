from polls.models import Question, Choice
from django.utils import timezone
# Make sure our __str__() addition worked.
Question.objects.all()
Question.objects.filter(id=1)


current_year = timezone.now().year
Question.objects.filter(pub_date__year=current_year)

q = Question.objects.get(pk=1)
q.pub_date
q.was_published_recently()

q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)
print c
q.choice_set.all()
