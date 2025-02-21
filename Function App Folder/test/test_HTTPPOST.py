
import pytest
from azure.functions import HttpRequest
from FunctionCloudChallenge import main  # Update 'my_function' to the folder name of your function

def test_post_method():
    # Create a mock HTTP POST request
    req = HttpRequest(
        method='POST',
        body=b'{"name": "Marta"}',
        url='http://localhost:7071/api/http_trigger1',
        headers={'Content-Type': 'application/json'}
    )

    # Call your Azure Function's main method
    response = main(req)

    # Assert the response
    assert response.status_code == 200
    assert response.get_body().decode() == 'Hello, Marta. This HTTP triggered function executed successfully.'

#response = requests.post(url, json=data)

#if response.status_code == 200:  # Check for HTTP 200 OK
    #print("Request passed!")
    #print("Response Body:", response.text)
#else:
    #print(f"Request failed with status code: {response.status_code}")
    #print("Error Response Body:", response.text)