from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    data_catalog_item = CatalogItem.objects.all()
    context = {
        'list_barang' : data_catalog_item,
        'nama': 'Yan Christofer S.',
        'npm' : '2106752464'
    }
    return render(request, "katalog.html",context)