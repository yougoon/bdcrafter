from django.db import models
from django.utils import timezone

class ProjectRequest(models.Model):
    BUDGET_CHOICES = [
        ('standard', 'Standard ($500-$2000)'),
        ('advance', 'Advance ($2500-$5000)'),
        ('premium', 'Premium ($6000-$10000)'),
        ('custom', 'Custom Quote'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('contacted', 'Contacted'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
    ]
    
    full_name = models.CharField(max_length=200, verbose_name="Full Name")
    company_org = models.CharField(max_length=200, blank=True, null=True, verbose_name="Company/Organization")
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number")
    email = models.EmailField(verbose_name="Email Address")
    project_description = models.TextField(verbose_name="Project Description")
    budget = models.CharField(max_length=50, choices=BUDGET_CHOICES, default='standard', verbose_name="Budget Range")
    
    # Metadata
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending', verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    admin_notes = models.TextField(blank=True, null=True, verbose_name="Admin Notes")
    
    # Contact tracking
    contacted_at = models.DateTimeField(blank=True, null=True)
    contacted_by = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.full_name} - {self.email}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Project Request"
        verbose_name_plural = "Project Requests"

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.email

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    class Meta:
        ordering = ['-created_at']

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=100, help_text="Font Awesome icon class", default="fas fa-code")
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']

class Project(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    technologies = models.CharField(max_length=200, help_text="Comma-separated technologies")
    project_url = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']
