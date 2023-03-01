import requests
import json
from assertpy import assert_that
import pytest
from pytest_bdd import scenarios, given, when, then
from Utils.Variables import Api

scenarios('../features/api_check_order.feature')
header = ''
body = ''
@given('Open Connection')
def open_connection():
    header = Api.header
@when('Set params')
def params():
    body = Api.body
@then('Check if the order is registered')
def read_order():
    response = requests.post(Api.url, headers=Api.header, data=Api.body)
    print(response.text)
    assert_that(response.status_code).is_equal_to(200)