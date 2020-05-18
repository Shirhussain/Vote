from django.contrib import admin
from django.urls import path
from blogs.views import BlogListView, BlogDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',BlogListView.as_view(), name="list"),
    path("blog/<int:pk>/",BlogDetailView.as_view(), name="detail"),
]
