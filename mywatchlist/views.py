from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    the_watchlist = MyWatchList.objects.all()
    context = {
        'watchlist': the_watchlist,
        'name': 'yan'
    }
    return render(request, "mywatchlist.html", context)

def xml_mywatchlist(request):
    the_watchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", the_watchlist), content_type="application/xml")

def json_mywatchlist(request):
    the_watchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", the_watchlist), content_type="application/json")