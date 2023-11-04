from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
import cloudinary.uploader

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
    image = CloudinaryField('image', default='placeholder')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="paintings")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    likes = models.ManyToManyField(User, related_name='likes',
                                   default=None, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.pk:
            # This is a new instance, process the image
            img = Image.open(self.image)

            img = img.convert('RGB')

            # Resize the image so that the longest side is equal to 1280 pixels
            img.thumbnail((1280, 1280))

            with BytesIO() as tmp_img_io:
                img.save(tmp_img_io, 'JPEG', quality=90)
                tmp_img_io.seek(0)  # Move the cursor to the beginning of the stream

                # Upload the optimized image to Cloudinary
                upload_result = cloudinary.uploader.upload(tmp_img_io)

                # Update the image field with the Cloudinary URL
                self.image = upload_result['url']

        # Continue with the normal save operation
        super(Painting, self).save(*args, **kwargs)


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
