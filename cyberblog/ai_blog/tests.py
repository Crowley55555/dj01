"""
Tests for the ai_blog application.
"""
from django.test import TestCase
from django.urls import reverse


class ViewTests(TestCase):
    def test_data_page(self):
        """
        Test that data page returns correct response and template.
        """
        response = self.client.get(reverse('ai_blog:data'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ai_blog/data.html')
        self.assertContains(response, 'Data Science in AI')
