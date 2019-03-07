# models.py에 있는 Blog 객체를 기반으로 입력공간(form)을 만들 것이기 때문에 blogapp 안에 form.py 만듦

from django import forms
from .models import Blog

class BlogPost(forms.ModelForm): # model 기반
    class Meta:
        model = Blog
        fields = ['title', 'body']

# class BlogPost(forms.Form):
#     email = forms.EmailField()
#     files = forms.FileField()
#     url = forms.URLField()
#     words= forms.CharField(max_length=200)
#     max_number = forms.ChoiceField(choices=[('1','one'),('2','two'),('3','three')])

