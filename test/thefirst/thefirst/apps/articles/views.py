from django.shortcuts import render
from .models import Article
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse


def main(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_article_list': latest_article_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Article was not found")

    latest_comments_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Article was not found")

    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['name'])
    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))
