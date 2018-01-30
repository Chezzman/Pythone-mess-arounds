from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Muscician, Album


def index(request):
    all_muscicians = Muscician.objects.all()
    return render(request, 'music/index.html',  {'all_muscicians': all_muscicians})


def detail(request, Muscician_id):
    muscician = get_object_or_404(Muscician, pk=Muscician_id)
    return render(request, 'music/detail.html', {'muscician': muscician})
