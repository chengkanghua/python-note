from django.shortcuts import render,HttpResponse,redirect
from app01.models import *
# Create your views here.
from django.core.paginator import Paginator,EmptyPage

def index(request):
    # 批量导入数据
    # book_list = []
    # for i in range(100):
    #     book = Book(title="book_%s"%i,price=i*i)
    #     book_list.append(book)
    #     Book.objects.bulk_create(book_list)
    # 清空
    # Book.objects.all().delete()

    book_list = Book.objects.all()
    # 分页器
    paginator = Paginator(book_list,10)
    print('count:',paginator.count)
    print("num_pages",paginator.num_pages)
    print("page_range",paginator.page_range)
    page_range = paginator.page_range

    current_page_num = int(request.GET.get("page",1))
    if paginator.num_pages > 11:
        if current_page_num-5 < 1:
            page_range=range(1,11)
        elif current_page_num+5 > paginator.num_pages:
            page_range=range(paginator.num_pages-10,paginator.num_pages+1)
        else:
            page_range = range(current_page_num-5,current_page_num+6)
    else:
        page_range = paginator.page_range


    try:
        current_page =paginator.page(current_page_num)
        # print("obj_list",current_page.object_list)
    except EmptyPage as e:
        current_page =paginator.page(1)



    return render(request,"index.html",locals())