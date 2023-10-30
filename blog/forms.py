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
    def __init__(self, *args, **kwargs):
        super(PaintingForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget = forms.Textarea(attrs={'rows': 3})

        if self.instance.pk:  # Check if the form is in "edit" mode
            self.fields['image'].required = False
            self.fields['image'].widget.attrs.pop('required', None)
        else:
            self.fields['image'].widget.attrs['required'] = 'required'

    class Meta:
        model = Painting
        fields = [
            'image',
            'title',
            'category',
            'description',
        ]

    def save(self, commit=True):
        painting = super(PaintingForm, self).save(commit=False)
        painting.title = self.cleaned_data['title']

        # Generate a slug from the title
        painting.slug = slugify(painting.title)

        if commit:
            painting.save()

        return painting
