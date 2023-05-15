# from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User

# Create your tests here.
@pytest.mark.django_db
def test_page_profiles_index():

    User_test = User.objects.create(
                           username= "toto",
                           password = "toto",
                           first_name = "Toto_first_name",
                           last_name = "Toto_last_name",

                           )

    Profile.objects.create(user = User_test,
                           favorite_city = "Paris")
    client = Client()
    uri = reverse('profiles_index')
    response = client.get(uri)

    print(response.content)

    assert response.status_code == 200
    assert b"<title>Profiles</title>" in response.content 


@pytest.mark.django_db
def test_page_profiles():

    User_test = User.objects.create(
                           username= "toto",
                           password = "toto",
                           first_name = "Toto_first_name",
                           last_name = "Toto_last_name",

                           )

    Profile.objects.create(user = User_test,
                           favorite_city = "Paris")
    
    client = Client()
    uri = reverse('profile', kwargs={'username':"toto"})
    response = client.get(uri)

    print(response.content)

    assert response.status_code == 200
    assert b"<title>toto</title>" in response.content

