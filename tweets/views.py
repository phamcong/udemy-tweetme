from django.shortcuts import render
from django.urls import reverse_lazy
from django import forms
from django.forms.utils import ErrorList
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from .forms import TweetModelForm
from .models import Tweet
from .mixins import FormUserNeededMixin, UserOwnerMixin

# Create your views here.
# CLASS based views
# Check logged in user: FormUserNeededMixin. We can use also LoginRequired mixin.
class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/tweet_create.html'
    # success_url = '/tweet/create/'
    # success_url = reverse_lazy("tweet:detail")

class TweetUpdateView(UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/tweet_update.html'
    success_url = '/tweet/'

class TweetDeleteView(DeleteView):
    model = Tweet
    success_url = reverse_lazy("list") # or some named url like "create", "detail". We can add app namespace like. "tweet:list".

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        return Tweet.objects.get(id=pk) # we can use get_object_or_404(Tweet, id=id)

class TweetListView(ListView):
    # template_name = "list_view.html" # use this if template file is different with default name: tweet_list.html.
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context
