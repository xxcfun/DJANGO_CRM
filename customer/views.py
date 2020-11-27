import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404

from business.models import CustomerBusiness
from customer.forms import CustomerForm
from customer.models import Customer
from liaison.models import Liaison
from record.models import CustomerRecord
from users.models import Count


def customer_list(request):
    """查看所有客户信息"""
    user = request.session.get('user_id')
    if 'name' in request.GET and request.GET['name']:
        name = request.GET['name']
        customer = Customer.objects.filter(name__icontains=name, user=user, is_valid=True).order_by('-created_at')
    else:
        customer = Customer.objects.filter(user=user, is_valid=True).order_by('-created_at')
    paginator = Paginator(customer, 10)
    page = request.GET.get('page')
    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)

    return render(request, 'customer.html', {
        'customers': customers
    })


def customer_add(request):
    """添加客户信息"""
    user = request.session.get('user_id')
    customer = None
    now = datetime.datetime.now().month
    if request.method == 'POST':
        form = CustomerForm(request=request, data=request.POST, instance=customer)
        if form.is_valid():
            form.save()
            tody_cus = Customer.objects.filter(user=user, is_valid=True, created_at__month=now).count()
            Count.objects.get_or_create(user=user)
            Count.objects.filter(user=user).update(add_cus=tody_cus)
            return redirect('customer:customer_list')
    else:
        form = CustomerForm(request=request, instance=customer)
    return render(request, 'customer_add.html', {
        'form': form
    })


def customer_detail(request, pk):
    """查看和修改客户信息"""
    """获取客户详细信息"""
    user = request.user
    customer = get_object_or_404(Customer, pk=pk, is_valid=True)
    # 拿到该客户名称，存到session中，供后面使用
    cus_name = str(customer)
    request.session['name'] = cus_name
    if request.method == 'POST':
        form = CustomerForm(request=request, data=request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer:customer_list')
    else:
        form = CustomerForm(request=request, instance=customer)
    """获取该客户的其他信息"""
    businesse_list = CustomerBusiness.objects.filter(customer=customer, is_valid=True)
    liaison_list = Liaison.objects.filter(customer=customer, is_valid=True)
    record_list = CustomerRecord.objects.filter(customer=customer, is_valid=True)
    return render(request, 'customer_detail.html', {
        'form': form,
        'businesse_list': businesse_list,
        'liaison_list': liaison_list,
        'record_list': record_list,
        'cus_id': pk,
    })


def customer_edit(request, pk):
    """单个修改界面"""
    user = request.session.get('user_id')
    customer = get_object_or_404(Customer, pk=pk, user=user, is_valid=True)
    if request.method == 'POST':
        form = CustomerForm(request=request, data=request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer:customer_list')
    else:
        form = CustomerForm(request=request, instance=customer)
    return render(request, 'customer_edit.html', {
        'form': form,
    })


def customer_delete(request, pk):
    """删除客户信息"""
    user = request.session.get('user_id')
    customer = get_object_or_404(Customer, pk=pk, user=user, is_valid=True)
    customer.is_valid = False
    customer.save()
    return redirect('customer:customer_list')
