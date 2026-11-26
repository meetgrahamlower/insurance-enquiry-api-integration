# Customer Quick Start Guide

## Insurance Enquiry API Integration

### 1. Introduction

This guide is designed to help customers and integration
partners make their first successful API request.

No previous programming experience is required.

By the end of this guide, you will understand how to:

- Make an API request.
- Interpret an API response.
- Use bearer token authentication.
- Submit an insurance enquiry.
- Identify common API errors.

### 2. What is an API?

An Application Programming Interface (API) allows
different software systems to communicate with each other.

For example, an insurance broker could use an API to
transfer customer enquiry information from their website
to an insurance management platform.

This can reduce manual data entry, improve accuracy
and streamline business processes.

### 3. Before You Begin

You will need:

- An internet connection.
- Postman installed on your computer.
- A basic understanding of the information you wish
  to exchange between systems.

Postman is available from:

https://www.postman.com/downloads/

This guide uses httpbin, a public demonstration API.

No real customer information or production API
credentials should be used.

### 4. Make Your First API Request

1. Open Postman.
2. Create a new HTTP request.
3. Select GET as the request method.
4. Enter the following URL:

https://httpbin.org/get

5. Click Send.

#### Expected Result

You should receive an HTTP status code of 200 OK.

This indicates that the server successfully processed
your request.

The response will contain information about your request
in JSON format.

### 5. Understanding JSON

JSON stands for JavaScript Object Notation.

It is a commonly used format for exchanging structured
information between software systems.

Example:

```json
{
    "name": "John Smith",
    "email": "john@example.com",
    "enquiry_type": "Motor Insurance"
}
```

Each piece of information has a name, known as a key,
and an associated value.

### 6. Understanding Authentication

Many APIs require authentication before allowing
access to their services.

Bearer token authentication is one common method.

A bearer token is supplied with the request to
demonstrate that the requesting application has
appropriate credentials.

#### Test Bearer Token Authentication

1. Create a new GET request in Postman.
2. Enter the following URL:

https://httpbin.org/bearer

3. Select the Authorization tab.
4. Select Bearer Token as the authentication type.
5. Enter the following demonstration token:

demo-token-123

6. Click Send.

#### Expected Result

HTTP status: 200 OK

The response should include:

```json
{
    "authenticated": true,
    "token": "demo-token-123"
}
```

This demonstration endpoint checks for a bearer token
but does not validate it against a real user account.

Never share production API tokens or include them
in public repositories.

### 7. Submit an Insurance Enquiry

1. Create a new HTTP request.
2. Select POST as the request method.
3. Enter the following URL:

https://httpbin.org/post

4. Select the Body tab.
5. Select raw.
6. Select JSON as the data format.
7. Enter the following demonstration customer data:

```json
{
    "name": "John Smith",
    "email": "john@example.com",
    "telephone": "07123456789",
    "enquiry_type": "Motor Insurance"
}
```

8. Click Send.

#### Expected Result

HTTP status: 200 OK

The response should contain a JSON object that includes
the customer information you submitted.

The demonstration API returns the submitted data
but does not create an actual insurance enquiry
or insurance policy.

### 8. Understanding HTTP Status Codes

| Status Code | Meaning | Recommended Action |
| --- | --- | --- |
| 200 | OK | Request successful |
| 201 | Created | Resource successfully created |
| 400 | Bad Request | Check submitted information |
| 401 | Unauthorized | Check authentication credentials |
| 403 | Forbidden | Check access permissions |
| 404 | Not Found | Check the endpoint URL |
| 429 | Too Many Requests | Respect the API rate limit |
| 500 | Internal Server Error | Check service status or contact support |

### 9. Troubleshooting Authentication

Return to the bearer token authentication request.

1. Open the Authorization tab.
2. Change the authentication type to No Auth.
3. Ensure no Authorization header is being sent.
4. Click Send.

#### Expected Result

HTTP status: 401 Unauthorized

This demonstrates how an API may respond when
required authentication credentials are missing.

An unsuccessful API response is not necessarily
an unsuccessful test.

In this example, receiving a 401 response is the
expected behaviour and therefore represents a
successful negative test.

### 10. Requesting Technical Support

When reporting an API integration issue, provide:

- The API endpoint.
- The HTTP request method.
- The HTTP status code.
- The error message.
- The date and time of the request.
- A description of the expected behaviour.
- A description of the actual behaviour.
- Relevant request or correlation IDs, if available.

Remove all sensitive customer information,
authentication credentials and API tokens before
sharing request or response details.

Providing this information helps technical support
and engineering teams investigate issues efficiently.

### 11. Next Steps

You have now explored:

- GET requests.
- POST requests.
- JSON data.
- Bearer token authentication.
- HTTP status codes.
- Positive and negative API testing.

For further information about the Python integration,
refer to the [Project README](README.md).

### 12. Disclaimer

This guide forms part of an independent educational
API integration demonstration.

It is not affiliated with SchemeServe or any
insurance provider.

The demonstration API does not process real
insurance policies or customer information.