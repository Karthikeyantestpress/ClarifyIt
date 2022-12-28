from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def cover_page(request):
    return render(request, "cover_page.html")


@login_required
def home(request):
    return render(request, "clarifyit/home.html")
