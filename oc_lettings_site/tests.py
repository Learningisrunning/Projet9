from django.test import Client
from django.urls import reverse

def test_page_index():

    client = Client()
    uri = reverse('index')
    response = client.get(uri)

    print(response.content)

    assert response.status_code == 200
    assert b"<title>Holiday Homes</title>" in response.content 


