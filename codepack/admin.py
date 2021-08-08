from django.contrib import admin
from .models import Post,HomeModel,Author,Category
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(HomeModel)