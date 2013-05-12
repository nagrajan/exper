# Create your views here.
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from article.models import Article, Comment
from django.utils import timezone

from django.http import HttpResponse
from forms import ArticleForm, CommentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


def articles(request):
    language = 'en-us'
    session_language = 'en-us'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    return render_to_response('articles.html',
                              {'articles': Article.objects.all(),
                               'language': language,
                               'session_language': session_language})

def article(request, article_id=1):
    f = CommentForm()
    a = Article.objects.get(id=article_id)
    args = {}
    args.update(csrf(request))
    args['article'] = a
    args['comment_form'] = f
    return render_to_response('article.html', args)


def language(request, language='en-us'):
    response = HttpResponse('setting language to %s'%language)
    response.set_cookie('lang', language)
    request.session['lang'] = language

    return response


def create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/articles/all')
    else:
        form = ArticleForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('create_article.html', args)

def like(request, article_id=None):
    if article_id is not None:
        a = Article.objects.get(id=article_id)
        a.likes += 1
        a.save()
    return HttpResponseRedirect('/articles/get/%s'%article_id)

def add_comment(request, article_id=None):
    if article_id is not None:
        a = Article.objects.get(id=article_id)
        if request.method == "POST":
            f = CommentForm(request.POST)
            if f.is_valid():
                c = f.save(commit=False)
                c.pub_date = timezone.now()
                c.article = a
                c.save()
                return HttpResponseRedirect('/articles/get/%s'%article_id)
        else:
            f = CommentForm()
    else:
        f = CommentForm()

    args = {}
    args.update(csrf(request))
    args['article'] = a
    args['form'] = f

    return render_to_response('add_comment.html', args)






