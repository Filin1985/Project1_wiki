from django.shortcuts import render
import markdown2
from markdown2 import Markdown

from . import util
from .forms import PostModelForm, Edit
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django import forms
import secrets

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


def edit(request, title):
    form = PostModelForm()
    if request.method == 'GET':
        page = util.get_entry(title)

        context = {
            'form': form,
            'edit': Edit(initial={'textarea': page}),
            'title': title
        }

        return render(request, "encyclopedia/edit.html", context)
    else:
        form = Edit(request.POST)
        if form.is_valid():
            textarea = form.cleaned_data["textarea"]
            util.save_entry(title, textarea)
            page = util.get_entry(title)
            page_converted = md.convert(page)

            context = {
                'form': form,
                'page': page_converted,
                'title': title
            }

            return render(request, "encyclopedia/title.html", context)


def search(request):
    query = request.GET.get('q', '')
    if(util.get_entry(query) is not None):
        return HttpResponseRedirect(reverse('title', kwargs={'title': query}))
    else:
        listTitle = []
        for title in util.list_entries():
            if query.upper() in title.upper():
                listTitle.append(title)
            context = {"entries": listTitle,
                       "search": True,
                       "query": query}
        return render(request, "encyclopedia/index.html", context)


def random(request):
    data = util.list_entries()
    randomTitle = secrets.choice(data)
    return HttpResponseRedirect(reverse('title', kwargs={'title': randomTitle}))
