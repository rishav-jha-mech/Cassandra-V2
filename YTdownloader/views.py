from django.shortcuts import HttpResponse, redirect, render
from pytube import *
from django.contrib import messages
from django.conf.urls import handler404,handler500

# defining function
def yt(request):
  
    # checking wheather request.method is post or not
    if request.method == 'POST':
        
        # getting link from frontend
        link = request.POST['link']
        video = YouTube(link)
        embedLink = link.replace("watch?v=", "embed/")
        #print(video.streams.all)
        a=video.streams.filter(progressive=False, only_video=True)
        b=video.streams.filter(only_audio=True)
        c=video.streams.filter(progressive=True)
        messages.add_message(request, messages.INFO, 'Hello world.')
        context={
            'yobj' : video,
            'embedLink' : embedLink,
            'onlyVideo' :      a,
            'onlyAudio':       b,
            'bothVideoAudio' : c,
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html')

def handler404(request, exception):
    return render(request,'404.html')

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)

def admin(request):
    return redirect('home')
def accadmin(request):
    return redirect('home')

