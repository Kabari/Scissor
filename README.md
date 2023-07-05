# 
# Scissor

**Shorten URL Service**

## Description

The Shorten URL Service is a web application that allows users to shorten long URLs and create custom short URLs. It provides a user-friendly interface for generating short URLs, tracking link performance, and managing custom domains.

## Features

- Shorten long URLs to compact and manageable short URLs
- Customizable short URLs with user-defined domains
- QR code generation for each short URL
- Link performance tracking and analytics
- User authentication and authorization
- Categorization of URLs for easy management

## Technologies Used

- Python
- Flask (Python web framework)
- SQLAlchemy (Python SQL toolkit)
- SQLite (Relational database)
- HTML/CSS/JavaScript (Front-end)
- Axios (JavaScript HTTP client)

## Installation

1. Clone the repository: `git clone https://github.com/Kabari/Scissor.git`
2. Change to the project directory: `cd Scissor`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment: `source venv/Scripts/activate`
5. Install the dependencies: `pip install -r requirements.txt`
6. Set up the database:
   In your terminal type `flask shell` then type `db.create_all()`
8. Start the application: `flask run`

## Configuration
## The application can be configured by modifying the `.env` file.

- Create a `.env` file in your root directory of the project
- Add the following configurations to the file
  ```
    SECRET_KEY = 'your secret key'
    JWT_SECRET_KEY = 'your JWT secret key'
    DEBUG = TRUE
    FLASK_APP=runserver
    CACHE_TYPE = SimpleCache
    FLASK_ENV=development
  ```
 Make sure to set the appropriate values in the `config.py` for:

- Database connection details

## Usage

1. Access the application in your web browser: `http://localhost:5000`
2. Register an account or log in with your existing credentials.
3. Shorten long URLs, customize short URLs, and track link performance using the provided features.

# Endpoints

## Signup

**Description:** Register a new account

**Endpoint:** `/auth/signup`

**Method:** POST

**Request Body:**
  ```
    {
    "first_name": "string",
    "last_name": "string",
    "email": "string",
    "password": "string",
    "confirm_password": "string"
    }
  ```
**Responses:**

- **HTTP Status Code: 201**
  - **Description:** Success
  - **Body:**
    ```
    {
      "id": "integer",
      "first_name": "string",
      "last_name": "string",
      "email": "string",
      "is_verified": "boolean"
    }
    ```

- **HTTP Status Code: 400**
  - **Description:** Validation Error or User already exists
  - **Body:**
    ```
    {
      "message": "string"
    }
    ```

## Login

**Description:** Login to your account

**Endpoint:** `/auth/login`

**Method:** POST

**Request Body:**
'''
{
"email": "string",
"password": "string"
}
'''

**Responses:**

- **HTTP Status Code: 200**
  - **Description:** Success
  - **Body:**
    ```
    {
      "message": "Logged in as [user_email]",
      "access_token": "string",
      "refresh_token": "string"
    }
    ```

- **HTTP Status Code: 401**
  - **Description:** Invalid credentials

## Refresh

**Description:** Refresh the User's Access Token

**Endpoint:** `/auth/refresh`

**Method:** POST

**Security:** JWT token (Include the access token in the request header as `Authorization: Bearer [access_token]`)

**Responses:**

- **HTTP Status Code: 200**
  - **Description:** Success
  - **Body:**
    ```
    {
      "access_token": "string"
    }
    ```

## Logout

**Description:** Log the User Out

**Endpoint:** `/auth/logout`

**Method:** POST

**Security:** JWT token (Include the access token in the request header as `Authorization: Bearer [access_token]`)

**Responses:**

- **HTTP Status Code: 200**
  - **Description:** Success
  - **Body:**
    ```
    {
      "message": "Successfully Logged Out"
    }
    ```

## Dashboard

**Description:** Get the dashboard details

**Endpoint:*** `/url/dashboard`

**Method:** GET

**Security:** JWT token (Include the access token in the request header as `Authorization: Bearer [access_token]`)

**Responses:**

- **HTTP Status Code: 200**
  - **Description:** Success
  - **Body:**
      ```
      {
        "first_name": "string",
        "total_urls": "integer",
        "total_clicks": "integer"
      }
      ```
- **HTTP Status Code:** 404
  - **Description:** User not found

## Create URL

**Description:** Create a shortened URL

**Endpoint:** `/url/create`

**Method:** POST

**Security:** JWT token (Include the access token in the request header as `Authorization: Bearer [access_token]`)

**Rate Limit:** 10 requests per minute

**Request Body:**
```
{
  "long_url": "string"
}
```
**Responses:**

- **HTTP Status Code:** 201

- **Description:** Created
- **Body:**
```
{
  "id": "integer",
  "long_url": "string",
  "short_code": "string",
  "short_url": "string",
  "user_id": "string"
}
```
- **HTTP Status Code:** 400
- **Description:** Bad request (Invalid URL)

## Redirect URL

**Description:** Redirect to the original URL

**Endpoint:** `/url/<short_code>`

**Method:** GET

**Responses:**

- **HTTP Status Code:** 302
  - **Description:** Success (Redirects to the original URL)

- **HTTP Status Code:** 404
  - **Description:** Invalid short URL


## Update Custom Domain
**Description:** Update the custom domain

**Endpoint:** `/url/custom/<short_code>`

**Method:** PATCH

**Security:** JWT token (Include the access token in the request header as `Authorization: Bearer [access_token]`)

**Params:**
  **short_code:** Specify the short code
  
**Request Body:**
    ```
    {
      "custom_domain": "string"
    }
    ```
**Responses:**

- **HTTP Status Code:** 201

  - **Description:** Created
  - **Body:**
    ```
      {
        "id": "integer",
        "long_url": "string",
        "short_code": "string",
        "short_url": "string",
        "custom_domain": "string",
        "user_id": "string"
      }
  ```

- **HTTP Status Code:** 404
  - **Description:** URL not found
 
    
## Get All URLs
**Description:** Get all URLs

**Endpoint:** `/url/urls`

**Method:** GET

**Security:** JWT token (Include the access token in the request header as `Authorization: Bearer [access_token]`)

**Responses:**

- **HTTP Status Code:** 200

  - **Description:** Success
  - **Body:** Array of URL objects
    ```
      [
        {
          "id": "integer",
          "long_url": "string",
          "short_code": "string",
          "short_url": "string",
          "user_id": "string"
        },
        ...
      ]
    ```
- **HTTP Status Code:** 404

  - **Description:** User not found


## URL Analytics
**Description:** Get analytics for a URL

**Endpoint:** `/url/analytics/<short_code>`

**Method:** GET

**Params:**

**short_code:** Short code of the URL
**Responses:**

- **HTTP Status Code:** 200

  - **Description:** Success
  - **Body:**
    ```
      {
        "short_code": "string",
        "clicks": [
          {
            "id": "integer",
            "timestamp": "string",
            "ip_address": "string",
            "referrer": "string",
            "user_agent": "string"
          },
          ...
        ]
      }
    ```
    
- **HTTP Status Code:** 404

  - **Description:** Invalid short URL

  
## Get QR Code
**Description:** Get QR code for a URL

**Endpoint:** `/url/qr-code/<short_code>`

**Method:** GET

**Params:**

**short_code:** Short code of the URL
**Responses:**

- **HTTP Status Code:** 200

  - **Description:** Success (Returns the QR code image)
  - **Body:** QR code image file

- **HTTP Status Code:** 404

  - **Description:** Invalid short URL



## Contributing

Contributions are welcome! If you have any ideas, bug fixes, or improvements, please submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) - Python web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL toolkit
- [Flask-Restx](https://flask-restx.readthedocs.io/en/latest/) - Flask RestAPI



