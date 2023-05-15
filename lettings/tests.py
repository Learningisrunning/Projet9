# from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse
from lettings.models import Letting
from lettings.models import Address

# Create your tests here.
@pytest.mark.django_db
def test_page_lettings_index():

    Address_test = Address.objects.create(
                           number= 30,
                           street = "streeet",
                           city= "Portland",
                           state = "Oregon",
                           zip_code = 92290,
                           country_iso_code = 920)

    Letting.objects.create(title = "test_letting",
                           address = Address_test)
    client = Client()
    uri = reverse('lettings_index')
    response = client.get(uri)

    assert response.status_code == 200
    assert b"<title>Lettings</title>" in response.content 


@pytest.mark.django_db
def test_page_lettings():

    Address_test = Address.objects.create(
                           number= 30,
                           street = "streeet",
                           city= "Portland",
                           state = "Oregon",
                           zip_code = 92290,
                           country_iso_code = 920)

    Letting.objects.create(title = "test_letting",
                           address = Address_test)
    
    client = Client()
    uri = reverse('letting', kwargs={'letting_id':1})
    response = client.get(uri)

    print(response.content)

    assert response.status_code == 200
    assert b"<title>test_letting</title>" in response.content

