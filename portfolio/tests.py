import json
from django.test import TestCase, Client
from django.urls import reverse
from portfolio.models import Skill, Project, ContactMessage

class PortfolioTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Seed test database with a skill and project
        self.skill = Skill.objects.create(
            name="Python",
            category="languages",
            proficiency=95,
            icon_class="devicon-python-plain"
        )
        self.project = Project.objects.create(
            title="AI Healthcare Assistant",
            description="Short description",
            detailed_description="Long description",
            tech_stack="Python, Django",
            key_features="Feature 1\nFeature 2",
            is_featured=True
        )

    def test_home_view_status_code(self):
        """Verify home page loads correctly and includes seeded data."""
        response = self.client.get(reverse('portfolio:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/index.html')
        self.assertContains(response, "Deepanshu Chauhan")
        self.assertContains(response, "AI Healthcare Assistant")

    def test_contact_form_submission_success(self):
        """Verify successful AJAX POST to contact form saves data."""
        contact_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Inquiry',
            'message': 'Hello, I want to hire you!'
        }
        response = self.client.post(
            reverse('portfolio:contact_api'),
            data=json.dumps(contact_data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertEqual(response_json['status'], 'success')
        self.assertTrue(ContactMessage.objects.filter(email='test@example.com').exists())

    def test_contact_form_submission_failure(self):
        """Verify validation errors for incomplete submissions."""
        contact_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            # Missing subject and message
        }
        response = self.client.post(
            reverse('portfolio:contact_api'),
            data=json.dumps(contact_data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 400)
        response_json = response.json()
        self.assertEqual(response_json['status'], 'error')

    def test_ai_assistant_offline_fallback(self):
        """Verify the AI Assistant responds successfully with the keyword fallback classifier."""
        query_data = {'message': 'What projects has Deepanshu built?'}
        response = self.client.post(
            reverse('portfolio:ai_assistant_api'),
            data=json.dumps(query_data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertEqual(response_json['status'], 'success')
        # Check that it matched the 'project' keyword fallback
        self.assertIn("AI Healthcare Assistant", response_json['response'])
