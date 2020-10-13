from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Questions
from django.shortcuts import get_object_or_404
import participants.db as db
from django.core.paginator import EmptyPage , PageNotAnInteger, Paginator

from django.contrib import messages, auth
from django.contrib.auth.models import User
from participants.models import Participants


global l


l = dict()

def index(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.error(request,'Email is already registered')
            return redirect('index')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'user name is already exists')
                return redirect('index')
            else:
                # date_joined, email, first_name, groups, id, is_active, is_staff, is_superuser, last_login, last_name, logentry, password, user_permissions, username
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                # db.call([first_name,last_name,email,0],1)
                # auth.login(request,user)s

                messages.success(request,'Your Successfully registeres here')
                return redirect('login')
    else:
        return render(request,'login/login.htm')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        # print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('instruction')
        else:
            messages.error(request, 'Invalid user name')
            return redirect('login')
    else:
        return render(request,'login/register.htm')
def instruction(request):
    participants = Participants.objects.all()

    context = {
        'participants':participants
    }


    return render(request,'login/instruction.htm',context)



def score(answer,key):
    s = list(answer.values())
    c = 0
    for i in range(1,len(key)+1):
        if key[i-1] == answer[i]:
            c += 10
    return c


def quiz(request):
    question = Questions.objects.all()

    paginator = Paginator(question, 1)

    page = request.GET.get('page')

    paged_question = paginator.get_page(page) 
    s = str(paged_question)
    # l = dict()
    print(s[6:8])
    s = int(s[6:8])
    t = []
    for i in question:
        t.append(i.answer_no)
    print(t)

    try:
        if request.method == 'POST':
            a = request.POST['1']
            print(a)
            l[s] = int(a)
            s = request.user

            print(s.first_name)
            if len(l) == len(t):
                # score(l,t)  
                
                print(score(l,t))
                
                db.call(s.first_name,s.last_name,s.email,score(l,t))
                for i in range(1,len(l)+1) :
                    l.pop(i)
                return redirect('results')

    except:
        pass    
    print(l)
    
    context = {     
        'question':paged_question
    }
    return render(request,'questions/quiz.htm',context)


def results(request):
    question = Questions.objects.all()

    score =  Participants.objects.all()
    
    if request.method == 'POST':
        print("yess")
        auth.logout(request)
        return redirect('login')

    user = request.user

    

    context = {
        'question': question,
        'user':user,
        'score':score
    }
    return render(request, 'questions/results.htm',context)
