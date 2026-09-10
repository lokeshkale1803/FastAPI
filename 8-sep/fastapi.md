# FastAPI Implementation Documentation for Student Management System

## 1. Introduction

The Student Management System is a simple CRUD-based application used to manage student records.

CRUD stands for:

* Create – Add a new student
* Read – Display student information
* Update – Modify existing student information
* Delete – Remove a student record

In this project, FastAPI is used to convert normal Python functions into API endpoints.

---

## 2. Technologies Used

* Python
* FastAPI
* Uvicorn
* Pydantic
* Dictionary for temporary data storage

---

## 3. Installation

Install FastAPI and Uvicorn using:

```bash
pip install fastapi uvicorn
```

FastAPI is used to create APIs.

Uvicorn is used to run the FastAPI server.

---

## 4. Import Required Libraries

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
```

### Explanation

`FastAPI`

Used to create the API application.

`HTTPException`

Used to return proper error messages such as:

```text
404 - Student not found
```

`BaseModel`

Used to define and validate the data received from the user.

---

## 5. Create FastAPI Application

```python
app = FastAPI()
```

This line creates the FastAPI application.

The variable `app` represents our API server.

---

## 6. Student Data Storage

```python
students = {}
```

The dictionary is used to temporarily store student information.

Example:

```python
students = {
    101: "Lokesh",
    102: "Rahul"
}
```

Here:

```text
101 → Student ID
Lokesh → Student Name
```

The dictionary stores data only while the application is running.

If the server stops, the data is lost.

---

## 7. Student Data Model

```python
class Student(BaseModel):
    name: str
```

This model defines the structure of student data.

FastAPI expects data in JSON format.

Example:

```json
{
    "name": "Lokesh"
}
```

The `name` must be a string.

---

# 8. Home API

```python
@app.get("/")
def home():

    return {
        "message": "Student Management API is running"
    }
```

This API checks whether the server is working.

### Endpoint

```text
GET /
```

### Response

```json
{
    "message": "Student Management API is running"
}
```

---

# 9. Create Student API

```python
@app.post("/students/{student_id}")
def create_student(student_id: int, student: Student):

    if student_id in students:

        raise HTTPException(
            status_code=400,
            detail="Student ID already exists"
        )

    students[student_id] = student.name

    return {
        "message": "Student created successfully",
        "students": students
    }
```

## Purpose

This API creates a new student.

### Endpoint

```text
POST /students/{student_id}
```

Example:

```text
POST /students/101
```

### Request Body

```json
{
    "name": "Lokesh"
}
```

### Internal Operation

```python
students[101] = "Lokesh"
```

Dictionary becomes:

```python
{
    101: "Lokesh"
}
```

### Response

```json
{
    "message": "Student created successfully",
    "students": {
        "101": "Lokesh"
    }
}
```

---

# 10. Read Students API

```python
@app.get("/students")
def read_students():

    return students
```

## Purpose

This API displays all stored students.

### Endpoint

```text
GET /students
```

### Response

```json
{
    "101": "Lokesh",
    "102": "Rahul"
}
```

No request body is required.

---

# 11. Update Student API

```python
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    if student_id not in students:

        raise HTTPException(
            status_code=404,
            detail="Student ID not found"
        )

    students[student_id] = student.name

    return {
        "message": "Student updated successfully",
        "students": students
    }
```

## Purpose

This API updates an existing student's name.

### Endpoint

```text
PUT /students/101
```

### Request Body

```json
{
    "name": "Lokesh Kale"
}
```

Before update:

```python
{
    101: "Lokesh"
}
```

After update:

```python
{
    101: "Lokesh Kale"
}
```

---

# 12. Delete Student API

```python
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    if student_id not in students:

        raise HTTPException(
            status_code=404,
            detail="Student ID not found"
        )

    del students[student_id]

    return {
        "message": "Student deleted successfully",
        "students": students
    }
```

## Purpose

This API removes a student record.

### Endpoint

```text
DELETE /students/101
```

Before deletion:

```python
{
    101: "Lokesh"
}
```

After deletion:

```python
{}
```

---

# 13. Complete FastAPI Code

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


students = {}


class Student(BaseModel):

    name: str


@app.get("/")
def home():

    return {
        "message": "Student Management API is running"
    }


@app.post("/students/{student_id}")
def create_student(student_id: int, student: Student):

    if student_id in students:

        raise HTTPException(
            status_code=400,
            detail="Student ID already exists"
        )

    students[student_id] = student.name

    return {
        "message": "Student created successfully",
        "students": students
    }


@app.get("/students")
def read_students():

    return students


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    if student_id not in students:

        raise HTTPException(
            status_code=404,
            detail="Student ID not found"
        )

    students[student_id] = student.name

    return {
        "message": "Student updated successfully",
        "students": students
    }


@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    if student_id not in students:

        raise HTTPException(
            status_code=404,
            detail="Student ID not found"
        )

    del students[student_id]

    return {
        "message": "Student deleted successfully",
        "students": students
    }
```

---

# 14. Run the Application

Save the file as:

```text
main.py
```

Open terminal and run:

```bash
uvicorn main:app --reload
```

The server will start on:

```text
http://127.0.0.1:8000
```

---

# 15. FastAPI Documentation Page

Open:

```text
http://127.0.0.1:8000/docs
```

FastAPI automatically generates an interactive API documentation page.

From here we can test:

```text
POST   /students/{student_id}

GET    /students

PUT    /students/{student_id}

DELETE /students/{student_id}
```

without using Postman.

---

# 16. API Flow

The overall application flow is:

```text
User / Frontend
      ↓
HTTP Request
      ↓
FastAPI Endpoint
      ↓
Python Function
      ↓
Student Dictionary
      ↓
JSON Response
      ↓
User / Frontend
```

Example:

```text
POST /students/101
        ↓
create_student()
        ↓
students[101] = "Lokesh"
        ↓
JSON Response
```

---

# 17. HTTP Methods Used

| Operation      | HTTP Method | Endpoint                 |
| -------------- | ----------- | ------------------------ |
| Create Student | POST        | `/students/{student_id}` |
| Read Students  | GET         | `/students`              |
| Update Student | PUT         | `/students/{student_id}` |
| Delete Student | DELETE      | `/students/{student_id}` |

---

# 18. Difference Between Normal Python and FastAPI

Normal Python program:

```text
User
 ↓
input()
 ↓
Python Function
 ↓
Dictionary
 ↓
print()
```

FastAPI program:

```text
Frontend
 ↓
HTTP Request
 ↓
FastAPI
 ↓
Python Function
 ↓
Dictionary / Database
 ↓
JSON Response
```

FastAPI removes the need for terminal-based `input()` and `print()`.

Instead, information is sent and received through APIs.

---

# 19. Future Improvements

The current project uses:

```python
students = {}
```

This is temporary storage.

A more complete version can use:

```text
FastAPI
   ↓
Python CRUD Logic
   ↓
SQLite / MySQL
```

After that, a frontend such as HTML, CSS and JavaScript can communicate with FastAPI.

Final architecture:

```text
HTML / CSS / JavaScript
          ↓
        FastAPI
          ↓
        MySQL
```

This creates a proper full-stack Student Management System.

---

# 20. Conclusion

FastAPI is used in this project to expose student CRUD operations through HTTP APIs.

The system supports:

* Adding students
* Viewing students
* Updating student records
* Deleting students

FastAPI provides a simple and structured way to connect Python backend logic with web applications, mobile applications, or other software.
