from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from . import models  # Article


def hello(request):
    request.encoding='utf-8'
    if 'name' in request.GET and request.GET['name']:
        message = '你姓名的内容为: ' + request.GET['name']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
    # 保存数据
    # article = models.Article(title="demo", context="12312312sdfasdfasdf")
    # article.save()

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    # list = models.Article.objects.all()
    # return render(request, 'index.html', {'article': list})

    # 获取单个对象
    # list=models.Article.objects.get(id=9)
    # return render(request, 'index.html', {'article': (list,)})

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    # list = models.Article.objects.filter(title=5)
    # return render(request, 'index.html', {'article': list})

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    # list = models.Article.objects.order_by('title')[0:2]
    # return render(request, 'index.html', {'article': list})

    # 上面的方法可以连锁使用
    # list = models.Article.objects.filter(title="1").order_by("id")
    # return render(request, 'index.html', {'article': list})
