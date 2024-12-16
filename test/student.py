from http.client import HTTPException
from typing import Optional

from fastapi import Path
from pydantic import BaseModel



class Student(BaseModel):
    name: str
    age: int
    year: str
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


students = {
    1: Student(name="John", age=21, year="2021"),
    2: Student(name="Jane", age=23, year="2021"),
}

@app.get("/")
def index():
    return students
@app.get("/students/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student to get")):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str]= None, test : int):
    for student_id in students:
        if students[student_id].name == name:
            return students[student_id]
    return {"data": "No student found"}


@app.post("/students/{student_id}")
def create_student(student_id: int,student: Student):
    if student_id in students:
        return {"Error":"Student with this ID already exists"}
    students[student_id] = student
    return student

@app.put("/students/{student_id}")
def update_student(student_id: int,student: UpdateStudent):
    if student_id not in students:
        return {"Error":"Student with this ID does not exist"}
    for key, value in student.dict().items():
        if value is not None:
            setattr(students[student_id], key, value)
    return students[student_id]

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error":"Student with this ID does not exist"}
    del students[student_id]
    return {"message": "Student deleted successfully"}