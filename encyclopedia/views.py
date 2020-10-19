from django.shortcuts import render
import markdown2
from markdown2 import Markdown

from . import util
from .forms import PostModelForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

md = Markdown()


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):
    data = util.list_entries()
    if title in data:
        page = util.get_entry(title)
        page_md = md.convert(page)

        context = {
            'page': page_md,
            'title': title,
        }

        return render(request, "encyclopedia/title.html", context)
    else:
        return render(request, "encyclopedia/error.html", {"message": "We don't have page with this title."})


def newPage(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            data = util.list_entries()
            if title in data:
                return render(request, "encyclopedia/error.html", {"message": "This title is already created"})
            else:
                util.save_entry(title, content)
                page = util.get_entry(title)
                page_md = md.convert(page)

                context = {
                    'page': page_md,
                    'title': title
                }

            return render(request, 'encyclopedia/title.html', context)

    else:
        return render(request, "encyclopedia/newpage.html", {
            'form': PostModelForm()
        })
