import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000"

def add_student(name, course, marks):
    try:
        response = requests.post(f"{API_URL}/students", params={"name": name, "course": course, "marks": int(marks)})
        if response.status_code == 200:
            return response.json().get("message", "Success!")
        return f"Error: {response.text}"
    except Exception as e:
        return str(e)

def view_students():
    try:
        response = requests.get(f"{API_URL}/students")
        if response.status_code == 200:
            data = response.json().get("data", [])
            if not data:
                return "No students found."
            
            # Format as a string for easy reading
            result = ""
            for student in data:
                result += f"Name: {student.get('name')}, Course: {student.get('course')}, Marks: {student.get('marks')}\n"
            return result
        return f"Error: {response.text}"
    except Exception as e:
        return str(e)

def update_student(name, course, marks):
    try:
        response = requests.put(f"{API_URL}/students/{name}", params={"course": course, "marks": int(marks)})
        if response.status_code == 200:
            return response.json().get("message", "Success!")
        return f"Error: {response.text}"
    except Exception as e:
        return str(e)

def delete_student(name):
    try:
        response = requests.delete(f"{API_URL}/students/{name}")
        if response.status_code == 200:
            return response.json().get("message", "Success!")
        return f"Error: {response.text}"
    except Exception as e:
        return str(e)

# Create Gradio Interface
with gr.Blocks(title="Student Management System") as demo:
    gr.Markdown("# Student Management System")
    
    with gr.Tab("View Students"):
        view_btn = gr.Button("Refresh Student List")
        view_output = gr.Textbox(label="Students", lines=10)
        view_btn.click(view_students, inputs=[], outputs=view_output)
        
    with gr.Tab("Add Student"):
        add_name = gr.Textbox(label="Name")
        add_course = gr.Textbox(label="Course")
        add_marks = gr.Number(label="Marks")
        add_btn = gr.Button("Add")
        add_output = gr.Textbox(label="Result")
        add_btn.click(add_student, inputs=[add_name, add_course, add_marks], outputs=add_output)
        
    with gr.Tab("Update Student"):
        gr.Markdown("*(Updates a student based on their Name)*")
        update_name = gr.Textbox(label="Name")
        update_course = gr.Textbox(label="New Course")
        update_marks = gr.Number(label="New Marks")
        update_btn = gr.Button("Update")
        update_output = gr.Textbox(label="Result")
        update_btn.click(update_student, inputs=[update_name, update_course, update_marks], outputs=update_output)
        
    with gr.Tab("Delete Student"):
        delete_name = gr.Textbox(label="Name to Delete")
        delete_btn = gr.Button("Delete", variant="stop")
        delete_output = gr.Textbox(label="Result")
        delete_btn.click(delete_student, inputs=[delete_name], outputs=delete_output)

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860)
