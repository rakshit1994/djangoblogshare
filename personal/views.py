from django.shortcuts import render
from django.shortcuts import render_to_response
from blog.models import Post
from django.http import HttpResponse
from forms import CreateBlog
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

# Create your views here.
def base(request):
	return render(request,'index.html')

def index(request):
	return render(request,'index.html')

def profile(request):
	return render(request,'index.html')

def contact(request):
	return render(request,'personal/contact.html',{'content':['Contact me:','singhrakshit@gmail.com']})

def create(request):
	if request.POST:
		form = CreateBlog(request.POST)
		if form.is_valid():
			blog = form.save(commit=False)
	        blog.username = request.user.username
	        blog.save()
		return HttpResponseRedirect('/blog')
	else:
		form = CreateBlog()

	args={}
	args.update(csrf(request))
	args['form'] = form

	return render(request,'blog/createblog.html',args)