from django import forms
from blog.models import Post

class CreateBlog(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ['title','body','date','username']