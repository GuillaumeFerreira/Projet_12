from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed


def test_admin(client):
    response = client.get("/")
    assert response.status_code == 200
