
import json

from customer import validate_customer
from api_client import submit_enquiry


# Example customer enquiry
customer = {
    "name": "John Smith",
    "email": "john@example.com",
    "telephone": "07123456789",
    "enquiry_type": "Motor Insurance"
}


# Step 1: Validate the customer information
valid, message = validate_customer(customer)

print("Validation:", message)


# Step 2: Submit the enquiry if the information is valid
if valid:

    result = submit_enquiry(customer)

    if result["success"]:
        print("\nEnquiry submitted successfully!")
        print("HTTP status:", result["status_code"])

        print("\nCustomer information received by API:")

        returned_data = result["data"]["json"]

        print(json.dumps(returned_data, indent=4))

    else:
        print("\nEnquiry submission failed:")
        print(result["error"])

else:
    print("\nEnquiry was not submitted.")
