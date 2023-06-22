from django.shortcuts import render, redirect
from django.views.generic.base import View

from form import CommentsForm
from .models import Post, Likes



class PostView(View):
    """Вывод записей"""
    def get(self, request):
        posts = Post.objects.all()
        return render(request, "blog/blog.html", {'post_list' : posts})

class PostDetall(View):
    """ отдельная страница записи """
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {'post': post})

class AddComments(View):
    """ Добавление комментариев """
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')
    
def get_client_in(request):
    x_forwarded_for = request.META.get('HTTP_x_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(('.'))[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_in(request=request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')

class DelLike(View):
    def get(self, request, pk):
        ip_client = get_client_in(request=request)
        try:
            like = Likes.objects.get(ip=ip_client)
            like.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')
        