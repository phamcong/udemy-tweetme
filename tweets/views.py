from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Tweet

# Create your views here.

class TweetDetailView(DetailView):
    # template_name = "detail_view.html"
    queryset = Tweet.objects.all()

    def get_object(self):
        id = self.kwargs.get('id')
        return Tweet.objects.get(id=id) # we can use get_object_or_404(Tweet, id=id)

class TweetListView(ListView):
    # template_name = "list_view.html" # use this if template file is different with default name: tweet_list.html.
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context



# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id),
#     context = {
#         "object": obj
#     }
#     return render(request, "detail_view.html", context)
#
# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "list_view.html", context)
