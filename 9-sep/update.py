from fastapi import FastAPI

# Create FastAPI application
app = FastAPI()


# Temporary student data
students = [
    {
        "id": 1,
        "name": "Ram",
        "course": "Python",
        "marks": 85
    },
    {
        "id": 2,
        "name": "Diya",
        "course": "AI",
        "marks": 90
    }
]


@app.get("/students")
def get_students():
    # Return all students
    return students

@app.put("/students/{student_id}")
def update_student(student_id: int, data: dict):

    for student in students:
        if student["id"] == student_id:
            student.update(data)
            
            return student

    return {"message": "Student not found"}


@app.delete("/students")
def delete_student(id: int):

    for student in students:
        if student["id"] == id:
            students.remove(student)

            return {
                "message": "Student deleted successfully"
            }

    return {
        "message": "Student not found"
    }
    
    
# POST
@app.post("/students")
def add_student(data: dict):

    students.append(data)

    return {
        "message": "Student added successfully",
        "student": data
    }
