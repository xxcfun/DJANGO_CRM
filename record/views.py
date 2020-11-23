import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from customer.models import Customer
from record.forms import RecordEditForm, RecordAddForm
from record.models import CustomerRecord
from users.models import Count


@login_required
def record_list(request):
    """查看所有客户拜访记录信息"""
    record = CustomerRecord.objects.filter(user=request.user, is_valid=True).order_by('-created_at')
    return render(request, 'record.html', {
        'record': record
    })


@login_required
def record_add(request, pk):
    """添加客户拜访记录"""
    record = None
    now = datetime.datetime.now().day
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = RecordAddForm(request=request, data=request.POST, instance=record, customer=customer)
        if form.is_valid():
            form.save()
            tody_rec = CustomerRecord.objects.filter(user=request.user, is_valid=True, created_at__day=now).count()
            Count.objects.get_or_create(user=request.user)
            Count.objects.filter(user=request.user).update(add_rec=tody_rec)
            return redirect('record:record_list')
    else:
        form = RecordAddForm(request=request, instance=record, customer=customer)
    return render(request, 'record_add.html', {
        'form': form
    })


@login_required
def record_detail(request, pk):
    """修改客户拜访记录"""
    record = get_object_or_404(CustomerRecord, pk=pk, is_valid=True)
    if request.method == 'POST':
        form = RecordEditForm(request=request, data=request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('record:record_list')
    else:
        form = RecordEditForm(request=request, instance=record)
    return render(request, 'record_detail.html', {
        'form': form
    })


@login_required
def record_delete(request, pk):
    """删除客户拜访记录"""
    record = get_object_or_404(CustomerRecord, pk=pk, user=request.user, is_valid=True)
    record.is_valid = False
    record.save()
    return redirect('record:record_list')
