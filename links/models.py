from django.db import models
from django.conf import settings

# Create your models here.
class Link(models.Model):
    name = models.TextField()
    description = models.TextField()
    image = models.URLField()
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    link = models.ForeignKey('links.Link', related_name='votes', on_delete=models.CASCADE)