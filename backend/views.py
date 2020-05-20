from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm,LoginForm, newEvent, searchEvent
from django.contrib import messages
from .models import Profile,Event
from django.urls import path
from datetime import datetime
import re
from validate_email import validate_email


    
# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'backend/index.html')

def register(request):
    if request.method== 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid:
            email=request.POST.get('email','')
            username=request.POST.get('username','')
            password=request.POST.get('password1','')
            password2=request.POST.get('password2', '')
            if isValidUsername(username) and isValidEmail(email) and passMatch(password,password2):
                obj=Profile(username=username,email=email, password=password) 
                obj.save()
                messages.add_message(request,messages.SUCCESS, "You have registered successfully")
                return redirect('/backend/login',{'messages':messages})
            else:
                messages.add_message(request,messages.ERROR, "Invalid Input")
                print(messages)
                return render(request, 'backend/signup.html', {'form': form})
    else :
        form=SignUpForm()
    
    return render(request, 'backend/signup.html', {'form': form})

def login(request):
    if request.method== 'POST':
        form=LoginForm(request.POST)
        if form.is_valid:
            email=request.POST.get('email','')
            password=request.POST.get('password','')
            try:
                user=Profile.objects.get(email=email)
                print(user)
                print(user.password)
                print(user.user_id)
                if user.password == password:
                   return redirect('/backend/dashboard/'+user.user_id)
                else:
                    messages.info(request, 'Username OR password is incorrect')
            except:
                 messages.info(request, 'Username OR password is incorrect')
    else:
        print(messages)
        form=LoginForm()
    return render(request, 'backend/login.html', {'form': form})

def dashboard(request,pk):
    try:
        user=Profile.objects.get(user_id=pk)
        context={'user':user}
        print(user)
        return render(request, 'backend/dashboard.html', context)
    except:
        return HttpResponse('404 PAGE NOT FOUND')

def create(request,pk):
    try:
        if request.method== 'POST':
            form=newEvent(request.POST)
            if form.is_valid:
                title=request.POST.get('title','')
                date=request.POST.get('date','')
                print(title+' '+date)
                user=Profile.objects.get(user_id=pk)
                event=Event(title=title, date=date, user=user)
                event.save()
                messages.add_message(request, messages.SUCCESS, "Event Created ")
                return render(request, 'backend/create.html', {'form':form})
        else:
            form=newEvent()
            user=Profile.objects.get(user_id=pk)
            context={'user':user, 'form':form}
        return render(request, 'backend/create.html', context)
    except:
            form=newEvent()
            messages.add_message(request,messages.ERROR, "Invalid Date Input: Note that Date should be in the form YYYY-MM-DD")
            return render(request, 'backend/create.html', {'form':form})


def show(request,pk):
    user=Profile.objects.get(user_id=pk)
    events=Event.objects.filter(user=user)
    print(events)
    context={'user':user, 'events':events}
    return render(request, 'backend/show.html', context )

def delete(request,pk):
    try:
        if request.method== 'POST':
            form=searchEvent(request.POST)
            if form.is_valid:
                title=request.POST.get('title','')
                user=Profile.objects.get(user_id=pk)
                event=Event.objects.get(title=title, user=user)
                event.delete()
                context={'user':user, 'form':form}
                messages.add_message(request, messages.SUCCESS, 'Event Deleted Successfully!')
                return render(request, 'backend/delete.html', context)
        else:
            form=searchEvent()
            user=Profile.objects.get(user_id=pk)
            context={'user':user, 'form':form}
        return render(request, 'backend/delete.html', context)
    except:
        context={'user':user, 'form':form}
        messages.add_message(request, messages.ERROR, 'Did not find any Event by that name. Check your Scheduled Events!')
        return render(request, 'backend/delete.html', context)

def update(request,pk):
    try:
        if request.method== 'POST':
            form=searchEvent(request.POST)
            if form.is_valid:
                title=request.POST.get('title','')
                user=Profile.objects.get(user_id=pk)
                event=Event.objects.get(title=title, user=user)
                context={'user':user, 'events':event}
                print(event)
                return redirect('/backend/update2/'+user.user_id +'/'+title)

        else:
            form=searchEvent()
            user=Profile.objects.get(user_id=pk)
            context={'user':user, 'form':form}
        return render(request, 'backend/update.html', context)
    except:
        context={'user':user, 'form':form}
        messages.add_message(request, messages.ERROR, 'Did not find any Event by that name. Check your Scheduled Events!')
        return render(request, 'backend/update.html', context)
def update2(request,pk1, pk2):
    try:
        if request.method== 'POST':
            form=newEvent(request.POST)
            if form.is_valid:
                title=request.POST.get('title','')
                date=request.POST.get('date','')
                user=Profile.objects.get(user_id=pk1)
                event=Event.objects.get(title=pk2, user=user)
                event.title=title
                event.date=date
                event.save()
                context={'user':user, 'form':form, 'event':event}
                messages.add_message(request,messages.SUCCESS, "Event Updated Sucessfully!")
                return render(request, 'backend/update2.html', context)
        else:
            user=Profile.objects.get(user_id=pk1)
            event=Event.objects.get(title=pk2, user=user)
            form=newEvent(initial={'title':event.title, 'date':event.date})
            context={'user':user, 'form':form, 'event':event}
        return render(request, 'backend/update2.html', context)
    except:
        context={'user':user, 'form':form, 'event':event}
        messages.add_message(request,messages.ERROR, "Invalid Date Input: Note that Date should be in the form YYYY-MM-DD")
        return render(request, 'backend/update2.html', context)
def isValidUsername(value):
    if not re.match(r'[a-zA-Z0-9_@#-]+', value):
        return False
    else :
        if value[0]>='1' and value<='9':
           return False
        else :
            return True

def passMatch(a,b):
    if a == b :
        return True
    else :
        return False

def isValidEmail(email):
    try:
        validate_email(email)
    except:
        return False
    else:
        return True