#coding=utf-8
from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.core.urlresolvers import reverse
from cms.models import *

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class PresentationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User(username='TestUser', email='test@testdomain.com')
        self.user.is_active = True
        self.user.set_password('1234')
        self.user.save()
        self.client.login(username=self.user.username, password='1234')


    def test__presentation_add(self):
        self.assertEqual(Presentation.objects.count(), 0)
        post_data = {
            'speakers': [User.objects.get(id=1)],
            'name': 'PyVE: Hacia una comunidad organizada',
            'description': 'Cómo PyVE se ha ido organizando hasta lograr montar el primer PyConVE',
            'tutorial': True,
            'duration': 120,
            'requirements': 'Video Beam, pantalla y ganas de aprender'
        }
        response = self.client.post(reverse('presentation-create'), post_data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(Presentation.objects.count(), 1)

