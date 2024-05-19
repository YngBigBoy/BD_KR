# Import the path function from Django's urls module and the views module from this application
from django.urls import path
from . import views

# Define the URL patterns for this application's views
urlpatterns = [
    # The empty path maps to the index view function in the views module
    path('', views.index, name="analytics"),

    # The path 'add-expense' maps to the add_expense view function in the views module
    path('add-expense', views.add_expense, name="add-expenses")
]
