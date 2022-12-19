from django.shortcuts import render,redirect
from .form import RegisterForm
from django.contrib import messages
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


def login(request):
    form = AuthenticationForm
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            if user.is_superuser:
                login(request, user) 
                messages.info(request,  {username}) 
                return redirect("/dot")
            else:
                login(request, user) 
                messages.info(request, {username}) 
                messages.info(request, f"You are now logged in as {id}") 
                return redirect('dot')
                # userquery = User.objects.all().filter(username=user)
                # user_group = ''
                # for x in userquery :
                #     userid= x.id
                #     print(x.groups)
                #     print('########################################################')
                #     group_name=user.groups.all().filter(user=userid)
                #     user_group = group_name[0].name
                #     print(group_name[0].name)
                # if user_group == 'Marketing':
                #     login(request, user) 
                #     messages.info(request, {username}) 
                #     messages.info(request, f"You are now logged in as {id}") 
                #     return redirect('dot')
                # elif user_group == 'customercare':
                #     login(request, user) 
                #     messages.info(request, {username}) 
                #     messages.info(request, f"You are now logged in as {id}") 
                #     return redirect('dot')
                  
        
        else:
            return render(request,"login.html",{'msg':'username or password is incorrect'})
    return render(request, "login.html",{'form': form})

def index(request):
    return render(request, 'dashboard.html')


def dot_add_user(request):
    form = RegisterForm
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            print(username)
            groups = form.cleaned_data.get('groups')
            gr_id = request.POST.getlist('groups')
            idd= gr_id[0]
            print(gr_id)
            # group = Group.objects.get(id=gr[0])
            # print(gr[0])
            for x in  gr_id:
                print(x)
                user.groups.add(x)
            messages.success(request, 'Account was created for' + username)
            return redirect('dot_add_users')
    return render(request,"admin/add_user.html", {"form":form})
