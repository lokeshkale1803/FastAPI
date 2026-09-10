from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# CREATE
@app.post("/students")
def create_student(name: str, course: str, marks: int):
    student = {
        "name": name,
        "course": course,
        "marks": marks
    }

    response = (
        supabase.table("students")
        .insert(student)
        .execute()
    )

    return {
        "message": "Student created successfully",
        "data": response.data
    }


# READ
@app.get("/students")
def get_students():
    response = (
        supabase.table("students")
        .select("*")
        .execute()
    )

    return {
        "data": response.data
    }


# UPDATE
@app.put("/students/{student_name}")
def update_student(student_name: str, course: str, marks: int):
    updated_data = {
        "course": course,
        "marks": marks
    }

    response = (
        supabase.table("students")
        .update(updated_data)
        .eq("name", student_name)
        .execute()
    )

    if response.data:
        return {
            "message": "Student updated successfully",
            "data": response.data
        }

    return {"message": "Student not found"}


# DELETE
@app.delete("/students/{student_name}")
def delete_student(student_name: str):
    response = (
        supabase.table("students")
        .delete()
        .eq("name", student_name)
        .execute()
    )

    if response.data:
        return {
            "message": "Student deleted successfully",
            "data": response.data
        }

    return {"message": "Student not found"}