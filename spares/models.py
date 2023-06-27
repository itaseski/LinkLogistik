from django.db import models


class Document(models.Model):
    '''
    Display document title
    '''
    number = models.CharField(max_length=10)
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return self.title


class Part(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    pos = models.IntegerField(blank=True)
    references = models.TextField(blank=True)
    part_no = models.CharField(max_length=7)
    qty = models.CharField(max_length=2) # to accept `rq`
    replacement =models.CharField('Replacement part no.', blank=True, max_length=7)
    designation = models.CharField(max_length=256)
    additional_information = models.CharField(blank=True,max_length=64)
    note = models.CharField(blank=True, max_length=32)
    included = models.BooleanField('Is in package?', default=False)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.part_no
