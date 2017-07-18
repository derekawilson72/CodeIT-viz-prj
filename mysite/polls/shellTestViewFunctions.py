from polls.views import *
from polls.models import *
from django.http import HttpRequest
from django.core.urlresolvers import  resolve, reverse
from django.shortcuts import render, get_object_or_404

request     = HttpRequest()    ##initialize a http request
question_id = 1  ##set the test question id

indexResp   = index(request)   ##return the index page as a response
print indexResp          ##print the html string returned 
print indexResp.content  ##just view the content of the response

detailResp  = detail(request, question_id) ##return a detail repsone

resultsResp = results(request, question_id) ##return results response

voteResp    = vote(request, question_id)    ##return a vote response



from django.test import Client
c = Client(HTTP_HOST= 'localhost')  ##run a client as though accessing the url
response = c.get('/polls/',request.GET)  ##get the html response
print response  ##

response = c.get('/polls/1/',request.GET)  ##get the html response
print response  ##

response = c.get('/polls/1/results/',request.GET)  ##get the html response
print response  ##

##test the server directly with the server up and running
from django.core.urlresolvers import reverse
import requests
indexURL = reverse(index) ##negotiate the url pointing to the index function
url = "http://127.0.0.1:8000" + indexURL ##set the full url
resp = requests.get(url) #request the index page
resp.text ##html output from the page
resp.status_code ##status code = 200 is normal



##Test the Voting Form
request     = HttpRequest()    ##initialize a http request
question_id = 1  ##set the test question id
question = get_object_or_404(Question, pk=question_id) ##get question entry
choices  = question.choice_set.all()  ##get choices associated with entry
choice   = choices[0]
request.POST['choice'] = choice.id  ##set the choice number to vote on
selected_choice = question.choice_set.get(pk=request.POST['choice'])  ##select the choice from query such as the html form will do
selected_choice.votes ##get the number of votes with this choice
selected_choice.votes +=1   #increment by one vote
selected_choice.save()      #save to database
responseSite=reverse('detail', args=(question.id,))##set the response to the detail url
response=HttpResponseRedirect(responseSite)
rm=resolve('/polls/1/vote/')  ##test the url functionality to make sure this url will call the right function
##Test the whole function at once
request     = HttpRequest()    ##initialize a http request
question_id = 1  ##set the test question id
request.POST['choice'] = 2
voteResp    = vote(request, question_id)    ##return a vote response
print voteResp
