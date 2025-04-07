from django import forms
from .models import Post, Category

#cat_name = [('kosz', 'siata'), ('fiza', 'mata'), ('szachy', 'gra')]
cat_name = Category.objects.all().values_list('name','name')

cat_name_list =[]

for item in cat_name:
    cat_name_list.append(item)

cat_name_slug = Category.objects.all().values_list('slug','slug')

cat_name_list_slug =[]

for item in cat_name_list_slug:
    cat_name_list_slug.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'category_slug', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        name_choices = Category.objects.all().values_list('name', 'name')
        slug_choices = Category.objects.all().values_list('slug', 'slug')

        self.fields['category'].widget = forms.Select(
            choices=name_choices,
            attrs={'class': 'form-control'}
        )
        self.fields['category_slug'].widget = forms.Select(
            choices=slug_choices,
            attrs={'class': 'form-control'}
        )

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }