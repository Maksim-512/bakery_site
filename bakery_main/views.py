from django.shortcuts import render


def main(request):
    return render(request,
                  'bakery_main/new_main.html')
