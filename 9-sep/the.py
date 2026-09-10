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
