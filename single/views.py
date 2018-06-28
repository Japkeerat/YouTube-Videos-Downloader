from django.shortcuts import render
from pytube import YouTube as YT
from .forms import data

def index(request):
    form = data(request.POST or None)
    v = None
    if form.is_valid():
        Video = form.cleaned_data['Video']
        YT(Video).streams.first().download()
    context = {'form': form}
    return render(request, 'single.html', context)