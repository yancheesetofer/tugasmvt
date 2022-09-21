from django.urls import path
from mywatchlist.models import MyWatchList
from mywatchlist.views import show_mywatchlist, xml_mywatchlist, json_mywatchlist

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name = 'show_mywatchlist'),
    path('xml/', xml_mywatchlist, name='xml_mywatchlist'),
    path('json/', json_mywatchlist, name='json_mywatchlist'),
    path('html/', show_mywatchlist, name = 'show_mywatchlist'),
]