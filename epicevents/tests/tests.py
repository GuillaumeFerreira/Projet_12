from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed



def test_url():
    client = Client()
    response = client.get("client.html")
    assert response.status_code == 404