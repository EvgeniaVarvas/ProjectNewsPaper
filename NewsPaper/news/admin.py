from django.contrib import admin
from .models import Author, Category, Post, Comment
# from django.contrib.flatpages.admin import FlatPageAdmin
# from django.contrib.flatpages.models import FlatPage
# from django.utils.translation import gettext_lazy as _

# Зарегистрируйте свои модели здесь.


# # Define a new FlatPageAdmin
# class FlatPageAdmin(FlatPageAdmin):
#     fieldsets = (
#         (None, {'fields': ('url', 'title', 'content', 'sites')}),
#         (_('Advanced options'), {
#             'classes': ('collapse',),
#             'fields': (
#                 'enable_comments',
#                 'registration_required',
#                 'template_name',
#             ),
#         }),
#     )
 
 
# # Re-register FlatPageAdmin
# admin.site.unregister(FlatPage)
# admin.site.register(FlatPage, FlatPageAdmin)

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)

 