from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import Book

from django.core.paginator import Paginator, EmptyPage


def create_multi(request):
    '''
    insert into book () values
                           ( ),
                           ( ),
                           ( ),
                           ( ),
                           ( ),
                           ( ),
                           ( ),
                           ( ),


    '''

    # 方案1： 1000条insert语句
    # for i in range(1, 1001):
    #     Book.objects.create(title="Book" + str(i), price=i*2)

    # 方案2：

    book_list = []
    for i in range(1, 101):
        book = Book(title="Book" + str(i), price=i * 2)
        book_list.append(book)

    Book.objects.bulk_create(book_list)

    return HttpResponse("批量插入成功")


def index(request):
    book_list = Book.objects.all()

    # (1) 分页对象
    paginator = Paginator(book_list, 2)  # 每页一百条数据

    # 分页信息
    print(paginator.count)  # 1000
    print(paginator.num_pages)  # 13
    print(paginator.page_range)  # 分页列表 range(1, 14)
    try:
        # (2) 获取某页对象
        visit_page_num = int(request.GET.get("page", 1))
        page = paginator.page(visit_page_num)
        # 获取该页的所有数据
        # 方式1：
        # print(page.object_list)
        # 方式2：
        # for book in page:
        #     print(book)

        # 某页对象其他属性

        # print(page02.next_page_number())  #
        # print(page02.previous_page_number())  # 1
        # print(page02.has_next())  # True
        # print(page02.has_previous())  # True

        # page_book_list = page.object_list
        if visit_page_num == 1:
            page_range = range(1, 4)
        elif visit_page_num == paginator.num_pages:
            page_range = range(paginator.num_pages - 2, paginator.num_pages + 1)
        else:
            page_range = [visit_page_num - 1, visit_page_num, visit_page_num + 1]


    except EmptyPage:

        page = paginator.page(1)

    return render(request, "index2.html",
                  {"page": page, "paginator": paginator, "page_range": page_range, "visit_page_num": visit_page_num})
