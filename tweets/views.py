from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView

from .forms import TweetModelForm
from .models import Tweet

# Create your views here.
# CLASS based views
class TweetCreateView(CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_form.html'
    success_url = '/tweet/create/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)

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

#------------------
# FUNCTION based views

# def tweet_create_view(request):
#     form = TweetModelForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.user = request.user
#         instance.save()
#
#     context = {
#         "form": form
#     }
#
#     return render(request, 'tweets/create_form.html', context)

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
