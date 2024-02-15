from django.test import TestCase
from django.urls import reverse

class SnackBoxTests(TestCase):

    def test_snack_list_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_snack_detail_page_status_code(self):
        # Assuming you have at least one snack object created
        # Replace `1` with a valid snack ID in your database
        url = reverse('snack_detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_detail_page_template(self):
        # Assuming you have at least one snack object created
        # Replace `1` with a valid snack ID in your database
        url = reverse('snack_detail', args=[1])
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')
