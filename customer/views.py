import datetime
from io import StringIO

import xlwt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from business.models import CustomerBusiness
from customer.forms import CustomerForm
from customer.models import Customer
from liaison.models import Liaison
from record.models import CustomerRecord
from users.models import Count


@login_required
def customer_list(request):
    """查看所有客户信息"""
    if 'name' in request.GET and request.GET['name']:
        name = request.GET['name']
        customer = Customer.objects.filter(name__icontains=name, user=request.user, is_valid=True).order_by('-created_at')
    else:
        customer = Customer.objects.filter(user=request.user, is_valid=True).order_by('-created_at')
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


@login_required
def customer_add(request):
    """添加客户信息"""
    customer = None
    now = datetime.datetime.now().month
    if request.method == 'POST':
        form = CustomerForm(request=request, data=request.POST, instance=customer)
        if form.is_valid():
            form.save()
            tody_cus = Customer.objects.filter(user=request.user, is_valid=True, created_at__month=now).count()
            Count.objects.get_or_create(user=request.user)
            Count.objects.filter(user=request.user).update(add_cus=tody_cus)
            return redirect('customer:customer_list')
    else:
        form = CustomerForm(request=request, instance=customer)
    return render(request, 'customer_add.html', {
        'form': form
    })


@login_required
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


@login_required
def customer_edit(request, pk):
    """单个修改界面"""
    user = request.user
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


@login_required
def customer_delete(request, pk):
    """删除客户信息"""
    customer = get_object_or_404(Customer, pk=pk, user=request.user, is_valid=True)
    customer.is_valid = False
    customer.save()
    return redirect('customer:customer_list')


# """客户信息导出到excel"""
# def export_excel(request):
#     """设置HTTP response的类型"""
#     response = HttpResponse(content_type='application/vnd.ma-excel')
#     response['Content-Disposition'] = 'attachment;filename=customer.xls'
#     # new一个文件
#     wb = xlwt.Workbook(encoding='utf-8')
#     # new一个sheet
#     sheet = wb.add_sheet(u'客户名单')
#     # 修护一些样式， style_heading, style_body, style_red, style_green
#     style_heading = xlwt.easyxf("""
#         font:
#             name Arial,
#             colour_index white,
#             bold on,
#             height 0xA0;
#         align:
#             wrap off,
#             vert center,
#             horiz center;
#         pattern:
#             pattern solid,
#             fore_colour 0x19;
#         borders:
#             left THIN,
#             right THIN,
#             top THIN,
#             bottom THIN;
#         """
#     )
#     style_body = xlwt.easyxf("""
#         font:
#             name Arial,
#             bold off,
#             height 0XA0;
#         align:
#             wrap on,
#             vert center,
#             horiz left;
#         borders:
#             left THIN,
#             right THIN,
#             top THIN,
#             bottom THIN;
#         """
#     )
#     style_green = xlwt.easyxf("pattern: pattern solid, fore-colour 0x11;")
#     style_red = xlwt.easyxf("pattern: pattern solid, fore-colour 0x0A;")
#     fmts = [
#         'M/D/YY',
#         'D-MMM-YY',
#         'D-MMM',
#         'MMM-YY',
#         'h:mm AM/PM',
#         'h:mm:ss AM/PM',
#         'h:mm',
#         'h:mm:ss',
#         'M/D/YY h:mm',
#         'mm:ss',
#         '[h]:mm:ss',
#         'mm:ss.0',
#     ]
#     style_body.num_format_str = fmts[0]
#
#     # 写标题栏
#     sheet.write(0, 0, '客户名称', style_heading)
#     sheet.write(0, 1, '客户级别', style_heading)
#     sheet.write(0, 2, '客户网址', style_heading)
#     sheet.write(0, 3, '客户规模', style_heading)
#     sheet.write(0, 4, '客户性质', style_heading)
#     sheet.write(0, 5, '客户行业', style_heading)
#     sheet.write(0, 6, '客户备注', style_heading)
#     sheet.write(0, 7, '创建人', style_heading)
#     sheet.write(0, 8, '创建时间', style_heading)
#     sheet.write(0, 9, '修改时间', style_heading)
#     sheet.write(0, 10, '是否有效', style_heading)
#
#     # 写数据
#     row = 1
#     for cus in Customer.objects.all():
#         sheet.write(row, 0, cus.name, style_body)
#         sheet.write(row, 1, cus.rank, style_body)
#         sheet.write(row, 2, cus.website, style_body)
#         sheet.write(row, 3, cus.scale, style_body)
#         sheet.write(row, 4, cus.nature, style_body)
#         sheet.write(row, 5, cus.industry, style_body)
#         sheet.write(row, 6, cus.remarks, style_body)
#         sheet.write(row, 7, cus.user, style_body)
#         sheet.write(row, 8, cus.created_at, style_body)
#         sheet.write(row, 9, cus.updated_at, style_body)
#         sheet.write(row, 10, cus.is_valid, style_body)
#         row = row + 1
#
#     # 写出到IO
#     output = StringIO()
#     wb.save(output)
#     # 重新定位到开始
#     output.seek(0)
#     response.write(output.getvalue())
#     return response
