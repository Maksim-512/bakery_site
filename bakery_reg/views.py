from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegistrationForm, LoginForm
from django.contrib import messages


# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Создан аккаунт {username}!')
#             return redirect('login')
#     else:
#         form = RegistrationForm()
#     return render(request, 'bakery_reg/register.html', {'form': form})

class CustomRegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'bakery_reg/register.html'
    extra_context = {'title': 'Регистрация на сайте'}

    def get_success_url(self):
        return reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)


class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'bakery_reg/login.html'
    extra_context = {'title': 'Авторизация на сайте'}

    def get_success_url(self):
        return reverse_lazy('new_main')

