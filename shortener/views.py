
import random
import string

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from shortener.models import Link


def get_short():
    length = 8
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    short_link = ''.join(random.choice(char) for x in range(length))
    return short_link


class LinkView(CreateView):
    model = Link
    fields = ['httpurl']
    success_url = 'result/'

    def form_valid(self, form):
        short_link = get_short()
        form.instance.short_link = short_link
        super(LinkView, self).form_valid(form)
        return render(self.request, 'shortener/result.html', {'short_link': short_link})


def redirect_original(request, short_link):
    url = get_object_or_404(Link, short_link=short_link)
    url.save()
    return HttpResponseRedirect(url.httpurl)





