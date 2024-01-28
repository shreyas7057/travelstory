from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

def RegisterUser(request):
    if request.method == "POST":
        email = request.POST.get("email")
        full_name = request.POST.get("full_name")
        password = request.POST.get("password")
        user = User(
            email = email,
            full_name = full_name,
            password = password
        )
        user.is_traveler = True
        user.is_staff = True
        user.is_active = True
        user.set_password(password)
        user.save()
        # messages.success
        return redirect('login-user')
    
    return render(request,'accounts/register_user.html')


def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            if user.is_traveler and user.is_active:
                # messages sucess
                return redirect('traveler_dashboard')
            
            if user.is_staff and user.is_active:
                # messages success
                return redirect('traveler_dashboard')
        
        else:
            # messages error
            return redirect('login-user')

    return render(request,'accounts/login_user.html')


@login_required(login_url='login-user')
def logout_user(request):
    logout(request)
    # messages success
    return redirect('login-user')