from django.shortcuts import render
from pytube import Playlist as PL
from .forms import data

def index(request):
    form = data(request.POST or None)
    pl = None
    if form.is_valid():
        Playlist = form.cleaned_data['Playlist']
        pl = PL(Playlist)
        pl.download_all()
    context = {'form': form}
    return render(request, 'playlist.html', context)