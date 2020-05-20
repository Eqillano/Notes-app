from django import forms
from .models import Post,Category

choices = Category.objects.all().values_list('title','title')


choice_list = []

for item in choices:
    choice_list.append(item)
print(choice_list)

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','category']

        widgets = {
        'title':forms.TextInput(attrs={'class':'form-control'}),
        'content':forms.TextInput(attrs={'class':'form-control'}),
        'category':forms.Select(choices=choice_list,attrs={'class':'form-control'})
        }



class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','category']

        widgets = {
        'title':forms.TextInput(attrs={'class':'form-control'}),
        'content':forms.TextInput(attrs={'class':'form-control'}),
        'category':forms.Select(choices=choice_list,attrs={'class':'form-control'})
        }
