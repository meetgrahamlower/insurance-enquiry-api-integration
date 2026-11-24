
import requests


def submit_enquiry(customer):
    """Send a customer enquiry to the demonstration API."""

    url = "https://httpbin.org/post"

    try:
        response = requests.post(
            url,
            json=customer,
            timeout=10
        )

        response.raise_for_status()

        return {
            "success": True,
            "status_code": response.status_code,
            "data": response.json()
        }

    except requests.exceptions.RequestException as error:
        return {
            "success": False,
            "error": str(error)
        }
