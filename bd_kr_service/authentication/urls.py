# Import necessary modules and views
from .views import LoginView, RegisterView
from django.urls import path

# Define the URL patterns for the application
urlpatterns = [
    # Define a URL pattern for registering a new user
    path('register', 
         # Use the RegisterView from the views.py file
         RegisterView.as_view(), 
         # Set the name of the view for reverse URL lookups
         name='register'),
    # Define a URL pattern for logging in an existing user
    path('login', 
         # Use the LoginView from the views.py file
         LoginView.as_view(), 
         # Set the name of the view for reverse URL lookups
         name='login')
]
