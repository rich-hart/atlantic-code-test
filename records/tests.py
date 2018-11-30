import os
from django.conf import settings

from django.test import TestCase
from rest_framework.test import APIClient

class TestDocument(TestCase):
    def test_upload(self):
        #import ipdb; ipdb.set_trace()
        client = APIClient()
        with open(os.path.join(settings.BASE_DIR, 'records','test_data.tsv')) as fp:
            response = client.post('/documents/', {'upload': fp})
        self.assertEqual(response.status_code, 201)


