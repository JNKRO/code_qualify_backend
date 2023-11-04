"""
This file contains the views for the codequalify app.
"""
from django.shortcuts import render

"""
This view renders the login page.

:param request: the HTTP request
:return: the HTTP response
"""
def login(request):
    return render(request, 'templates/login.html')
