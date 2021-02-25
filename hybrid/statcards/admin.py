from django.contrib import admin
from .models import *


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'author', 'publish', 'status')
#     list_filter = ('status', 'created', 'publish', 'author')
#     search_fields = ('title', 'body')
#     prepopulated_fields = {'slug': ('title',)}
#     raw_id_fields = ('author',)
#     date_hierarchy = 'publish'
#     ordering = ('status', 'publish')

admin.site.register(FORM1)

# @admin.register(FORM1)
# class FORM1Admin(admin.ModelAdmin):
#     list_display = ('r01', 'r01_organ', 'r02', 'r51', 'r03')
