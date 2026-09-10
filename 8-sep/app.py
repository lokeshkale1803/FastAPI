'''wap to create student management system which will consist of 
1.to create stud id
2.to read stud id
3.to delete stud id
4.to update stud id'''

'''student={}

while true:
    print("1.crate stud id")
    print("2.read stud id")
    print("3.delete stud id")
    print("4.update stud id")
    
    choise=int(input("Enter your choise between 1-4:"))
    
    
        
        
    choice == "1":
    id = input("Enter Student ID: ")
        if id in students:
            print("ID already exists!")
        else:
            name = input("Enter Name: ")
            students[id] = name
            print("Student added successfully.")
            
            
  
    elif choise==2:
        id=int(input("Enter stud id:"))
        if id in student:
            print(f"stud name is {student[id]}")
        else:
            print("stud id not found")
    
    else:
        print("invalid choise")
    '''

import gradio as gr

students = {}   # Empty dictionary

def create_stud_id(id, name):
    id = int(id)
    students[id] = name
    return "Student ID created successfully.", str(students)

def read_stud_id():
    return str(students)


def delete_stud_id(id):
    id = int(id)
    if id in students:
        del students[id]
        return "Student ID deleted successfully.", str(students)
    else:
        return "Student ID not found.", str(students)


def update_stud_id(id, name):
    id = int(id)
    if id in students:
        students[id] = name
        return "Student ID updated successfully.", str(students)
    else:
        return "Invalid Student ID.", str(students)


# =========================
# GRADIO UI
# =========================

with gr.Blocks() as demo:

    gr.Markdown("# 🎓 Student Management System")

    # Inputs
    student_id = gr.Textbox(label="Student ID")
    student_name = gr.Textbox(label="Student Name")

    # Buttons
    create_btn = gr.Button("Create Student")
    read_btn = gr.Button("Show Students")
    update_btn = gr.Button("Update Student")
    delete_btn = gr.Button("Delete Student")

    # Outputs
    message = gr.Textbox(label="Message")
    student_data = gr.Textbox(label="Students")


    # CREATE
    create_btn.click(
        fn=create_stud_id,
        inputs=[student_id, student_name],
        outputs=[message, student_data]
    )


    # READ
    read_btn.click(
        fn=read_stud_id,
        inputs=[],
        outputs=student_data
    )


    # UPDATE
    update_btn.click(
        fn=update_stud_id,
        inputs=[student_id, student_name],
        outputs=[message, student_data]
    )


    # DELETE
    delete_btn.click(
        fn=delete_stud_id,
        inputs=student_id,
        outputs=[message, student_data]
    )


demo.launch()