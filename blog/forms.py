"""Forms for Comments and Paintings"""

from django import forms
from django_summernote.widgets import SummernoteWidget
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