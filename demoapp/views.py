from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# #--------------
# from django.shortcuts import render
# from .forms import MyForm
# #---------------

# # Create your views here.
# # def home(request):
# #     post=Blog.objects.all()

# #     return render(request,'siva.html',{'post':post})
# # def demo(request):
# #     return render(request,'demo.html',{"age":27})
# def home(request):
#     post=Blog.objects.all()

#     return render(request,'home.html',{'post':post})
# def login(request):
#     return render(request,'login.html')
# def register(request):
#     return render(request,'register.html')


# def my_form(request):
#   if request.method == "POST":
#     form = MyForm(request.POST)
#     if form.is_valid():
#       form.save()
#   else:
#       form = MyForm()
#   return render(request, 'cv-form.html', {'form': form})



# from django.shortcuts import render
# from django.http import HttpResponse


# def home(request):
#     return render(request,'base.html')
def home(request):
    return render(request,'home.html')
def login_page(request):
    return render(request,'login.html')
def registers(request):
    return render(request,'register.html')

def login_request(request):
    if request.method == 'POST':
        username = request.POST['Uname']
        password = request.POST['Pass']
        print('username:',username)
        print('password:',password)
        # user = authenticate(username=username, password=password)
        check = User.objects.get(username=username, password=password)
        # check = User.objects.filter(username=username, password=password)
        print(check)
        if check is not None:
            login(request, check)
            return render(request,'home.html')
        else:
            print('password is invalid')
            return render(request,'login.html')


def registerpage(request):
    if request.method == 'POST':
        fristname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['Repeat_password']
        print(username)
        print(password)
        if password == confirmpassword:
            try:
                user = User.objects.get(username=username)
                if user:
                    print('User name already exists!')
                    return render(request, 'register.html')
            except User.DoesNotExist:
                print('Created successfully!')
                user = User.objects.create(username=username, password=password, last_name=lastname, first_name=fristname)
                return render(request, 'login.html')
        else:
            print('Password and confirm password are not matched!')
            return render(request, 'register.html')
        # print('fristname:',fristname)
        # print('lastname:',lastname)
        # print('password:',password)
        # print('confirmpassword:',confirmpassword)
        # user = authenticate(request, fristname=fristname, lastname=lastname,username=username,password=password,confirmpassword=confirmpassword)
        # check = User.objects.filter(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return render(request,'login.html')
        else:
            print('password is invalid')
            return render(request,'register.html')