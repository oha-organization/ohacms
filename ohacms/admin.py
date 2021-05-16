from django.contrib import admin
from .models import Post
from .models import Option

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} # while you were typing title, slug is being typed automatic


admin.site.register(Post,PostAdmin)
admin.site.register(Option)
