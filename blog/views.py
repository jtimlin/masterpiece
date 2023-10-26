from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Painting, Comment
from .forms import CommentForm, PaintingForm
from cloudinary.exceptions import Error


class PaintingList(generic.ListView):
    model = Painting
    queryset = Painting.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

    # Override get_queryset to limit the number of posts displayed
    def get_queryset(self):
        return self.queryset[:3]


class PaintingDetail(View):

    def get(self, request, slug, *args, **kwargs):
        """
        Retrives the painting and related comments from the database
        """
        painting = get_object_or_404(Painting, slug=slug)
        comments = painting.comments.order_by('created_on')
        liked = False
        if painting.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Generate the URL for the 'painting_detail' view
        detail_url = reverse('painting_detail', kwargs={'slug': painting.slug})

        return render(
            request,
            "painting_detail.html",
            {
                "painting": painting,
                "comments": comments,
                "comment_form": CommentForm(),
                "liked": liked,
                "detail_url": detail_url,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        This method is called when a POST request is made to the view
        via the comment form.
        """
        painting = get_object_or_404(Painting, slug=slug)
        comments = painting.comments.order_by('created_on')
        liked = False
        if painting.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.painting = painting
            comment.save()
            messages.success(self.request, 'Your thoughts successfully added.')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "painting_detail.html",
            {
                "painting": painting,
                "comments": comments,
                "comment_form": CommentForm(),
                "liked": liked,
            },
        )


class AddPainting(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = PaintingForm
    template_name = 'add_painting.html'
    success_message = "%(calculated_field)s was created successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        try:
            # Attempt to save the form
            return super().form_valid(form)
        except Error as e:
            # Handle the exception and provide a custom error message
            form.add_error('image', 'Invalid image file. Please upload a valid image file.')
            return self.form_invalid(form)

    def get_success_url(self):
        """
        Redirect to the detail page of the newly added painting.
        """
        return reverse('painting_detail', args=[self.object.slug])

    def get_success_message(self, cleaned_data):
        """
        This function overrides the get_success_message() method to add
        the painting title into the success message.
        source: https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )


class LikePainting(LoginRequiredMixin, View):
    """
    This view allows a logged in user to bookmark paintings.
    """

    def post(self, request, slug, *args, **kwargs):
        """
        Checks if user id already exists in the favourites
        field in the Painting database.
        If they exist then remove them from the database.
        If they don't exist then add them to the database.
        """
        painting = get_object_or_404(Painting, slug=slug)
        if painting.likes.filter(id=request.user.id).exists():
            painting.likes.remove(request.user)
            messages.success(self.request, 'Painting removed from your favorites.')
        else:
            painting.likes.add(request.user)
            messages.success(self.request, 'Painting added to my favorites.')
        return HttpResponseRedirect(reverse('painting_detail', args=[slug]))


class MyPaintings(LoginRequiredMixin, generic.ListView):
    """
    This view is used to display a list of paintings uploaded by the logged in
    user.
    """
    model = Painting
    template_name = 'my_paintings.html'
    paginate_by = 8

    def get_queryset(self):
        """
        Override get_queryset to filter by user
        """
        return Painting.objects.filter(author=self.request.user)


class UpdatePainting(LoginRequiredMixin, UserPassesTestMixin,
                   SuccessMessageMixin, generic.UpdateView):
    """
    This view is used to allow logged in users to edit their own paintings
    """
    model = Painting
    form_class = PaintingForm
    template_name = 'update_painting.html'
    success_message = "%(calculated_field)s was updated successfully"

    def get_success_url(self):
        # Use reverse to dynamically generate the URL based on your URL pattern
        return reverse('painting_detail', args=[self.object.slug])

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        The signed-in user is set as the author of the painting.
        """
        form.instance.author = self.request.user

        # Check if a new image was provided
        if 'image' not in form.changed_data:
            # No new image provided, clear the image field error (if any)
            form._errors.pop('image', None)

        return super().form_valid(form)

    def test_func(self):
        """
        Prevent another user from updating someone else's painting
        """
        painting = self.get_object()
        return painting.author == self.request.user

    def get_success_message(self, cleaned_data):
        """
        Override the get_success_message() method to add the painting title
        into the success message.
        source: https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )



class DeletePainting(LoginRequiredMixin, UserPassesTestMixin,
                   generic.DeleteView):
    """
    This view is used to allow logged in users to delete their own painting
    """
    model = Painting
    template_name = 'delete_painting.html'
    success_message = "Painting deleted successfully."
    success_url = reverse_lazy('my_paintings')

    def test_func(self):
        """
        Prevent another user from deleting someone else's painting
        """
        painting = self.get_object()
        return painting.author == self.request.user

    def delete(self, request, *args, **kwargs):
        """
        This function is used to display success message given
        SuccessMessageMixin cannot be used in generic.DeleteView.
        Credit: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        messages.success(self.request, self.success_message)
        return super(DeletePainting, self).delete(request, *args, **kwargs)


class MyLikes(LoginRequiredMixin, generic.ListView):
    """
    This view allows a logged in user to view their favorite paintings.
    """
    model = Painting
    template_name = 'my_likes.html'
    paginate_by = 8

    def get_queryset(self):
        """
        Override get_queryset to filter by user likes
        """
        return Painting.objects.filter(likes=self.request.user.id)


class UpdateComment(LoginRequiredMixin, UserPassesTestMixin,
                    SuccessMessageMixin, generic.UpdateView):
    """
    This view is used to allow logged in users to update their own comments
    """
    model = Comment
    form_class = CommentForm
    template_name = 'update_comment.html'
    success_message = "Comment updated successfully!"

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        The signed in user is set as the author of the comment.
        """
        form.instance.name = self.request.user.username
        return super().form_valid(form)

    def test_func(self):
        """
        Prevent another user from updating someone else's comment
        """
        comment = self.get_object()
        return comment.name == self.request.user.username

    def get_success_url(self):
        """
        Return to pointing detail view when comment updated successfully
        """
        painting = self.object.painting
        return reverse_lazy('painting_detail', kwargs={'slug': painting.slug})


class DeleteComment(LoginRequiredMixin, UserPassesTestMixin,
                    generic.DeleteView):
    """
    This view is used to allow logged in users to delete their own comments
    """
    model = Comment
    template_name = 'delete_comment.html'
    success_message = "Comment deleted successfully"

    def test_func(self):
        """
        Prevent another user from deleting someone else's comment
        """
        comment = self.get_object()
        return comment.name == self.request.user.username

    def delete(self, request, *args, **kwargs):
        """
        This function is used to display success message given
        SuccessMessageMixin cannot be used in generic.DeleteView.
        Credit: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        messages.success(self.request, self.success_message)
        return super(DeleteComment, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        """
        Return to painting detail view when comment deleted successfully
        """
        painting = self.object.painting
        return reverse_lazy('painting_detail', kwargs={'slug': painting.slug})
