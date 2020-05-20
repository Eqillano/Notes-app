from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse,JsonResponse
from .forms import PostCreateForm,PostEditForm
from .models import Post,Category
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
##from .filters import PostFilter
# Create your views here.


def FavouriteList(request):
    favs = Post.objects.filter(favourite=request.user)
    #print(favs)
    context = {'favs':favs}
    template = 'notes1/fav_list.html'
    return render(request,template,context)


def FavouriteView(request,pk):
    post = get_object_or_404(Post,id=request.POST.get('post_id'))
    #marked = False
    if post.favourite.filter(id=request.user.id).exists():
       post.favourite.remove(request.user)
       #marked = False
    else:
       post.favourite.add(request.user)
       #marked = True
    #post.favourite.add(request.user)
    #print(favourite)
    return HttpResponseRedirect(reverse('post-detail',args=[str(pk)]))



def home_view(request):
    context = {
      'posts' : Post.objects.all()
    }
    return render(request,'notes1/home.html',context)


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request,'notes1/category_list.html',{"cat_menu_list":cat_menu_list})








class PostListView(ListView):
     model = Post
     template_name = 'notes1/home.html'
     context_object_name = 'posts'
     ordering = ['-date_posted']


     def get_context_data(self,*args,**kwargs):
         cat_menu = Category.objects.all()
         #posts = Post.objects.all()
         #stuff = get_object_or_404(Post,id=self.kwargs['pk'])
         context = super(PostListView,self).get_context_data(*args,**kwargs)
         #favourite = False
         #if stuff.favourite.filter(id=self.request.user.id).exists:
            #favourite = True
         #my_filter = PostFilter(self.request.GET,queryset=posts)
        # permission = False
         #if self.request.user.id == Post.author.id  :#Post.objects.author.user.id:
            # permission = True

         #context['permission'] = permission
         context['cat_menu'] = cat_menu
        # contextp['favourite'] = favourite
         #context['my_filter'] = my_filter
         return context



class PostDetailView(DetailView):
     model = Post
     fields = ['title','content']

     def get_context_data(self,*args,**kwargs):
         cat_menu = Category.objects.all()
         stuff = get_object_or_404(Post,id=self.kwargs['pk'])
         context = super(PostDetailView,self).get_context_data(*args,**kwargs)
         marked = False
         if stuff.favourite.filter(id=self.request.user.id).exists():
             marked = True
         context['cat_menu'] = cat_menu
         context['marked'] = marked
        # print(favourite)
         return context


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
     model = Post
     success_url = '/'
     def test_func(self):
         post = self.get_object()
         if self.request.user == post.author:
             return True
         return False



class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    #fields = ['title','content','category']
    form_class = PostCreateForm


    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class CategoryCreateView(LoginRequiredMixin,CreateView):
    model = Category
    #form_class =
    fields = ['title']
    template_name = 'notes1/add_category.html'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    from_class = PostEditForm
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




def about(request):
    return HttpResponse("<h1>Blog About</h1>")
