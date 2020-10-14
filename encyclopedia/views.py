from django.shortcuts import render
import markdown2
from markdown2 import Markdown

from . import util
from .forms import PostModelForm


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    md = Markdown()
    data = util.get_entry(title)
    context = {'title':title, 'data': md.convert(data)}
    if data is None:
        return render(request, 'encyclopedya/error.html', context)
    else:
        return render(request, "encyclopedia/title.html", context)

def new_page(request):
    form = PostModelForm()
    context = {
        "form": form
    }
    return render(request, 'encyclopedya/new_page.html', context)