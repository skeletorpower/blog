from django.contrib import admin

# Register your models here.
from .models import Post #can do like this cuz the folder is same

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated', 'timestamp']
    list_editable = ['title']
    list_display_links = ['updated', 'timestamp']
    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'content']




    class Meta:
        model = Post







admin.site.register(Post, PostModelAdmin)
