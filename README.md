﻿# Flask-crud-API
# Intellisqr Employee Management System

This is a simple REST API built using Flask for managing employees in the Intellisqr Employee Management System. It provides basic CRUD (Create, Read, Update, Delete) operations for managing employee data stored in a MongoDB database.

## Setup

To run the application locally, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:
markdown

# Intellisqr Employee Management System

This is a simple REST API built using Flask for managing employees in the Intellisqr Employee Management System. It provides basic CRUD (Create, Read, Update, Delete) operations for managing employee data stored in a MongoDB database.

## Setup

To run the application locally, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

git clone https://github.com/SachinNic1502/Flask-crud-API/


2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using the following command:

pip install -r requirements.txt


3. **Run the Application**: Start the Flask application by running the following command:

python app.py


4. **Access the API**: Once the application is running, you can access the API endpoints using a tool like Postman or by making HTTP requests.

## Endpoints

### Get All Employees

- **URL**: `/employees`
- **Method**: `GET`
- **Description**: Retrieves a list of all employees stored in the database.

### Get Single Employee

- **URL**: `/employees/<employee_id>`
- **Method**: `GET`
- **Description**: Retrieves details of a specific employee identified by their unique ID.

### Create Employee

- **URL**: `/employees`
- **Method**: `POST`
- **Description**: Creates a new employee record in the database.

### Update Employee

- **URL**: `/employees/<employee_id>`
- **Method**: `PUT`
- **Description**: Updates details of an existing employee identified by their unique ID.

### Delete Employee

- **URL**: `/employees/<employee_id>`
- **Method**: `DELETE`
- **Description**: Deletes an existing employee record from the database.

## Dependencies

- Flask
- Flask-Cors
- pymongo
- bson

## Database

The application uses MongoDB as its database to store employee data. You can configure the MongoDB connection details in the `app.py` file.

## Contributors

- [Sachin Rahod](https://github.com/SachinNic1502)

