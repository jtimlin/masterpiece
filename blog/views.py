from django.shortcuts import render
from django.views import generic, View
from .models import Painting


class PaintingList(generic.ListView):
    model = Painting
    queryset = Painting.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

    # Override get_queryset to limit the number of posts displayed
    def get_queryset(self):
        return self.queryset[:3]
