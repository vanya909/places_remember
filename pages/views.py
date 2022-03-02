from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


@login_required(login_url=reverse_lazy('account_login'))
def home_page_view(request):
    return render(request, 'pages/home.html')
