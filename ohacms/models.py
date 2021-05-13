from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class Post(models.Model):
    """A model of a post."""
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = RichTextField()
    status = models.CharField(choices=(
            ('y', "Yayinda"),
            ('t', "Taslak"),
        ),
        max_length=1
    )
    post_type = models.CharField(max_length=10)
    order = models.IntegerField()
    parent = models.ForeignKey("Post", on_delete=models.SET_NULL, null=True, blank=True)

    def get_absolute_url(self):
        """Returns the url to access a particular post instance."""
        return reverse('post-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Option(models.Model):
    """A model of options """
    name = models.CharField(max_length=200)
    description = models.TextField()
    content = RichTextField()

    def __str__(self):
        return self.name
