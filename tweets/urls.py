from django.conf.urls import url

from .views import TweetDetailView, TweetListView

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name='list'),
    url(r'^(?P<id>\d+)/$', TweetDetailView.as_view(), name='detail'),
]
