import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from customer.models import Customer
from liaison.forms import LiaisonAddForm, LiaisonEditForm
from liaison.models import Liaison
from users.models import Count


@login_required
def liaison_list(request):
    """查看所有联系人信息"""
    if 'name' in request.GET and request.GET['name']:
        name = request.GET['name']
        liaison = Liaison.objects.filter(name__icontains=name, is_valid=True).order_by('-created_at')
    else:
        liaison = Liaison.objects.filter(user=request.user, is_valid=True).order_by('-created_at')
    return render(request, 'liaison.html', {
        'liaison': liaison
    })


@login_required
def liaison_add(request, pk):
    """添加联系人信息"""
    liaison = None
    now = datetime.datetime.now().day
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = LiaisonAddForm(request=request, data=request.POST, instance=liaison, customer=customer)
        if form.is_valid():
            form.save()
            tody_lia = Liaison.objects.filter(user=request.user, is_valid=True, created_at__day=now).count()
            Count.objects.get_or_create(user=request.user)
            Count.objects.filter(user=request.user).update(add_lia=tody_lia)
            return redirect('liaison:liaison_list')
    else:
        form = LiaisonAddForm(request=request, instance=liaison, customer=customer)
    return render(request, 'liaison_add.html', {
        'form': form,
    })


@login_required
def liaison_detail(request, pk):
    """修改联系人信息"""
    liaison = get_object_or_404(Liaison, pk=pk, is_valid=True)
    if request.method == 'POST':
        form = LiaisonEditForm(request=request, data=request.POST, instance=liaison)
        if form.is_valid():
            form.save()
            return redirect('liaison:liaison_list')
    else:
        form = LiaisonEditForm(request=request, instance=liaison)
    return render(request, 'liaison_detail.html', {
        'form': form
    })


@login_required
def liaison_delete(request, pk):
    """删除联系人信息"""
    liaison = get_object_or_404(Liaison, pk=pk, user=request.user, is_valid=True)
    liaison.is_valid = False
    liaison.save()
    return redirect('liaison:liaison_list')
