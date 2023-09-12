import os
from django.shortcuts import render


def login(request):

    params = {
        "google_client_id": os.environ.get('GOOGLE_CLIENT_ID')
    }
    return render(request, 'auth_ui/google_login.html', params)
