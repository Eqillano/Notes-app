from django.shortcuts import render
from notes1.models import Post
from django.views.generic import ListView
from django.db.models import Q

# Create your views here.

class SearchView(ListView):
    template_name = 'search/view.html'


    def get_context_data(self,*args,**kwargs):
        context = super(SearchView,self).get_context_data(*args,**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


    def get_queryset(self,*args,**kwargs):
        request = self.request
        query = request.GET.get('q',None)
        if query is not None:
            lookups = Q(title__icontains=query)|Q(content__icontains=query)|Q(category__icontains=query)
            #print(lookups)
            result = Post.objects.filter(lookups).distinct()
            #print(result)
            return result
        return Post.objects.all()
