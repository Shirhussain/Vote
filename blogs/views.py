from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView
from . models import BlogPost
from tahlil.models import View 


class BlogListView(ListView):
	model = BlogPost
	template_name = "list.html"


class BlogDetailView(DetailView):
	model = BlogPost
	template_name = "detail.html"

	def get_object(self):
		post_query  = BlogPost.objects.filter(pk=self.kwargs.get("pk"))
		if post_query.exists():
			post_object = post_query.first()
			view, created = View.objects.get_or_create( user = self.request.user, post = post_object)
			if view:
				view.views_count += 1 
				view.save()
			return post_object
		raise Http404