#coding=utf-8
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from localization.models import *
from profiles.models import *
from cms.models import Presentation


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class NewProfileTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.country = Country(name='Venezuela')
        self.country.save()
        self.state = State(name='Dtto Capital', country=self.country)
        self.state.save()

    def test__new_user(self):
        post_data = {
            'first_name': 'Israel',
            'last_name': 'Fermin',
            'email': 'test2@zava.com.ve',
            'password': '1234',
            'confirm_password': '1234',
            'country': self.country.id,
            'state': self.state.id,
            'about': 'A Python GEEK'
        }
        self.assertEquals(User.objects.count(), 0)
        self.assertEquals(UserProfile.objects.count(), 0)

        response = self.client.post(reverse('create-profile'), post_data)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.count(), 1)
        self.assertEquals(UserProfile.objects.count(), 1)

    def test__speaker_registration(self):
        post_data = {
            'first_name': 'Israel',
            'last_name': 'Fermin',
            'email': 'test2@zava.com.ve',
            'password': '1234',
            'confirm_password': '1234',
            'country': self.country.id,
            'state': self.state.id,
            'about': 'A Python GEEK',
            'presentation_name': 'SETH, a semantic scripting tool',
            'presentation_description': 'Using SETH to do some semantinc Scripting',
            'presentation_requirements': 'Videobeam, pantalla, SETH instalado, iPython y ganas de aprender',
            'presentation_tutotial': False,
            'presentation_duration': 120,
        }
        self.assertEquals(Presentation.objects.count(), 0)
        self.assertEquals(User.objects.count(), 0)
        self.assertEquals(UserProfile.objects.count(), 0)

        response = self.client.post(reverse('speaker-registration'), post_data)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Presentation.objects.count(), 1)
        self.assertEquals(User.objects.count(), 1)
        self.assertEquals(UserProfile.objects.count(), 1)
