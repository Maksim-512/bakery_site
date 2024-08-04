from django.shortcuts import render
from django.views import View


def main(request):
    return render(request,
                  'bakery_reg/main.html')

# class RegUser(View):
#
#     def get(self):
#
#
#     def post(self):


