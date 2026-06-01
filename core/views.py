from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ProjectRequestForm, NewsletterForm, ContactForm
from .models import Service, Project, ProjectRequest
from django.core.paginator import Paginator

def index(request):
    form = ProjectRequestForm()
    newsletter_form = NewsletterForm()
    contact_form = ContactForm()
    
    # Handle forms submission
    if request.method == 'POST':
        if 'project_submit' in request.POST:
            form = ProjectRequestForm(request.POST)
            if form.is_valid():
                project_request = form.save()
                
                # Send email notification to admin
                send_mail(
                    f'New Project Request from {project_request.full_name}',
                    f"""
                    New project request received!
                    
                    Name: {project_request.full_name}
                    Company: {project_request.company_org or 'N/A'}
                    Email: {project_request.email}
                    Phone: {project_request.phone_number}
                    Budget: {project_request.get_budget_display()}
                    
                    Project Description:
                    {project_request.project_description}
                    
                    Please login to admin panel to view full details.
                    """,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.EMAIL_HOST_USER] if settings.EMAIL_HOST_USER else [],
                    fail_silently=True,
                )
                
                messages.success(request, 'Thank you! We will contact you within 24 hours.')
                return redirect('core:home')
            else:
                messages.error(request, 'Please correct the errors below.')
        
        elif 'newsletter_submit' in request.POST:
            newsletter_form = NewsletterForm(request.POST)
            if newsletter_form.is_valid():
                newsletter_form.save()
                messages.success(request, 'Successfully subscribed to newsletter!')
                return redirect('core:home')
            else:
                messages.error(request, 'Failed to subscribe. Please try again.')
        
        elif 'contact_submit' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, 'Your message has been sent. We will get back to you soon!')
                return redirect('core:home')
            else:
                messages.error(request, 'Failed to send your contact message. Please fix the errors.')
    
    # Get data for the page
    services = Service.objects.all()
    projects = Project.objects.all()[:6]  # Show latest 6 projects
    stats = {
        'projects': ProjectRequest.objects.count(),
        'clients': ProjectRequest.objects.values('email').distinct().count(),
        'experience': 5,
        'support': '24/7'
    }
    
    context = {
        'form': form,
        'newsletter_form': newsletter_form,
        'contact_form': contact_form,
        'services': services,
        'projects': projects,
        'stats': stats,
    }
    
    return render(request, 'index.html', context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})

def all_projects(request):
    projects_list = Project.objects.all()
    paginator = Paginator(projects_list, 9)
    page = request.GET.get('page')
    projects = paginator.get_page(page)
    return render(request, 'projects.html', {'projects': projects})
