def task():
    tasks = [] #Empty list of tasks
    print("\n -------------- Welcome to Task Manager App ---------------")

    total_tasks = int(input("Enter how many tasks you want to add : "))
    for i in range (1, total_tasks+1):
        task_name = input(f"Enter task {i} : ")
        tasks.append(task_name)  # Adds tasks to the list

    print(f"Today's tasks are\n{tasks}")
    while True:
        operation = int(input("Enter :\n1-Add task\n2-Update task\n3-Delete task\n4-View tasks\n5-Exit task manager\n >>> "))
        if operation == 1:
            new_task = input("Enter task you want to add : ")
            tasks.append(new_task)               #Adds new task to the list
            print(f"Task {new_task} has been added sucessfully...")

        elif operation == 2:
            task_update = input("Enter task you want to update: ")
            if task_update in tasks:
                update = input("Enter new task : ")
                ind = tasks.index(task_update) #Gives the indexing value in list
                tasks[ind] = update            # Updates the tasks list
                print(f"Updated task {update}")

        elif operation == 3:
            task_delete = input("Enter task you want to delete : ")
            if task_delete in tasks:
                ind = tasks.index(task_delete)
                del tasks[ind]                      # Deletes the task entered by the user
                print(f"Task {task_delete} has been deleted successfully...")

        elif operation == 4:
            print(f"Todays tasks are {tasks}") #Prints the tasks list

        elif operation == 5:
            print("Closing Task manager...")
            break   #Loop ends and the program gets closed
        else:
            print("Invalid Input !!")
task()
