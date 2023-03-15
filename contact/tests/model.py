from django.test import TestCase
from contact.models import ContactDetails


class TestAppModels(TestCase):

    def test_model_str(self):
        title = ContactDetails.objects.create(title='Django Testing')
        self.assertEqual(str(title), "Django Testing")
