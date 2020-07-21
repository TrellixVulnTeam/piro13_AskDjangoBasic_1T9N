from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from shop.models import Item

# Create your views here.

def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))

# def item_list(request):
#     qs = Item.objects.all()
#     return render(request, 'shop/item_list.html',{
#         'item_list':qs,
#     })

# def view1(request):
#     return HttpResponse('hello, ask company')

# def view2(request):
#     return render(request, 'template.html')

# def view3(request):
#     return JsonResponse({'hello':'ask company'})