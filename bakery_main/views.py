from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView


def main(request):
    return render(request,
                  'bakery_main/new_main.html')

@login_required
def profile_list(request):
    return render(request, 'bakery_main/user_profile_page.html')
