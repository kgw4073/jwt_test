from django.db import models
from authentication.models import User


class SellingPostManager(models.Manager):
    def create_post(self, seller, title, content):
        if seller is None:
            raise TypeError('seller must have a seller.')

        if title is None:
            raise TypeError('title must have a title.')

        selling_post = SellingPost(seller=seller, title=title, content=content)
        selling_post.save()

        return selling_post

class SellingPost(models.Model):
    #auto_increment_id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    content = models.TextField()

    objects = SellingPostManager()


    def __str__(self):
        return self.title