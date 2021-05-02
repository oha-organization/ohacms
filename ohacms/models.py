from django.db import models


class Post(models.Model):
    """A model of a post."""
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    status = models.CharField(choices=(
            ('y', "Yayinda"),
            ('t', "Taslak"),
        ),
        max_length=1
    )
    post_type = models.CharField(max_length=10)
    order = models.IntegerField()
    parent_id = models.ForeignKey("Post", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
