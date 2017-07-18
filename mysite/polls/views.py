from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question, Choice
# Create your views here.



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    resp= render(request, 'index.html', context) ## will look for the file in the template directory
    return resp

def index_old_response(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    template = loader.get_template('index.html')  ##will look for the file in the template directory
    context = {
        'latest_question_list': latest_question_list,
    }
    resp = HttpResponse(template.render(context, request))
    return resp
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  ##will return 404 error if not found
    resp = render(request, 'detail.html', {'question': question})
    return resp

def detail_old(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    template = loader.get_template('detail.html')  ##will look for the file in the template directory
    context = {
        'question': question,
    }
    resp  = HttpResponse(template.render(context, request))
    return resp #or render(request, 'detail.html', {'question': question})
    

def results(request, question_id):
    response = "You're looking at the results of question %s."% question_id
    return HttpResponse(response )

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print "post",request.POST
    print "meta",request.META
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        resp = HttpResponseRedirect(reverse('detail', args=(question.id,)))
        resp.content = "%s=%s"%(selected_choice, selected_choice.votes)
        return resp
