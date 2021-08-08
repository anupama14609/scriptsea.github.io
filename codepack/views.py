from django.shortcuts import render,HttpResponse
from .models import Author, Post, Category, HomeModel
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

def index(request):
    week_ago = datetime.date.today() - datetime.timedelta(days=7)
    TrendingPost = HomeModel.objects.filter(time_uploade__gte = week_ago).order_by('-read')
    PopularPost = HomeModel.objects.order_by('-read')[:2]
    TopAuthors = Author.objects.order_by('-rate')[:3]
    AuthorPost = [HomeModel.objects.filter(author=topauthor).first() for topauthor in TopAuthors]
   
    all_post=Paginator(HomeModel.objects.filter(publish=True),3)
    page= request.GET.get('page')
    try:
        posts = all_post.page(page)   
    except PageNotAnInteger:
        posts=all_post.page(1)
    except EmptyPage:
        posts=all_post.page(all_post.num_pages)

    context = {
        # 'allPost':HomeModel.objects.filter(publish=True),
        'allPost':posts,
        'trends':TrendingPost,
        'popular':PopularPost,
        'AuthorPosts':AuthorPost,
        'TopAuthors':TopAuthors, 
    }
    return render(request, 'codepack/home.html',context)

def BlogCategory(request):
    cats = Category.objects.all()
    print(cats)
    context = {'allCategory':cats}
    return render(request, 'codepack/home.html',context)

def Blog(request):
    allPosts = Post.objects.all().order_by('-timeStamp')
    paginator = Paginator(allPosts, 5)
    page = request.GET.get('page')
    
    try:
        posts =paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts':posts,
        'page':page,    
    }
    return render(request, 'codepack/blog.html',context)

def BlogPost(request, slug):
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, 'codepack/blogpost.html',context)

def Blogpdf(request):
    posts = Post.objects.all()
    context = {'allPost':posts}
    return render(request, 'codepack/blogpdf.html',context)

def create_pdf_report(request):
    template_path = 'pdfreports/pdfReport.html'
    posts = Post.objects.all()
    context = {'allPost':posts}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ExportBlog.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
  
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



    
   