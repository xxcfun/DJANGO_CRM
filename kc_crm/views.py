from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
# from django.views.generic import ListView

from business.models import CustomerBusiness
from customer.models import Customer
from liaison.models import Liaison
from record.models import CustomerRecord
from users.models import Count


@login_required
def index(request):
    """ 主页 """
    user = request.user
    if str(user) == '尹明辉' and 'admin':
        all_customer = Customer.objects.filter(is_valid=True).order_by('-created_at')
        all_liaison = Liaison.objects.filter(is_valid=True).order_by('-created_at')
        all_record = CustomerRecord.objects.filter(is_valid=True).order_by('-created_at')
        all_business = CustomerBusiness.objects.filter(is_valid=True).order_by('-created_at')
        customer = all_customer
        liaison = all_liaison
        record = all_record
        business = all_business
    elif str(user) == 'admin':
        all_customer = Customer.objects.filter(is_valid=True).order_by('-created_at')
        all_liaison = Liaison.objects.filter(is_valid=True).order_by('-created_at')
        all_record = CustomerRecord.objects.filter(is_valid=True).order_by('-created_at')
        all_business = CustomerBusiness.objects.filter(is_valid=True).order_by('-created_at')
        customer = all_customer
        liaison = all_liaison
        record = all_record
        business = all_business
    else:
        customer = Customer.objects.filter(user=request.user, is_valid=True).order_by('-created_at')
        liaison = Liaison.objects.filter(user=request.user, is_valid=True).order_by('-created_at')
        record = CustomerRecord.objects.filter(user=request.user, is_valid=True).order_by('-created_at')
        business = CustomerBusiness.objects.filter(user=request.user, is_valid=True).order_by('-created_at')

    paginator_cus = Paginator(customer, 10)
    page_cus = request.GET.get('page_cus')
    try:
        customers = paginator_cus.page(page_cus)
    except PageNotAnInteger:
        customers = paginator_cus.page(1)
    except EmptyPage:
        customers = paginator_cus.page(page_cus.num_pages)

    paginator_lia = Paginator(liaison, 10)
    page_lia = request.GET.get('page_lia')
    try:
        liaisons = paginator_lia.page(page_lia)
    except PageNotAnInteger:
        liaisons = paginator_lia.page(1)
    except EmptyPage:
        liaisons = paginator_lia.page(page_lia.num_pages)

    paginator_rec = Paginator(record, 10)
    page_rec = request.GET.get('page_rec')
    try:
        records = paginator_rec.page(page_rec)
    except PageNotAnInteger:
        records = paginator_rec.page(1)
    except EmptyPage:
        records = paginator_rec.page(page_rec.num_pages)

    paginator_bus = Paginator(business, 10)
    page_bus = request.GET.get('page_bus')
    try:
        businesses = paginator_bus.page(page_bus)
    except PageNotAnInteger:
        businesses = paginator_bus.page(1)
    except EmptyPage:
        businesses = paginator_bus.page(page_bus.num_pages)

    counts = Count.objects.all()

    return render(request, 'index.html', {
        'customer_list': customers,
        'liaison_list': liaisons,
        'record_list': records,
        'business_list': businesses,
        # 每日新增
        'counts': counts,
    })
