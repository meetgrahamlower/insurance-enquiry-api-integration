
import requests

url = "https://httpbin.org/post"

# Information we want to send
customer = {
    "name": "John Smith",
    "email": "john@example.com",
    "telephone": "07123456789",
    "enquiry_type": "Motor Insurance"
}

try:
    response = requests.post(url, json=customer, timeout=10)

    response.raise_for_status()

    result = response.json()

    print("Status code:", response.status_code)
    print("Request successful!")
    print("Customer information received by API:")
    print(result["json"])

except requests.exceptions.RequestException as error:
    print("API request failed:")
    print(error)
