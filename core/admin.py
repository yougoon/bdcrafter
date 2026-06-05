
from django.contrib import admin
from .models import ContactSubmission
@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display=('full_name','email','company','budget','created_at')
    search_fields=('full_name','email','company')
    list_filter=('budget','created_at')
