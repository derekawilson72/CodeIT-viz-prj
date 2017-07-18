from django.conf.urls import url
from . import views


#app_name="polls"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'), # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'), # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),# ex: /polls/5/vote/
#    url(r'^(?P<question_id>[0-9]{2})/vote/$', views.vote, name='vote1'), # ex: /polls/5/vote/
#    url(r'^(?P<question_id>[0-9]{3,})/vote/$', views.vote, name='vote2'), # ex: /polls/5/vote/
]
 
if __name__=='__main__':
    from django.core.urlresolvers import  resolve, reverse
    from polls.views import index, detail, results, vote
    import re
    ##Test the url functionality with both regex patterns, url reverse  and the url resolver
    ##The regex will test a pattern to a string to help setup url definitions

    match=re.match(r'^(?P<question_id>[0-9]+)/vote/$','111/vote/')
    match.group()
    #'111/vote/'
    match.groupdict()
    #{'question_id': '111'}

    ##url reverse will determine the url needed from the urls.py
    reverse(vote,kwargs={'question_id': u'1'})
    #u'/polls/1/vote/'
    reverse(detail,kwargs={'question_id': u'1'})
    #u'/polls/1/'

    
    rm=resolve('/polls/1/vote/')  ##will test the vote url to return the function parameters
    #ResolverMatch(func=polls.views.vote, args=(), kwargs={'question_id': u'1'}, url_name=vote1, app_names=[], namespaces=[])
    rm=resolve('/polls/1/') ##will test the details url to return the function parameters
    #ResolverMatch(func=polls.views.detail, args=(), kwargs={'question_id': u'1'}, url_name=detail, app_names=[], namespaces=[])

