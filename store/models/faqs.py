from django.db import models
class Faqs(models.Model):
    question=models.TextField( default='' , null=True , blank=True)
    answer=models.TextField( default='' , null=True , blank=True)
    
    def __str__(self):
        return self.question