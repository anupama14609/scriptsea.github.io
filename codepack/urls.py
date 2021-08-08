from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="CodePackHome"),
    path('blog/', views.Blog, name="CodepackBlog"),
    path('blog/<str:slug>/', views.BlogPost, name="CodepackBlogPost"),
    path('blogpdf/', views.Blogpdf, name="blogpdf"),
    path('blogpdf/create-pdf/', views.create_pdf_report, name="create-pdf"),

]
