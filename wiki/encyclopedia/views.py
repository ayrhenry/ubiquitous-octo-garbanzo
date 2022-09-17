from http.client import HTTPResponse
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wikiTitle(request, wikiTitleName):
    return render(request, "encyclopedia/wikiTitle.html", {
        wikiTitleName: util.get_entry(wikiTitleName)
    })
    util.get_entry({wikiTitleName})


asd
