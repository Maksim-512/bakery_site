from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import RegistrationForm, LoginForm
from django.contrib import messages


def main(request):
    return render(request,
                  'bakery_reg/main.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'bakery_reg/register.html', {'form': form})


class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'bakery_reg/login.html'
    extra_context = {'title': 'Авторизация на сайте'}

    def get_success_url(self):
        return reverse_lazy('main')


# def login(request):
#     return render(request, 'bakery_reg/login.html', {'form': form})

# class RegUser(View):
#
#     def get(self):
#
#
#     def post(self):
