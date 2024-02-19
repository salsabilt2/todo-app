import functuns
import PySimpleGUI as sg

label = sg.Text("Type In a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functuns.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("complete")
exit_button = sg.Button("Exit")
window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["todos"])
    match event:
        case "Add":
            todos = functuns.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functuns.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functuns.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functuns.write_todos(todos)
            window["todos"].update(values=todos)
        case "complete":
            todo_to_complete = values["todos"][0]
            todos = functuns.get_todos()
            todos.remove(todo_to_complete)
            functuns.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sg.WINDOW_CLOSED:
            break



window.close()