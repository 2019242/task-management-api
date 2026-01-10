# Task Management API

## Student Information
- Name: 
- Department: Department of Informatics
- University: Ionian University
- Course: Software Engineering
- Academic Year: 

## Description
This project implements a simple RESTful API for managing tasks.  
Each task includes:
- id
- username
- title
- description
- deadline

The API is built using **Python and Flask** and stores data in an **SQLite** database.

## Available Endpoints
- `GET /tasks` – Retrieve all tasks
- `GET /tasks/{id}` – Retrieve a task by ID
- `POST /tasks` – Create a new task
- `DELETE /tasks/{id}` – Delete a task by ID

## Testing
Unit tests are written using Python’s `unittest` framework and validate:
- Task creation
- Task retrieval
- Error handling
