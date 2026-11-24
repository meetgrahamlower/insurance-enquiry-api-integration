import re


def validate_customer(customer):
    """Check that customer enquiry information is complete and valid."""

    required_fields = ["name", "email", "telephone", "enquiry_type"]

    # Check required fields
    for field in required_fields:
        if not isinstance(customer.get(field), str) or not customer[field].strip():
            return False, f"Missing required information: {field}"

    # Check email address format
    email = customer["email"].strip()

    email_pattern = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

    if not re.match(email_pattern, email):
        return False, "Invalid email address."

    # Check telephone number
    telephone = customer["telephone"]

    digits = re.sub(r"\D", "", telephone)

    if len(digits) < 10 or len(digits) > 15:
        return False, "Invalid telephone number."

    return True, "Customer information is valid."