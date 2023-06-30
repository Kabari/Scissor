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
3. Install the dependencies: `pip install -r requirements.txt`
4. Set up the database: `python manage.py create_db`
5. Start the application: `python manage.py runserver`

## Configuration

The application can be configured by modifying the `config.py` file. Make sure to set the appropriate values for:

- Database connection details
- JWT secret key

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
'''
{
"first_name": "string",
"last_name": "string",
"email": "string",
"password": "string",
"confirm_password": "string"
}
'''
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



## Contributing

Contributions are welcome! If you have any ideas, bug fixes, or improvements, please submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) - Python web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL toolkit
- [Bootstrap](https://getbootstrap.com/) - CSS framework

Feel free to customize the documentation according to your project's specific details and requirements.
