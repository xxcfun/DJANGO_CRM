import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from business.forms import BusinessAddForm, BusinessEditForm
from business.models import CustomerBusiness
from customer.models import Customer
from users.models import Count


@login_required
def business_list(request):
    """查看所有商机信息"""
    business = CustomerBusiness.objects.filter(user=request.user, is_valid=True).order_by('-created_at')
    return render(request, 'business.html', {
        'business': business
    })


@login_required
def business_add(request, pk):
    """添加商机信息"""
    business = None
    now = datetime.datetime.now().day
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = BusinessAddForm(request=request, data=request.POST, instance=business, customer=customer)
        if form.is_valid():
            form.save()
            tody_bus = CustomerBusiness.objects.filter(user=request.user, is_valid=True, created_at__day=now).count()
            Count.objects.get_or_create(user=request.user)
            Count.objects.filter(user=request.user).update(add_bus=tody_bus)
            return redirect('business:business_list')
    else:
        form = BusinessAddForm(request=request, instance=business, customer=customer)
    return render(request, 'business_add.html', {
        'form': form,
    })


@login_required
def business_detail(request, pk):
    """查看和修改商机信息"""
    user = request.user
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


@login_required
def business_delete(request, pk):
    """删除"""
    business = get_object_or_404(CustomerBusiness, pk=pk, user=request.user, is_valid=True)
    business.is_valid = False
    business.save()
    return redirect('business:business_list')


# def bus_add_prod(request, pk):
#     """在商机里添加商品信息"""
#     business = get_object_or_404(CustomerBusiness, pk=pk, user=request.user, is_valid=True)
#     prod_name = request.POST.get('name')
#     prod_number = request.POST.get('number')
#     prod_price = request.POST.get('price')
#     business.product.create(name=prod_name, number=prod_number, price=prod_price)
#
#     return redirect('business:bus_add_prod')

