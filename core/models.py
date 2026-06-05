
from django.db import models
class ContactSubmission(models.Model):
    full_name=models.CharField(max_length=200)
    company=models.CharField(max_length=200,blank=True)
    email=models.EmailField()
    phone=models.CharField(max_length=50,blank=True)
    project_details=models.TextField()
    budget=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-created_at']
