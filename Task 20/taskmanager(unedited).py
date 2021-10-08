# This python program helps to manage tasks assigned to each member of the team
# for a small business.

# Request for login details
user = input("Enter Username:\n")
password = input("Enter password:\n")

# Create a login control variable
access_gained = False

# Validate login details
with open('user.txt', 'r+', encoding='utf-8') as user_file:
    for line in user_file:
        if (line.strip('\n').split(', ')[0] == user) and (line.strip('\n').split(', ')[1] == password):
            access_gained = True

# Keep asking for valid username and password if wrong
while not access_gained:
    print("\nError, please enter a valid username and/password\n")

    user = input("Enter Username:\n")
    password = input("Enter password:\n")

    with open('user.txt', 'r+', encoding='utf-8') as user_file:
        for line in user_file:
            if (line.strip('\n').split(', ')[0] == user) and (line.strip('\n').split(', ')[1] == password):
                access_gained = True

# Allow access if username and password is correct
if access_gained:
    print("\nPlease select one of the following options:")
    print("r - register user \na - add task \nva - view all tasks \nvm - view my tasks \ne - exit")
    choice = input()

    # REGISTER NEW USER
    if choice == 'r':
        new_user = input("Enter username you wish to register:\n")
        new_password = input("Enter password you wish to register:\n")
        confirm_password = input("Please confirm password:\n")

        # Check that the passwords match
        while confirm_password != new_password:
            print("Passwords do not match, please try again. Please confirm password")
            confirm_password = input("Please confirm password:\n")

        if new_password == confirm_password:
            user_file = open('user.txt', 'a', encoding='utf-8')
            user_file.write('\n' + new_user + ', ' + new_password)
            user_file.close()
            print(f"You have registered {new_user} as a user.")

    # ADD A NEW TASK
    elif choice == 'a':
        # Learnt how to use the 'date' class, module and object here
        # https://www.programiz.com/python-programming/datetime/current-datetime
        from datetime import date
        name = input('Enter the name of person task is assigned to:\n')
        title = input("Enter the title of the task:\n")
        description = input("Enter the description of the task:\n")
        due_date = input("Enter the due date of the task: \n")
        today_date = date.today()
        # Convert date object to a string
        t_date = today_date.strftime("%d %b %Y")
        completed = 'No'
        # append task data to a list, convert the list to a string and save to the tasks.txt file
        tasks = [name, title, description, t_date, due_date, completed]
        with open('tasks.txt', 'a', encoding='utf-8') as task_file:
            task_file.writelines('\n'+", ".join(tasks))
        print("done")

    # VIEW ALL TASKS
    elif choice == 'va':
        # Create a list of outputs
        output = ['Assigned to:', 'Task:', 'Task Description:', 'Date assigned:', 'Due date:', 'Task complete?']

        with open('tasks.txt', 'r', encoding='utf-8') as task_file:
            for line in task_file:
                print("----------------------------------------------------------------------------------------")
                for cat in output:
                    # Get the index of the output in the list and match it with the data in the task file
                    # Learnt how to use the index method here: https://www.w3schools.com/python/ref_list_index.asp
                    index = output.index(cat)
                    data = line.split(', ')[index]

                    # Learnt how to use the "ljust" method here:
                    # https://www.programiz.com/python-programming/methods/string/ljust
                    # The "ljust" method returns the left-justified string within the given minimum width
                    print(f"{cat.ljust(30)} {data}")

    # VIEW ALL MY TASKS
    elif choice == 'vm':
        # Create a boolean variable
        user_found = False
        with open('tasks.txt', 'r', encoding='utf-8') as task_file:
            for line in task_file:
                # if the user has been assigned tasks, display such tasks
                if user in line.split(','):
                    user_found = True
                    output = ['Assigned to:', 'Task:', 'Task Description:', 'Date assigned:', 'Due date:',
                              'Task complete?']
                    print("-------------------------------------------------------------------------------------")
                    for cat in output:
                        index = output.index(cat)
                        data = line.split(', ')[index]

                        print(f"{cat.ljust(30)} {data}")

            # Display a message if the user has not been assigned any tasks
            if not user_found:
                print("\nOOps, you have not been assigned any tasks.")

    # EXIT PROGRAM
    elif choice == 'e':
        # Learnt how to use the sys module to exit a program here
        # https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/
        import sys
        sys.exit("\nExiting.............\nThank you for using the task manager")
