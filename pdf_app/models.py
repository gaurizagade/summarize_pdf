from django.db import models

# Create your models here.
from django.db import models

class UploadedPDF(models.Model):
    pdf_file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.pdf_file.name