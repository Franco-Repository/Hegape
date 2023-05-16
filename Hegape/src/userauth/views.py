from django.shortcuts import render,redirect
from postgredb.models import CustomUser
from django.contrib import messages
import bcrypt
from django.contrib.auth import logout

# Create your views here.

def login(request):
    return render(request,'auth.html')




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        new_user = CustomUser.objects.create(username=username, password=hashed_password.decode('utf-8'))
        # Handle successful user creation
        return render(request, 'registration_success.html')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            user = None
        if user is not None and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            # Handle successful login
            request.session['user_id'] = user.id
            messages.success(request, 'Sesión Cerrada.')
            return redirect('home')  # Replace 'home' with the appropriate URL name for your home page
        else:
            # Handle invalid login
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html', {'invalid_credentials': True})
    else:
        return render(request, 'login.html')




def logout_view(request):
    logout(request)
    return redirect('login')