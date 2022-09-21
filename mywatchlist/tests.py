from lib2to3.pgen2.literals import simple_escapes
from django.test import TestCase, Client
# Create your tests here.
class MyWatchlistTest(TestCase):
    def test_xml(self):
        response = Client().get("/mywatchlist/xml/")
        self.assertEqual(response.status_code, 200)
    
    def test_json(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
    
    def test_html(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)