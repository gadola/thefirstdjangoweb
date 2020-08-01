from django.shortcuts import render
from .models  import Post
from django.views.generic import ListView,DetailView
# Create your views here.
# dùng hàm
# def list(request):
#     Data={'Posts':Post.objects.all().order_by('-date')}
#     return render(request, 'blog/blog.html',Data)
# def post(request,id):
#     post=Post.objects.get(id=id)
#     return render(request,'blog/post.html',{'post':post})
# dùng hàm có sẵn của generic 
class PostListView(ListView):
    queryset      = Post.objects.all().order_by("-date")
    template_name = 'blog/blog.html'
    context_object_name = 'Posts'
    paginate_by = 1 # tách ra 2 bài viết mỗi trang 
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'


