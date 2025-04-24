# crud-fast-api
This repository contains a FastAPI-based microservice for managing user data. It provides a RESTful API with CRUD (Create, Read, Update, Delete) operations for users. The application is designed to be modular, scalable, and easy to integrate with other services.

---

### **Repository Description**

This repository contains a FastAPI-based microservice for managing user data. It provides a RESTful API with CRUD (Create, Read, Update, Delete) operations for users. The application is designed to be modular, scalable, and easy to integrate with other services.

#### **Key Features**
- **Create User**: Add a new user to the database.
- **Read User**: Retrieve user details by ID or fetch a list of users with pagination.
- **Update User**: Modify existing user information.
- **Delete User**: Remove a user from the database.

#### **Unit Testing**
The project includes unit tests to ensure the reliability of the API endpoints. These tests cover:
- **Create User**: Verifies that a user can be successfully created.
- **Get User**: Ensures that a user can be retrieved by ID.
- **Update User**: Confirms that user details can be updated.
- **Delete User**: Validates that a user can be deleted and is no longer accessible.

The tests are located in the `tests/` directory and can be executed using `pytest`.

#### **Docker Support**
The application is containerized using Docker for easy deployment. A `Dockerfile` is provided to build the application image, and a docker-compose.yml file is included for managing the service.

- **Dockerfile**: Defines the application environment and dependencies.
- **docker-compose.yml**: Simplifies running the application with a single command.

To build and run the application using Docker:
1. Build the Docker image:
   ```bash
   docker build -t fastapi-microservice .
   ```
2. Run the application:
   ```bash
   docker-compose up
   ```

#### **Project Structure**
The project is organized as follows:
```
fastapi-microservice/
├── app/
│   ├── main.py          # Application entry point
│   ├── models.py        # Database models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # CRUD operations
│   ├── database.py      # Database configuration
│   ├── config.py        # Application settings
│   └── routers/         # API route definitions
├── tests/               # Unit tests
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose configuration
└── README.md            # Project documentation
```

This setup ensures the application is production-ready, testable, and easy to deploy.
