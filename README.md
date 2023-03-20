# Placement Management System

This is a web-based system for managing job placements for a college. It allows students to create profiles, upload their resumes, and apply for job opportunities posted by employers. Employers can also create profiles, post job opportunities, and review applications from students.

The application is built using Django, a Python web framework, and PostgreSQL, a powerful open source relational database system. It uses REST APIs to handle data requests between the front-end and back-end components.

## Features

- User authentication and authorization
- Student and employer profile creation and management
- Job opportunity posting and application management
- Resume uploading and management
- REST API for handling data requests

## Requirements

- Docker
- Docker Compose

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/anuragdevon/pl_mangement
```



2. Navigate to the project directory:


```
cd placement-management-system
```


3. Setup the Docker container:


```
docker-compose up --build
```



The application should now be accessible at http://localhost:8000.

## API Documentation

The API documentation is available at http://localhost:8000/swagger/ or http://localhost:8000/redoc/ when the development server is running.

## Contributing

Contributions to the project are welcome. Before making any changes, please create an issue to discuss the proposed changes.

To set up a development environment, follow the installation instructions above and create a new branch for your changes:

```
git checkout -b my-feature-branch
```


After making your changes, run the tests to ensure that everything is working correctly:

```
docker-compose run web python manage.py test
```


Finally, submit a pull request to merge your changes into the main branch.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
