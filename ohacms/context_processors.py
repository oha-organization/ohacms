from .models import Post
from .models import Option


def posts(request):
    return {
        'posts': Post.objects.all()
    }


def options(request):
    return {
        'options': Option.objects.all()
    }
