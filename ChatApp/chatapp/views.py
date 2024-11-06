from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required 
import re
from .models import Message
# View which handles login functionality
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username","").strip()
        password = request.POST.get("password","").strip()

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid username or password")
            return redirect('user_login')
    return render(request, 'chatapp/authenticate/login.html',{'messages': messages.get_messages(request)})
# view which takes care of the password strength
def is_strong_password(password):
    """Check if the password is strong."""
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):  # At least one uppercase letter
        return False
    if not re.search(r"[a-z]", password):  # At least one lowercase letter
        return False
    if not re.search(r"[0-9]", password):  # At least one number
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  # At least one special character
        return False
    return True

# View which handles registering the user
def signup(request):
    if request.method == 'POST':
        username =request.POST.get("username","").strip()
        email=request.POST.get("email","").strip()
        password=request.POST.get("password","").strip()


        if not is_strong_password(password):
            messages.error(request, "Password must be at least 8 characters long and include an uppercase letter, lowercase letter, number, and special character.")
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('signup')
        
        myuser = User.objects.create_user(username=username, password=password, email=email)
        myuser.save()

        messages.success(request, "Your account has been successfully created")

        return redirect('signup')

    return render(request, 'chatapp/authenticate/signup.html',{'messages': messages.get_messages(request)})


# View to render home page , login required to access this template
@login_required
def home(request):
    User = get_user_model()  # Get the user model
    if request.user.is_superuser:
        # If the user is a superuser, show all users
        users = User.objects.exclude(username=request.user.username)
    else:
        # For normal users, show only the superuser
        users = User.objects.filter(is_superuser=True)
    
    return render(request, 'chatapp/Chat/home.html', {'users': users})







# def chat_view(request, room_name):
#     messages = Message.objects.filter(room_name=room_name).order_by('timestamp')
#     return render(request, "chatapp/Chat/home.html", {"messages": messages},{'user': request.user})




@login_required
def chat_room(request, username):
    other_user = User.objects.get(username=username)
    room_name = f"chat_{min(request.user.id, other_user.id)}_{max(request.user.id, other_user.id)}"
    messages = Message.objects.filter(room=room_name).order_by('timestamp')
    return render(request, 'chatapp/Chat/chat_room.html', {
        'room_name': room_name,
        'other_user': other_user,
        'messages': messages
    })



