from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Painting, Comment
from .forms import CommentForm


class PaintingList(generic.ListView):
    model = Painting
    queryset = Painting.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

    # Override get_queryset to limit the number of posts displayed
    def get_queryset(self):
        return self.queryset[:3]


class PaintingDetail(View):

    def get(self, request, slug):
        """
        Retrives the painting and related comments from the database
        """
        painting = get_object_or_404(Painting, slug=slug)
        comments = painting.comments.order_by('created_on')
        liked = False
        if painting.likes.filter(id=self.request.user.id).exists():
            liked = True

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

    def post(self, request, slug):
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
            messages.success(self.request, 'Comment successfully added')
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