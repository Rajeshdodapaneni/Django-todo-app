from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import todo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
# Create your views here.

@login_required
def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        new_todo = todo(user=request.user, todo_name=task)
        new_todo.save()

    all_todos = todo.objects.filter(user=request.user)
    context = {
        'todos': all_todos
    }
    return render(request, 'todoapp/todo.html', context)

# def register(request):
#     if request.user.is_authenticated:
#         return redirect('home-page')
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         if not username or not email or not password:
#             messages.error(request, 'All fields are required')
#             return redirect('register')

#         if len(password) < 3:
#             messages.error(request, 'Password must be at least 3 characters')
#             return redirect('register')

#         get_all_users_by_username = User.objects.filter(username=username)
#         if get_all_users_by_username:
#             messages.error(request, 'Error, username already exists, User another.')
#             return redirect('register')

#         new_user = User.objects.create_user(username=username, email=email, password=password)
#         new_user.save()

#         messages.success(request, 'User successfully created, login now')
#         return redirect('login')
#     return render(request, 'todoapp/register.html', {})


#alternate toregister
def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            messages.error(request, 'All fields are required')
            return redirect('register')

        if len(password) < 3:
            messages.error(request, 'Password must be at least 3 characters')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, 'User created successfully. Login now')
        return redirect('login')

    return render(request, 'todoapp/register.html')




def LogoutView(request):
    logout(request)
    return redirect('login')

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('home')
        else:
            messages.error(request, 'Error, wrong user details or user does not exist')
            return redirect('login')


    return render(request, 'todoapp/login.html', {})

# @login_required
# def DeleteTask(request, name):
#     get_todo = todo.objects.get(user=request.user, todo_name=name)
#     get_todo.delete()
#     return redirect('home-page')

@login_required
def DeleteTask(request, id):
   task = get_object_or_404(todo, id=id, user=request.user)
   task.delete()
   return redirect('home')



@login_required
def FinishTask(request, id):
    task = todo.objects.get(user=request.user, id=id)
    task.status = not task.status
    task.save()
    return redirect('home')

@login_required
def Update(request, id):
    task=get_object_or_404(todo, id=id, user=request.user)

    if request.method == 'POST':
        task.todo_name = request.POST.get('task')
        task.status = 'status' in request.POST  
        task.save()
        return redirect('home')
    return render(request, 'todoapp/update.html', {'task': task})




# Register-view alternate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'register.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')   # change if your home url name is different
        else:
            messages.error(request, "Invalid username or password")
    return render(request,'newlogin.html')