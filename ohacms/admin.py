from django.contrib import admin
from .models import Post
from .models import Option


admin.site.register(Post)
admin.site.register(Option)