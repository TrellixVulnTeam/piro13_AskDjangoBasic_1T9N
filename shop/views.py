from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from shop.models import Item
import logging

# logger = logging.etLogger(__name__)

# def post_list(request):
#     logger.error('Somthing went wrong!')

# Create your views here.

def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))


def item_list(request):
    qs = Item.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(name__icontains=q)
    return render(request, 'shop/item_list.html',{
        'item_list':qs,
        'q':q,
    })

# def view1(request):
#     return HttpResponse('hello, ask company')

# def view2(request):
#     return render(request, 'template.html')

# def view3(request):
#     return JsonResponse({'hello':'ask company'})