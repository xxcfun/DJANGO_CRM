import datetime

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from business.forms import BusinessAddForm, BusinessEditForm
from business.models import CustomerBusiness
from customer.models import Customer
from users.models import Count


def business_list(request):
    """查看所有商机信息"""
    user = request.session.get('user_id')
    business = CustomerBusiness.objects.filter(user=user, is_valid=True).order_by('-created_at')
    return render(request, 'business.html', {
        'business': business
    })


def business_add(request, pk):
    """添加商机信息"""
    user = request.session.get('user_id')
    business = None
    now = datetime.datetime.now().day
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = BusinessAddForm(request=request, data=request.POST, instance=business, customer=customer)
        if form.is_valid():
            form.save()
            tody_bus = CustomerBusiness.objects.filter(user=user, is_valid=True, created_at__day=now).count()
            Count.objects.get_or_create(user=user)
            Count.objects.filter(user=user).update(add_bus=tody_bus)
            return redirect('business:business_list')
    else:
        form = BusinessAddForm(request=request, instance=business, customer=customer)
    return render(request, 'business_add.html', {
        'form': form,
    })


def business_detail(request, pk):
    """查看和修改商机信息"""
    user = request.session.get('user_id')
    business = get_object_or_404(CustomerBusiness, pk=pk, user=user, is_valid=True)
    if request.method == 'POST':
        form = BusinessEditForm(request=request, data=request.POST, instance=business)
        if form.is_valid():
            form.save()
            return redirect('business:business_list')
    else:
        form = BusinessEditForm(request=request, instance=business)
    return render(request, 'business_detail.html', {
        'form': form,
        'pk': pk
    })


def business_delete(request, pk):
    """删除"""
    user = request.session.get('user_id')
    business = get_object_or_404(CustomerBusiness, pk=pk, user=user, is_valid=True)
    business.is_valid = False
    business.save()
    return redirect('business:business_list')
