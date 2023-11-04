"""
This file contains the views for the codequalify app.
"""
from django.shortcuts import render

"""
This view renders the login page.
"""
def login(request):
    return render(request, 'templates/login.html')
