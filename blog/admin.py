import imp
from django.contrib import admin
from .models import Profile, Article, Tag
# Register your models here.

admin.site.register(Profile)
admin.site.register(Tag)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ['headline'],}