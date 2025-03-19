import tasks

task = input("What is a task you want to add?: ")
taskList.append(task)
print(taskList)
while input == "add" or "remove":
    choice = input("Would you like to add or remove a task?: ")
    if choice == "add":
        task = input("What do you want to add?: ")
        taskList.append(task)
        print(taskList)
    elif choice == "remove":
        task = input("What do you want to remove?: ")
        taskList.remove(task)
        print(taskList)
    else:
        break
