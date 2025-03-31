from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate

# View for user registration
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Create the user and set the password
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            # Add a success message
            messages.success(request, "Your account has been created successfully!")
            
            # Redirect to the login page after successful registration
            return redirect("login")  # You'll need to create the login view next
    else:
        form = RegisterForm()  # Create an empty form for GET requests

    return render(request, "accounts/register.html", {"form": form})

# View for user login
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            # Authenticate the user
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)  # Log the user in
                messages.success(request, "You are now logged in!")
                return redirect('dashboard')  # Redirect to the dashboard (or home page) after successful login
            else:
                messages.error(request, "Invalid credentials. Please try again.")
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})

# View for dashboard after login
def dashboard(request):
    return render(request, "accounts/dashboard.html")


