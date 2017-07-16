from django.conf.urls import url

from .views import (
    TweetDetailView,
    TweetListView,
    TweetCreateView
    # tweet_create_view
)

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name='list'),
    url(r'^create/$', TweetCreateView.as_view(), name='create'),
    # url(r'^create/$', tweet_create_view, name='create'),
    url(r'^(?P<id>\d+)/$', TweetDetailView.as_view(), name='detail'),
]
