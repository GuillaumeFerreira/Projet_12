from django.test import Client
from django.urls import reverse, resolve
import pytest
from pytest_django.asserts import assertTemplateUsed


def test_admin():
    # client = Client()
    # response = client.get("login/", data={"username": "ferreira","password":"Guillaume46"})
    path = reverse("token_obtain_pair")
    assert path == "/login/"
    assert resolve(path).view_name == "token_obtain_pair"
