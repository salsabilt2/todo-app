import functuns
import PySimpleGUI as sg

label = sg.Text("Type In a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functuns.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functuns.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break



window.close()