# Event Management API

## Overview
A Django REST API for managing events like conferences and meetups. Allows users to create, view, update, delete events, and register for events.

## Requirements
- Python 3.9+
- Docker (for containerization)
- Django and Django REST framework

## Installation
1. Clone the repository.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run migrations with `python manage.py migrate`.
4. Start the server with `python manage.py runserver`.

## Usage
- Register: `POST /api/register/`
- Obtain Token: `POST /api/token/`
- Events CRUD: `/api/events/`
- Event Registration: `POST /api/events/<id>/register/`

## API Documentation
Visit `/api/docs/` for Swagger documentation.
