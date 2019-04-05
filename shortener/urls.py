from django.conf.urls import url
from django.urls import path

from shortener.views import LinkView, redirect_original

urlpatterns = [
    path('', LinkView.as_view()),
    url(r'^(?P<short_link>\w{8})$', redirect_original, name='redirectoriginal'),

]