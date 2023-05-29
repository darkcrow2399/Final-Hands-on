# Final-Hands-on
# CRUD REST API

This is a simple Flask application that provides a CRUD (Create, Read, Update, Delete) REST API for managing records. The API allows users to interact with records and supports JSON responses.

## Getting Started

Follow the instructions below to set up and run the project on your local machine.

### Prerequisites

- Python 3.x
- Flask (install using `pip install Flask`)

### Installation

1. Clone the repository to your local machine:


2. Navigate to the project directory:


3. Install the required dependencies using pip:


### Usage

1. Run the Flask application:


2. The API server will start running on `http://localhost:5000/`.

3. Use a tool like cURL, Postman, or a web browser to interact with the API endpoints.

### Endpoints

- `GET /api/marvel`: Retrieves a random Marvel movie from the list of available movies.
- `POST /api/marvel`: Adds a new Marvel movie to the list.
- `PUT /api/marvel/{id}`: Replaces a Marvel movie with the specified ID.
- `PATCH /api/marvel/{id}`: Updates a Marvel movie with the specified ID.
- `DELETE /api/marvel/{id}`: Deletes a Marvel movie with the specified ID.

### Examples

- GET request to retrieve a random Marvel movie:

- POST request to add a new Marvel movie:

- PUT request to replace a Marvel movie:

- PATCH request to update a Marvel movie:

- DELETE request to delete a Marvel movie:

### License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

