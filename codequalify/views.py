"""
This file contains the views for the codequalify app.
"""
from django.shortcuts import render

def login(request):
    """
    This function renders the login page.
    
    Parameters:
        request: the request object

    Returns:
        The rendered login page.
    """
    return render(request, 'templates/login.html')
