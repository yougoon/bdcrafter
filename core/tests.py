from django.test import TestCase, Client
from django.urls import reverse
from .models import ProjectRequest, Subscriber, ContactMessage, Service, Project

class CoreViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a test service and project
        self.service = Service.objects.create(title="Test Service", description="Test Service Description", icon_class="fas fa-test", order=1)
        self.project = Project.objects.create(title="Test Project", category="Test Category", description="Test Project Description", technologies="Python, Django", is_featured=True, order=1)

    def test_index_get(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Service")
        self.assertContains(response, "Test Project")

    def test_project_detail_get(self):
        response = self.client.get(reverse('core:project_detail', args=[self.project.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Project")
        self.assertContains(response, "Test Project Description")

    def test_all_projects_get(self):
        response = self.client.get(reverse('core:all_projects'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Project")

    def test_project_request_submit(self):
        form_data = {
            'project_submit': '1',
            'full_name': 'Test User',
            'company_org': 'Test Org',
            'phone_number': '1234567',
            'email': 'test@example.com',
            'project_description': 'Need a beautiful landing page.',
            'budget': 'standard'
        }
        response = self.client.post(reverse('core:home'), data=form_data)
        # Should redirect back to home
        self.assertEqual(response.status_code, 302)
        # Check if project request is saved
        self.assertEqual(ProjectRequest.objects.count(), 1)
        req = ProjectRequest.objects.first()
        self.assertEqual(req.full_name, 'Test User')
        self.assertEqual(req.budget, 'standard')

    def test_newsletter_submit(self):
        form_data = {
            'newsletter_submit': '1',
            'email': 'subscriber@example.com'
        }
        response = self.client.post(reverse('core:home'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Subscriber.objects.count(), 1)
        sub = Subscriber.objects.first()
        self.assertEqual(sub.email, 'subscriber@example.com')

    def test_contact_submit(self):
        form_data = {
            'contact_submit': '1',
            'name': 'Contact Name',
            'email': 'contact@example.com',
            'subject': 'Inquiry',
            'message': 'This is a message.'
        }
        response = self.client.post(reverse('core:home'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ContactMessage.objects.count(), 1)
        msg = ContactMessage.objects.first()
        self.assertEqual(msg.name, 'Contact Name')
        self.assertEqual(msg.subject, 'Inquiry')
