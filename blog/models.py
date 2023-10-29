from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    """
    Model for Category
    """
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Painting(models.Model):
    """
    Model for Painting
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = CloudinaryField('image', default='placeholder', transformation='f_auto')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="paintings")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    likes = models.ManyToManyField(
    User, related_name='likes', default=None, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Model for Comment
    """
    painting = models.ForeignKey(
        Painting, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        To display the comments by created_on in ascending order
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
