from django.contrib import admin
from .models import *


admin.site.register(SPR_F10R1)
admin.site.register(SPR_F10R1_ORGAN)
admin.site.register(SPR_F10R2)
admin.site.register(SPR_F10R3)
admin.site.register(SPR_F10R3_GASORG)
admin.site.register(SPR_F10R7_1)
admin.site.register(SPR_F10R8)
admin.site.register(SPR_F10R9)
admin.site.register(SPR_F10R9_1)
admin.site.register(SPR_F10R10)
admin.site.register(SPR_F10R10_1)
admin.site.register(SPR_F10R10_2)
admin.site.register(SPR_F10R11)
admin.site.register(SPR_F10R13)
admin.site.register(SPR_F10R15)
admin.site.register(SPR_F10R16)
admin.site.register(SPR_F10R17)
admin.site.register(SPR_F10R18)
admin.site.register(SPR_F10R19_1)
admin.site.register(SPR_F10R19_2)
admin.site.register(SPR_F10R19_3)


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
