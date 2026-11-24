import unittest

from customer import validate_customer


class TestCustomerValidation(unittest.TestCase):

    def setUp(self):
        self.customer = {
            "name": "John Smith",
            "email": "john@example.com",
            "telephone": "07123456789",
            "enquiry_type": "Motor Insurance"
        }

    def test_valid_customer(self):
        valid, message = validate_customer(self.customer)
        self.assertTrue(valid)

    def test_missing_email(self):
        del self.customer["email"]
        valid, message = validate_customer(self.customer)
        self.assertFalse(valid)

    def test_invalid_email(self):
        self.customer["email"] = "johnexample.com"
        valid, message = validate_customer(self.customer)
        self.assertFalse(valid)

    def test_invalid_telephone(self):
        self.customer["telephone"] = "123"
        valid, message = validate_customer(self.customer)
        self.assertFalse(valid)

    def test_empty_name(self):
        self.customer["name"] = ""
        valid, message = validate_customer(self.customer)
        self.assertFalse(valid)


if __name__ == "__main__":
    unittest.main(verbosity=2)