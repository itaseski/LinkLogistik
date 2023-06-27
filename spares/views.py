from django.shortcuts import get_object_or_404, render

from .models import Document


def index(request):
    document_list = Document.objects.order_by("number")
    context = {
        "document_list": document_list,
    }
    return render(request, "spares/index.html", context)


def detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    return render(request, "spares/detail.html", {"document": document})

