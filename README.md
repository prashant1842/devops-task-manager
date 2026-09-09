# Automated CI/CD & Docker Deployment Pipeline

A DevOps project demonstrating an automated CI/CD pipeline for a Flask and MySQL Task Manager application using GitHub Actions, Docker, Docker Hub, and Trivy.

## Project Overview

This project automates the software delivery process of a Flask-based Task Manager application.

Whenever code is pushed to the `main` branch, GitHub Actions automatically:

1. Installs Python dependencies
2. Starts a MySQL service
3. Creates the required database table
4. Runs automated tests using Pytest
5. Builds a Docker image
6. Scans the Docker image using Trivy
7. Pushes the image to Docker Hub

The Docker image can then be deployed in a Linux-based Docker environment.

## Architecture

Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions
    |
    +----> Pytest
    |
    +----> Docker Build
    |
    +----> Trivy Security Scan
    |
    v
Docker Hub
    |
    v
Linux Docker Environment
    |
    +----> Flask Application
    |
    +----> MySQL Database

## Technologies Used

- Python
- Flask
- MySQL
- SQL
- Linux
- Docker
- Docker Compose
- Git
- GitHub
- GitHub Actions
- Docker Hub
- Trivy
- Pytest
- Bash

## Application Features

The Task Manager application allows users to:

- View tasks
- Add new tasks
- Mark tasks as completed
- Delete tasks
- Store task data in MySQL

## Project Structure

```text
devops-task-manager/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── app/
│   ├── app.py
│   ├── database.py
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   └── index.html
│   └── test/
│       └── test_app.py
│
├── Dockerfile
├── docker-compose.yml
├── init.sql
├── requirements.txt
├── .gitignore
└── README.md