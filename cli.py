import functuns
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functuns.get_todos()

        todos.append(todo + '\n')

        functuns.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functuns.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functuns.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functuns.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functuns.get_todos()

            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            functuns.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with this number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command not valid.")
print("Bye!")
