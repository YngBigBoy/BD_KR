from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'analytics/index.html')
def add_expense(request):
    return render(request, 'analytics/add_expense.html')