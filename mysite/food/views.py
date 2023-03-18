from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Item
from .forms import ItemForm

# Create your views here.
def index(request):
    item_details=Item.objects.all()
    data={
        'item_details':item_details,
    }
    return render(request,'food/index.html',data)

def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request,'food/detail.html',context)

def Create_item(request):
    form=ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form})

def Edit_item(request,item_id):
    item=Item.objects.get(pk=item_id)
    form=ItemForm(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form,'item':item})

def Delete_item(request,item_id):
    item=Item.objects.get(pk=item_id)
    if request.method=='POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/delete.html',{'item':item})
