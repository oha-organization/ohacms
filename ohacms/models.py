from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.template.defaultfilters import slugify

class Post(models.Model):
    """A model of a post."""
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    slug = models.SlugField(default='', max_length=200, blank=True)
    description = models.TextField()
    content = RichTextField()
    status = models.CharField(choices=(
            ('y', "Yayinda"),
            ('t', "Taslak"),
        ),
        max_length=1
    )
    post_type =  models.CharField(choices=(
            ('s', "Sayfa"), 
            ('d', "Duyuru"),
            ('h', "Haber"),
        ),
        max_length=10
    )
    order = models.IntegerField()
    parent = models.ForeignKey("Post", on_delete=models.SET_NULL, null=True, blank=True)

    def get_absolute_url(self):
        """Returns the url to access a particular post instance."""
        return reverse('post-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


    def __str__(self):
        return self.name


class Option(models.Model):
    """A model of options """
    name = models.CharField(max_length=200)
    description = models.TextField()
    content = RichTextField()

    def __str__(self):
        return self.name
