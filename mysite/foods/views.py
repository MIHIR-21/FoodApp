from django.shortcuts import render, redirect
from .forms import ItemForm
from django.http import HttpResponse
from foods.models import Item

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'foods/index.html', context)


def item(request):
    return HttpResponse("<h1>This is item in the view.</h1>")

def detail(request,item_id):
    item = Item.objects.get(id=item_id)
    context = {
        'item': item,
    }
    return render(request, "foods/detail.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('foods:index')
    
    return render(request, 'foods/item-form.html', {'form': form})

def update_item(request , id):
    item = Item.objects.get(id=id) 
    
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('foods:index')
    
    return render(request, 'foods/item-form.html', {'form': form, 'item': item})

def delete_item(request, id):
    item = Item.objects.get(id = id)

    if request.method == 'POST':
        item.delete() 
        return redirect('foods:index')

    return render(request, 'foods/item-delete.html', {'item' : item})