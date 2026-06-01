import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bdcrafter.settings')
django.setup()

from core.models import Service, Project

# Create Services
Service.objects.get_or_create(title='Custom Web Apps', defaults={'description': 'Tailored Python/Django applications built for performance, scale, and longevity.', 'icon_class': 'fas fa-code', 'order': 1})
Service.objects.get_or_create(title='Medical Portfolios', defaults={'description': 'Clean, professional, trust-building portfolio websites designed specifically for medical practitioners.', 'icon_class': 'fas fa-user-md', 'order': 2})
Service.objects.get_or_create(title='Landing Pages', defaults={'description': 'High-converting landing pages featuring flawless mobile responsiveness and modern CSS design.', 'icon_class': 'fas fa-rocket', 'order': 3})

# Create Projects
Project.objects.get_or_create(title="Dr. Sarah's Portfolio", defaults={'category': 'Medical Portfolio', 'description': 'A custom portfolio built for a leading cardiologist to manage patient appointments and showcase medical publications.', 'technologies': 'Django, Tailwind CSS, SQLite', 'project_url': 'https://example.com/sarah', 'is_featured': True, 'order': 1})
Project.objects.get_or_create(title='UrbanCart Commerce', defaults={'category': 'E-Commerce', 'description': 'A full-featured e-commerce platform with stripe integration, dashboard analytics, and custom inventory management.', 'technologies': 'Next.js, Python, PostgreSQL', 'project_url': 'https://example.com/urbancart', 'is_featured': True, 'order': 2})
Project.objects.get_or_create(title='Fintech Dashboard', defaults={'category': 'Web Application', 'description': 'A modern SaaS analytics platform featuring real-time charting, user management, and transactional reports.', 'technologies': 'React, Django, MySQL', 'project_url': 'https://example.com/fintech', 'is_featured': True, 'order': 3})

print('Seed data created successfully')
