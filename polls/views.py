from django.shortcuts import render_to_response
from polls.models import Poll
from django.http import Http404

from django.http import HttpResponse

def index(request):

    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list }
    return render_to_response('polls/index.html', context)
    #output = ', '.join([p.question for p in latest_poll_list])
    #return HttpResponse(output)

def detail(request, poll_id):
    
    try:
        p=Poll.objects.get(id=poll_id)
    except Poll.DoesNotExist:
        
        raise Http404
    return render_to_response('polls/detail.html',{'poll': p})

    #return HttpResponse("You're looking at poll %s." % (poll_id,))

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % (poll_id,))

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % (poll_id,))

