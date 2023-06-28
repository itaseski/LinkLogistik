from django.contrib import admin

from .models import Document, Part

class PartInline(admin.StackedInline):
    model = Part
    extra = 3

class DocumentAdmin(admin.ModelAdmin):
    fields = ["number", "title"]
    list_display = ["number", "title"]
    inlines = [PartInline]


admin.site.register(Document, DocumentAdmin)

admin.site.register(Part)
