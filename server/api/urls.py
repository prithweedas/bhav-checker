from django.conf.urls import url
from .views import search_equity_name
urlpatterns = [
    url(r'^search/$', search_equity_name),
]
