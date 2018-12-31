from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TodoList
from .forms import TodoListForm
from django.contrib import messages

def index(Request):
    if (Request.method=='POST'):
        form=TodoListForm(Request.POST)
        if(form.is_valid()):
            form.save()
            all_items=TodoList.objects.all
            messages.success(Request, 'Item is added successfully...!!!')
            return render(Request,"home.html",{'all_items':all_items})
        else: #trying to add item without text
            all_items=TodoList.objects.all
            messages.success(Request, 'No Item to add...!!!')
            return render(Request,"home.html",{'all_items':all_items})
    else:
        all_items=TodoList.objects.all
        return render(Request,"home.html",{'all_items':all_items}) 

def delete_item(Request,list_id):
    item=TodoList.objects.get(pk=list_id)
    item.delete()
    messages.success(Request, 'Item is deleted successfully...!!!')
    return redirect('home')

def edit_item(Request,list_id):
    item=TodoList.objects.get(pk=list_id)
    if (Request.method=='POST'):
        form=TodoListForm(Request.POST, instance=item)
        if(form.is_valid()):
            form.save()
            messages.success(Request, 'Item is updated successfully...!!!')
            return redirect('home')
        else:#trying to update item without text
            messages.success(Request, 'Item is not updated...!!!')
            return redirect('home')
    else:
        return render(Request,"edit.html",{'items':item}) 

def crossed_item(Request,list_id):
    item=TodoList.objects.get(pk=list_id)
    item.completed=True
    item.save()
    return redirect('home')

def uncrossed_item(Request,list_id):
    item=TodoList.objects.get(pk=list_id)
    item.completed=False
    item.save()
    return redirect('home')
