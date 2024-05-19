from django.shortcuts import render

# Create your views here.

def index(request):
    """
    This view function renders the index.html template, which is the main page
    for the analytics application. It is the first page users see when they
    access the analytics app.

    Parameters:
    request (HttpRequest): The incoming HTTP request object.

    Returns:
    HttpResponse: An HTTP response containing the rendered index.html template.
    """
    return render(request, 'analytics/index.html')

def add_expense(request):
    """
    This view function renders the add_expense.html template, which is the page
    for adding a new expense in the analytics application. It allows users to
    input the details of a new expense and save it to the database.

    Parameters:
    request (HttpRequest): The incoming HTTP request object.

    Returns:
    HttpResponse: An HTTP response containing the rendered add_expense.html template.
    """
    return render(request, 'analytics/add_expense.html')
