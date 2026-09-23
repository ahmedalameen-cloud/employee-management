# Employee Management System

A simple web-based Employee Management System built using Flask and MySQL, containerized with Docker and deployed on AWS EC2.

## Project Overview

This project allows users to manage employee information through a web interface.

## Features

- Add new employees
- View employee list
- Delete employees
- Store employee data in MySQL
- Containerized using Docker
- Deployed on AWS EC2

## Technologies Used

- Python
- Flask
- MySQL
- Docker
- Docker Compose
- AWS EC2
- Ubuntu Linux
- Git
- GitHub

## Architecture

User
  |
  v
AWS EC2 Public IP
  |
  v
Flask Web Application
  |
  v
MySQL Database


## Docker Services

### Web Application

- Service Name: web
- Technology: Python Flask
- Container Name: employee-app
- Port: 5000

### Database

- Service Name: mysql
- Database: MySQL 8.0
- Container Name: employee-db
- Database Name: employee_db
- Port: 3306

## Docker Compose

The application and database are managed using Docker Compose.

Start the application:

    docker compose up -d --build

Check running containers:

    docker compose ps

View application logs:

    docker compose logs web

View database logs:

    docker compose logs mysql

Stop the application:

    docker compose down

Restart the application:

    docker compose up -d

## How to Run

Clone the repository:

    git clone https://github.com/ahmedalameen-cloud/employee-management.git

Go to the project directory:

    cd employee-management

Build and start the containers:

    docker compose up -d --build

Check the containers:

    docker compose ps

Access the application:

    http://<EC2-PUBLIC-IP>:5000

## AWS Deployment

The application was deployed on an AWS EC2 Ubuntu instance.

Deployment steps:

1. Created an AWS EC2 Ubuntu instance.
2. Configured the EC2 Security Group.
3. Allowed SSH access through port 22.
4. Allowed application access through port 5000.
5. Connected to the EC2 instance using SSH.
6. Installed Docker and Docker Compose.
7. Cloned the project from GitHub.
8. Built the Docker image.
9. Started Flask and MySQL containers using Docker Compose.
10. Accessed the application using the EC2 public IP.

## Security Group

Required inbound rules:

- SSH - Port 22
- Custom TCP - Port 5000

## Project Structure

    employee-management/
    |
    |-- app.py
    |-- Dockerfile
    |-- docker-compose.yml
    |-- requirements.txt
    |-- README.md
    |-- static/
    |-- templates/

## Application Functions

### Add Employee

Users can add employee details such as:

- Name
- Email
- Department
- Salary

### View Employees

The application displays employee information stored in the MySQL database.

### Delete Employee

Users can delete employee records directly from the web interface.

## Database

The application uses MySQL to store employee information.

Database:

    employee_db

Table:

    employees

## Docker Architecture

    +----------------------+
    |        User          |
    +----------+-----------+
               |
               v
    +----------------------+
    |     AWS EC2          |
    |   Public IP:5000     |
    +----------+-----------+
               |
               v
    +----------------------+
    |   Flask Container    |
    |    employee-app      |
    +----------+-----------+
               |
               v
    +----------------------+
    |   MySQL Container    |
    |     employee-db      |
    +----------------------+

## Useful Commands

Check Docker version:

    docker --version

Check Docker Compose version:

    docker compose version

List running containers:

    docker ps

Check project containers:

    docker compose ps

Start containers:

    docker compose up -d

Build and start:

    docker compose up -d --build

Stop containers:

    docker compose down

View logs:

    docker compose logs

View Flask logs:

    docker compose logs web

View MySQL logs:

    docker compose logs mysql

## Git Commands

Check status:

    git status

Add changes:

    git add .

Commit changes:

    git commit -m "Update README"

Push to GitHub:

    git push

## Project Outcome

The Employee Management System was successfully containerized using Docker and deployed on AWS EC2. The Flask application communicates with the MySQL database through Docker Compose, allowing users to add, view, and delete employee records through a web interface.

## Author

Ahmed Al Ameen

B.Tech IT Graduate  
AWS & DevOps Enthusiast

