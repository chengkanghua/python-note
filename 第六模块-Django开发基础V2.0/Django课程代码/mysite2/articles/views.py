from django.shortcuts import render, HttpResponse


# Create your views here.


def article_detail(request):
    # 查询2012年的文章
    return HttpResponse("2012年的文章")


def article_archive_by_year(request, year):
    print("year:", year)
    # 查询文章
    # select * from articles where year = year
    return HttpResponse("%s年的文章" % year)


'''
def article_archive_by_month(request, year, month):
    print(year, month)
    # 查询文章
    # select * from articles where year = ? and month=?
    return HttpResponse("%s年%s月的文章" % (year, month))
    
'''


# 有名分组

def article_archive_by_month(request, month, year, ):
    print(year, month)
    # 查询文章
    # select * from articles where year = ? and month=?
    return HttpResponse("%s年%s月的文章" % (year, month))
