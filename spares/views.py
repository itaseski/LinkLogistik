from django.views import generic

from .models import Document


class IndexView(generic.ListView):
    template_name = "spares/index.html"
    context_object_name = "document_list"

    def get_queryset(self):
        """Return documents."""
        return Document.objects.order_by("number")


class DetailView(generic.DetailView):
    model = Document
    template_name = "spares/detail.html"

