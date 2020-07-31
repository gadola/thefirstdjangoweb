from django.test import TestCase, SimpleTestCase

# Create your tests here.
class Simpletest(SimpleTestCase):
    def testHomePageStatus(self):
        response = self.client.get('/home/')
        self.assertEquals(response.status_code,200)