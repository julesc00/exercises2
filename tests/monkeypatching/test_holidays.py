import pytest

import unittest
from http import HTTPStatus
from requests.exceptions import Timeout
from unittest.mock import Mock

from monkeypatching.holidays import get_holidays

requests = Mock()
URL = "http://localhost/api/holidays"

def test_get_holidays2(monkeypatch):
    # Define a mock response JSON
    mock_json_response = [{"name": "New Year", "date": "2023-01-01"}]

    # Define a mock response object
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    # Define a mock get function that returns the mock response
    def mock_get(*args, **kwargs):
        return MockResponse(mock_json_response, HTTPStatus.OK)
    mock_get_holidays = Mock()
    # Patch the requests.get method with the mock_get function
    monkeypatch.setattr(requests, "get", mock_get)

    # Call the function being tested
    result = get_holidays()
    breakpoint()
    # Assert that the result matches the mock response
    assert result == mock_json_response
    assert requests.get.call_count == 2


def test_get_holidays3():
    # Create a mock response object
    mock_response = Mock()

    # Set status code and json data for the mock response
    mock_response.status_code = HTTPStatus.OK
    mock_response.json.return_value = [{"name": "Christmas", "date": "2023-12-25"}]

    # Mock the requests.get method to return the mock response
    requests.get = Mock(return_value=mock_response)

    # Call the function being tested
    result = get_holidays()
    breakpoint()
    # Assert that requests.get is called with the correct URL
    requests.get.assert_called_once_with(URL)

    # Assert that the result matches the mock response JSON data
    assert result == [{"name": "Christmas", "date": "2023-12-25"}]


def test_get_holidays_failure(monkeypatch):
    # Define a mock response with status code other than OK
    class MockResponse:
        def __init__(self, status_code):
            self.status_code = status_code

    # Define a mock get function that returns the mock response
    def mock_get(*args, **kwargs):
        return MockResponse(HTTPStatus.INTERNAL_SERVER_ERROR)

    requests.get.side_effect = [Timeout, HTTPStatus.INTERNAL_SERVER_ERROR]
    # Patch the requests.get method with the mock_get function
    monkeypatch.setattr(requests, "get", mock_get)

    # Call the function being tested
    result = get_holidays()

    # Assert that the result is None when status code is not OK
    assert result is None
    assert requests.get.call_count == 2
