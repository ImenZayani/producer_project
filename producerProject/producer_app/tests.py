from django.test import TestCase
from .models import Message
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


class MessageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Message.objects.create(text='Test message')

    def test_message_content(self):
        message = Message.objects.get(id=1)
        expected_object_name = f'{message.text}'
        self.assertEquals(expected_object_name, 'Test message')
        
class WebhookReceiverTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.message_data = {'text': 'Test message'}
        self.list_url = '/api/webhook/'
