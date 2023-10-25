"""Forms for Comments and Paintings"""

from django import forms
from django_summernote.widgets import SummernoteWidget
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from .models import Comment, Painting


class CommentForm(forms.ModelForm):
    """
    Create Comment Form
    """

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget = forms.Textarea(attrs={'rows': 3})

    class Meta:
        """
        Get comment model, choose fields to display
        """
        model = Comment
        fields = ('body',)


class PaintingForm(forms.ModelForm):
    """
    Add Painting Form
    """

    def __init__(self, *args, **kwargs):
        super(PaintingForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget = forms.Textarea(attrs={'rows': 3})

    class Meta:
        """
        Get painting model and choose fields to display
        """
        model = Painting
        fields = [
            'image',
            'title',
            'category',
            'description',
        ]

        # Make the 'image' field required
        widgets = {
            'image': forms.FileInput(attrs={'required': 'required'}),
        }

    def save(self, commit=True):
        painting = super(PaintingForm, self).save(commit=False)
        painting.title = self.cleaned_data['title']

        # Generate a slug from the title
        painting.slug = slugify(painting.title)

        if commit:
            painting.save()

        return painting
    
    def clean_image(self):
        image = self.cleaned_data['image']
        if image:
            # Get the file extension
            file_extension = image.name.split('.')[-1].lower()
            # Validate that the file is an image
            valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
            if file_extension not in valid_extensions:
                raise forms.ValidationError("Only 'jpg', 'jpeg', 'png', 'gif' files accepted.")
        return image
