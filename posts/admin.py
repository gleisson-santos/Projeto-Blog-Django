from django.contrib import admin
from .models import Post, PostImage
from django.db import models
from django_summernote.admin import SummernoteModelAdmin



class PostImageAdmin(admin.StackedInline):
    model = PostImage

class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    list_display = ('id','titulo_post', 'autor_post', 'data_post', 'categoria_post', 'publicado_post', )
    list_editable = ('publicado_post', )
    list_display_links = ('id', 'titulo_post', )
    summernote_fields = ('conteudo_post', )
    inlines = [PostImageAdmin]

admin.site.register(Post, PostAdmin)



