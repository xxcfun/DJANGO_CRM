import xlwt
from django.http import HttpResponse


def export_excel(request):
    # 设置httpresponse的类型
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=user.xls'
    # new一个文件
    wb = xlwt.Workbook(encoding='utf-8')
    # new一个sheet
    sheet = wb.add_sheet(u'客户列表按')
    style_heading = xlwt.easyxf("""
        font:
            name Arial,
            colour_index white,
            bold on,
            height 0xA0;
        align:
            wrap off,
            vert center,
            horiz center;
        pattern:
            pattern solid,
            fore-colour 0x19;
        borders:
            left THIN,
            right THIN,
            top THIN,
            bottom THIN;
        """
    )
    style_body = xlwt.easyxf("""
        font:
            name Arial,
            bold off,
            height 0XA0;
        align:
            wrap on,
            vert center,
            horiz left;
        borders:
            left THIN,
            right THIN,
            top THIN,
            bottom THIN;
    """
    )