from django.db import models
from datetime import datetime
class Contact(models.Model):
    name = models.CharField(max_length=50)
    whatsapp_number = models.CharField(max_length=50) 
    subject=models.TextField( default='' , null=True , blank=True)
    message=models.TextField( default='' , null=True , blank=True)
    date_time = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.subject