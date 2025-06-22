# Telehealth Platform API Documentation

## Overview
This API provides endpoints for managing a telehealth platform, including user management, doctor and patient profiles, and appointment scheduling.

## Authentication

### Login
- **Endpoint**: `/token`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Response**:
  ```json
  {
    "access_token": "string",
    "token_type": "bearer"
  }
  ```

### User Profile
- **Endpoint**: `/users/me`
- **Method**: GET
- **Authorization**: Bearer token
- **Response**:
  ```json
  {
    "id": "integer",
    "email": "string",
    "first_name": "string",
    "last_name": "string",
    "is_active": "boolean",
    "is_superuser": "boolean"
  }
  ```

## Users API

### Get All Users
- **Endpoint**: `/users`
- **Method**: GET
- **Authorization**: Bearer token (requires superuser)
- **Response**:
  ```json
  [
    {
      "id": "integer",
      "email": "string",
      "first_name": "string",
      "last_name": "string",
      "is_active": "boolean",
      "is_superuser": "boolean"
    }
  ]
  ```

### Get User by ID
- **Endpoint**: `/users/{user_id}`
- **Method**: GET
- **Authorization**: Bearer token
- **Response**:
  ```json
  {
    "id": "integer",
    "email": "string",
    "first_name": "string",
    "last_name": "string",
    "is_active": "boolean",
    "is_superuser": "boolean"
  }
  ```

## Doctors API

### Get All Doctors
- **Endpoint**: `/doctors`
- **Method**: GET
- **Authorization**: Bearer token
- **Response**:
  ```json
  [
    {
      "id": "integer",
      "specialization": "string",
      "license_number": "string",
      "years_of_experience": "integer"
    }
  ]
  ```

### Get Doctor by ID
- **Endpoint**: `/doctors/{doctor_id}`
- **Method**: GET
- **Authorization**: Bearer token
- **Response**:
  ```json
  {
    "id": "integer",
    "specialization": "string",
    "license_number": "string",
    "years_of_experience": "integer"
  }
  ```

## Patients API

### Get All Patients
- **Endpoint**: `/patients`
- **Method**: GET
- **Authorization**: Bearer token
- **Response**:
  ```json
  [
    {
      "id": "integer",
      "medical_record_number": "string",
      "date_of_birth": "datetime",
      "emergency_contact_name": "string",
      "emergency_contact_phone": "string",
      "has_insurance": "boolean"
    }
  ]
  ```

### Get Patient by ID
- **Endpoint**: `/patients/{patient_id}`
- **Method**: GET
- **Authorization**: Bearer token
- **Response**:
  ```json
  {
    "id": "integer",
    "medical_record_number": "string",
    "date_of_birth": "datetime",
    "emergency_contact_name": "string",
    "emergency_contact_phone": "string",
    "has_insurance": "boolean"
  }
  ```

## Appointments API

### Get All Appointments
- **Endpoint**: `/appointments`
- **Method**: GET
- **Authorization**: Bearer token
- **Response**:
  ```json
  [
    {
      "id": "integer",
      "scheduled_time": "datetime",
      "status": "string",
      "notes": "string"
    }
  ]
  ```

### Get Appointment by ID
- **Endpoint**: `/appointments/{appointment_id}`
- **Method**: GET
- **Authorization**: Bearer token
- **Response**:
  ```json
  {
    "id": "integer",
    "scheduled_time": "datetime",
    "status": "string",
    "notes": "string"
  }
  ```

### Create Appointment
- **Endpoint**: `/appointments`
- **Method**: POST
- **Authorization**: Bearer token
- **Request Body**:
  ```json
  {
    "scheduled_time": "datetime",
    "status": "string",
    "notes": "string"
  }
  ```

### Update Appointment Status
- **Endpoint**: `/appointments/{appointment_id}`
- **Method**: PUT
- **Authorization**: Bearer token
- **Request Body**:
  ```json
  {
    "status": "string"
  }
  ```
