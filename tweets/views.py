from django.shortcuts import render

from .models import Tweet

# Create your views here.

def tweet_detail_view(request, id=1):
    obj = Tweet.objects.get(id=id),
    context = {
        "object": obj
    }
    return render(request, "detail_view.html", context)

def tweet_list_view(request):
    queryset = Tweet.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "list_view.html", context)
