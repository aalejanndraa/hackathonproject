# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResopnse("You're at the polls index")

def login(request):
    m = Member.objects.get(username=request.POST['username'])
    if m.password == request.POST['password']:
        request.session['member_id'] = m.id
        return HttpResponse("You're logged in.")
    else:
        return HttpResponse("Your username and password didn't match.")