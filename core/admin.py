from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils import timezone
from .models import ProjectRequest, Subscriber, ContactMessage, Service, Project

class ProjectRequestAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number', 'budget', 'status', 'created_at']
    list_filter = ['status', 'budget', 'created_at']
    search_fields = ['full_name', 'email', 'phone_number', 'company_org']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('full_name', 'company_org', 'phone_number', 'email')
        }),
        ('Project Details', {
            'fields': ('project_description', 'budget')
        }),
        ('Admin Management', {
            'fields': ('status', 'admin_notes', 'contacted_at', 'contacted_by'),
            'classes': ('wide',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mark_as_contacted', 'mark_as_in_progress', 'mark_as_completed']
    
    def mark_as_contacted(self, request, queryset):
        queryset.update(status='contacted', contacted_at=timezone.now(), contacted_by=request.user.username)
        self.message_user(request, f"{queryset.count()} project(s) marked as contacted.")
    mark_as_contacted.short_description = "Mark selected as contacted"
    
    def mark_as_in_progress(self, request, queryset):
        queryset.update(status='in_progress')
        self.message_user(request, f"{queryset.count()} project(s) marked as in progress.")
    mark_as_in_progress.short_description = "Mark selected as in progress"
    
    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
        self.message_user(request, f"{queryset.count()} project(s) marked as completed.")
    mark_as_completed.short_description = "Mark selected as completed"

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at', 'is_active']
    list_filter = ['is_active', 'subscribed_at']
    search_fields = ['email']
    actions = ['activate_subscribers', 'deactivate_subscribers']
    
    def activate_subscribers(self, request, queryset):
        queryset.update(is_active=True)
    activate_subscribers.short_description = "Activate selected subscribers"
    
    def deactivate_subscribers(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_subscribers.short_description = "Deactivate selected subscribers"

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    
    actions = ['mark_as_read']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected as read"

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'icon_class']
    list_editable = ['order']
    search_fields = ['title']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_featured', 'order', 'image_preview']
    list_editable = ['order', 'is_featured']
    list_filter = ['category', 'is_featured']
    search_fields = ['title', 'description']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 8px;"/>', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Preview'

# Register models
admin.site.register(ProjectRequest, ProjectRequestAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Project, ProjectAdmin)

# Customize admin site
admin.site.site_header = "BD Crafter Admin Panel"
admin.site.site_title = "BD Crafter Admin"
admin.site.index_title = "Welcome to BD Crafter Dashboard"
