
# Start

#======importing libraries======

from datetime import datetime
import datetime

import inspect


#=========Login Section=========

print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

# open the files and read the lines
user_read = open("user.txt", "r")
user_lines = user_read.readlines()
tasks_read = open("tasks.txt", "r")
tasks_lines = tasks_read.readlines()

# empty lists to store the usernames and passwords
usernames = []
passwords = []

# formulate the lists of usernames and passwords
username = [line.split()[0].strip(", ") for line in user_lines]
usernames += username
password = [line.split()[1] for line in user_lines]
passwords += password

number_of_users = 0

for line in user_read:
    number_of_users += 1

# while loop to input the correct username/s and password/s
while True:
    login = input("Enter 'username, password': ")

    if login == "":

        print("\nInvalid input, try again.\n")
        continue

    if len(login.split()) == 1:

        print("\nInvalid input, try again.\n")
        continue

    user_input = login.split(", ")[0]
    pass_input = login.split()[1]

    # for loop to find out which username is logging in
    for i in range(len(usernames)):
        if username[i] == user_input:
            acc_no = i
            user_pass = (f"{username[acc_no]}, {password[acc_no]}")
            break

        else:
            acc_no = 0

    # still checking the right username/s and pasword/s input is correct
    if login == (f"{username[acc_no]}, {password[acc_no]}"):

        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
        print(f"Welcome {usernames[acc_no]}! ")
        break

    elif "," not in login:

        print("\nThe comma is missing.\n")
        continue

    elif user_input not in usernames:

        print("\nIncorrect username, try again.\n")
        continue

    elif username[acc_no] in login:

        print("\nIncorrect password, try again.\n")
        continue

    else:

        print("\nLogin information incorrect, try again.\n")
        continue

print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")


#===========Functions===========

def this_is(var):
    print(var, "=", eval(var))

def reg_user():

    # conditional to allow only 'admin' to register new users
    if user_input == "admin":

        while True:
            admin_choice = input("Enter 'users' to show the names of and how many users, 'new' to register a user or 'exit' to exit: ").lower()

            # open and read data in the file
            user_read = open("user.txt", "r")
            user_lines = user_read.readlines()

            # empty list for storing the username/s
            usernames = []

            # copying the username/s algorithm for new registered users and formulate the list again
            username = [line.split()[0].strip(", ") for line in user_lines]
            usernames += username

            number_of_users = 0

            # calculate the total number of users registered
            for line in user_lines:
                number_of_users += 1

            if admin_choice == "exit":
                break

            # display to 'admin' how many users are registered within the file
            elif admin_choice == "users":

                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                print(f"There are {number_of_users} users registered.\n")
                print(f"The registered users are: {usernames}")
                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                continue

            elif admin_choice == "new":

                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

                # while loop to check if new username is free or not
                while True:
                    new_user = input("Enter a new username or 'exit' to exit: ").lower()

                    print("")

                    if new_user == "exit":

                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                        break

                    # conditional to make sure a valid input is entered
                    if new_user == "":

                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                        print("Invalid input.")
                        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                        continue

                    if new_user in usernames:

                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                        print("Username already in use, try a different username.")
                        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                        continue

                    else:
                        # while loop to enter the new password and confirm it
                        while True:
                            new_pass = input("Enter a password: ")

                            # conditional to make sure a valid input is entered
                            if new_pass == "":

                                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                print("Invalid input.")
                                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                continue

                            else:
                                new_pass_confirm = input("Confirm the password: ")

                            # conditional to make sure the password/s match
                            if new_pass_confirm == new_pass:

                                # open the file and write the new username/s and password/s under the previous
                                with open("user.txt", "a") as user_write:
                                    user_write.write(f"\n{new_user}, {new_pass}")
                                break

                            else:
                                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                print("The passwords do not match, try again.")
                                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                continue

                        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                        print("New user added successfully. ")
                        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                        break

            else:
                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                print("Invalid input, try again. ")
                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                continue

        # close the file
        user_read.close()

        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
        print("End of Registering a User. ")
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    else:
        print("Access 'admin' specific. ")
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

def add_task():

    # open the files to review any new users or tasks
    user_read = open("user.txt", "r")
    user_lines = user_read.readlines()
    tasks_read = open("tasks.txt", "r")
    tasks_lines = tasks_read.readlines()

    # empty list to store the username/s
    usernames = []

    # repeating the username/s algorithm for any new registered users to formulate the list again
    username = [line.split()[0].strip(", ") for line in user_lines]
    usernames += username

    while True:
        # adding a task menu to exit when needed
        add_choice = input("Enter 'add' to add a new task or 'exit' to exit: ").lower()

        if add_choice == "exit":
            break

        if add_choice == "add":

            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

            # check to see if the user the task is being assigned to is registered inside the file
            while True:
                task_user = input("Enter the username the task is assigned to or 'exit' to exit: ")

                if task_user == "exit":
                    break

                if task_user not in usernames:

                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                    print("Unknown user, try again.")
                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                    continue

                # inputs for the all the variables needed for the assigned task/s
                task_title = input("Enter the title of the task: ")
                task_description = input("Enter the description of the task: ")
                # assigned date == current date
                current_date = datetime.datetime.today()

                # while loop to error check the due date
                while True:
                    due_date = input("Enter the due date of the task: ")

                    # defensive programming and error handling to check the format of the date entered
                    try:
                        due_date = datetime.datetime.strptime(due_date, "%d/%m/%Y")

                    except ValueError:

                        try:
                            due_date = datetime.datetime.strptime(due_date, "%d %b %Y")

                        except ValueError:

                            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                            print("Invalid date format, use dd/mm/YYYY or dd Mmm YYYY")
                            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                            continue

                    if due_date < current_date:

                        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                        print("The due date has already passed, choose a future date.")
                        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                        continue

                    else:
                        # remove the 00:00:00 and being written into the file
                        due_date = due_date.strftime("%d/%m/%Y")
                        break

                task_completion = "No\n"

                # open the file to add new tasks into the file
                with open("tasks.txt", "a") as tasks_write: 
                    # write the new task/s as a string into the file under the previous task/s
                    tasks_write.write(str(f"{task_user}, {task_title}, {task_description}, {current_date:%d/%m/%Y}, {due_date}, {task_completion}"))

                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                print("Task added successfully. ")
                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

                # close the files
                user_read.close()
                tasks_read.close()

                break

        else:
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
            print("Invalid input, try again. ")
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
            continue

    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    print("End of Adding a Task. ")
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

def view_all():

    # conditional to allow only 'admin' to view all tasks
    if user_input == "admin":
        # open the files to review any new users or tasks
        user_read = open("user.txt", "r")
        user_lines = user_read.readlines()
        tasks_read = open("tasks.txt", "r")
        tasks_lines = tasks_read.readlines()

        # empty list to re-store the username/s
        usernames = []

        # copying the username/s algorithm for new registered users and formulate the list again
        username = [line.split()[0].strip(", ") for line in user_lines]
        usernames += username

        # empty list for each task assigned to certain users
        pos_list = []

        # calculate how many total tasks are in the file
        number_of_lines = 0

        for line in tasks_lines:
            number_of_lines += 1

        print(f"There are {number_of_lines} total tasks.\n")

        # to number the lines and tasks from the file
        for pos, line in enumerate(tasks_lines, 1):
            pos_list.append(int(pos))
            tasks_split = line.split(", ")
            # only print output if there are tasks assigned avaliable
            if number_of_lines == 0:
                break

            else:
                output = (f"-=-=-=-=-=-=-=-=-=-[Task {pos}]-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n")
                output += (f"Task:\t\t   {tasks_split[1]}\n")
                output += (f"Assigned to:\t   {tasks_split[0]}\n")
                output += (f"Date Assigned:\t   {tasks_split[3]}\n")
                output += (f"Due Date:\t   {tasks_split[4]}\n")
                output += (f"Task Complete?:\t   {tasks_split[5]}")
                output += (f"Task Description:  {tasks_split[2]}\n")

                print(output)

        # conditional to print or not if there 0 tasks avaliable or not    
        if number_of_lines != 0:

            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

            # while loop to interact with the numbered tasks
            while True:
                # again to not interact unless there is a task avaliable
                if number_of_lines == 0:
                    break

                try:
                    # asks admin which task to select
                    tasks_number = input("Select which task number you want to modify or enter '0' to exit: ")

                    print("")

                    if tasks_number == "exit":
                        break

                    else:
                        tasks_number = int(tasks_number)

                    # splitting the chosen task into sections
                    edit_task = tasks_lines[(tasks_number - 1)]
                    split_task = edit_task.split(", ")

                    if tasks_number == 0:
                        break

                    if type(tasks_number) != int:

                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                        print("Invalid input, try again. ")
                        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                        continue

                    # conditional to make sure an avaliable task is chosen
                    if int(tasks_number) not in pos_list:

                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                        print("Invalid task, try again. ")
                        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                        continue

                    if int(tasks_number) > len(tasks_lines) or int(tasks_number) < 0:

                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                        print("Invalid task, try again. ")
                        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                        continue

                    else:
                        while True:
                            # admin menu to offer choices that modify the chosen task
                            tasks_choice = input("Enter 'edit' to edit the task, 'complete' to mark as complete or 'exit' to exit: ").lower()

                            print("")

                            if tasks_choice == "exit":

                                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                break

                            # conditionals for the choice input
                            if tasks_choice == "edit":
                                edit_task_choice = input("Enter 'user' to change the assigned username, 'date' to change the due date or 'exit' to exit: ").lower()

                                print("")

                                if edit_task_choice == "exit":

                                    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                    break

                                if edit_task_choice == "user":

                                    while True:
                                        edit_task_user = input("Enter the username you want to assign this task to or enter 'exit' to exit: ")

                                        print("")

                                        if edit_task_user == "exit":

                                            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                            break

                                        if edit_task_user == "":

                                            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                            print("Invalid input, try again. ")
                                            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                            continue

                                        # make sure the user inputted is already registered
                                        if edit_task_user not in usernames:

                                            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                            print("Invalid username, try again. ")
                                            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                            continue

                                        # editing the username in the chosen task and line
                                        if edit_task_user in usernames:
                                            split_task[0] = edit_task_user
                                            changed_user = ", ".join(split_task)

                                            with open("tasks.txt", "r") as tasks_read:
                                                user_line = tasks_read.readlines()
                                                user_line[(tasks_number - 1)] = changed_user

                                            # write the new username into the file
                                            with open("tasks.txt", "r+") as tasks_write:
                                                tasks_write.writelines(user_line)

                                            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                            print(f"Task {tasks_number}'s user changed. ")
                                            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                            break

                                        else:

                                            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                            print("Invalid input, try again. ")
                                            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                            continue

                                    break

                                if edit_task_choice == "date":

                                    while True:
                                        new_date = input("Enter the new due date or 'exit' to exit: ")

                                        print("")

                                        if new_date == "exit":

                                            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                            break

                                        else:
                                            current_date = datetime.datetime.today()

                                            # defensive programming and error handling to check the format of the date entered
                                            try:
                                                new_date = datetime.datetime.strptime(new_date, "%d/%m/%Y")

                                            except ValueError:

                                                try:
                                                    new_date = datetime.datetime.strptime(new_date, "%d %b %Y")

                                                except ValueError:

                                                    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                                    print("Invalid date format, use dd/mm/YYYY or dd Mmm YYYY")
                                                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                                    continue

                                            # conditional to check if the date has passed or not
                                            if new_date < current_date:

                                                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                                print("The due date has already passed, choose a future date.")
                                                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                                continue

                                            else:
                                                # remove the 00:00:00 and being written into the file
                                                new_date = new_date.strftime("%d/%m/%Y")
                                                # editing the date in the chosen task and line
                                                split_task[-2] = new_date
                                                changed_date = ", ".join(split_task)

                                                with open("tasks.txt", "r") as tasks_read:
                                                    date_line = tasks_read.readlines()
                                                    date_line[(tasks_number - 1)] = changed_date

                                                # write the new date into the file
                                                with open("tasks.txt", "r+") as tasks_write:
                                                    tasks_write.writelines(date_line)

                                                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                                print(f"Task {tasks_number}'s due date changed. ")
                                                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                                break

                                else:
                                    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                    print("Invalid input, try again. ")
                                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                    continue

                                break

                            if tasks_choice == "complete":
                                edit_tasks = tasks_lines[(tasks_number - 1)]
                                split_tasks = edit_tasks.split(", ")

                                # only allow uncompleted tasks to be marked as complete
                                if split_tasks[-1] == "Yes\n":

                                    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                    print("This task is already complete, chose another task to edit. ")
                                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                    break

                                else:
                                    # changing the completion of the chosen task
                                    split_tasks[-1] = "Yes\n"
                                    complete_tasks = ", ".join(split_tasks)
                                    
                                    # implement the new line
                                    with open("tasks.txt", "r") as tasks_read:
                                        tasks_line = tasks_read.readlines()
                                        tasks_line[(tasks_number - 1)] = complete_tasks

                                    # write the new line into the file
                                    with open("tasks.txt", "r+") as tasks_write:
                                        tasks_write.writelines(tasks_line)

                                    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                    print(f"Task {tasks_number} has been marked as complete. ")
                                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                    break

                            else:

                                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                print("Invalid input, try again.")
                                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                continue

                except ValueError:

                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                    print("Invalid input, try again.")
                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                    continue

                except IndexError:

                    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                    print("Invalid task, try again.")
                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                    continue

                except TypeError:

                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                    print("Invalid input, try again.")
                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                    continue

        if number_of_lines != 0:

            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

        if number_of_lines == 0:

            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

        # close the files
        user_read.close()
        tasks_read.close()

    else:

        print("Information 'admin' specific. ")
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    print("End of View All Tasks. ")
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

def view_mine():

    # open the files and read the data
    user_read = open("user.txt", "r")
    user_lines = user_read.readlines()
    tasks_read = open("tasks.txt", "r")
    tasks_lines = tasks_read.readlines()

    # empty list for the assigned personal task/s of each user
    pos_list = []

    # calculate the total number of personal tasks for the user
    my_number_task = 0

    for line in tasks_lines:
        num_word = line.split()
        if num_word[0].strip(", ") == user_input:
            my_number_task += 1

    print(f"You have {my_number_task} task/s avaliable.\n")

    # calculate the number to assign each task
    my_task_number = 0

    # to number each line and task from the file
    for pos, line in enumerate(tasks_lines, 1):
        word = line.split(", ")
        # per user task condtional
        if word[0].strip(", ") == user_input:
            pos_list.append(int(pos))
            my_task_number += 1
            my_task_split = line.split(", ")

            # only print output if there are tasks assigned avaliable
            if my_task_number == 0:
                break

            else:
                output = (f"-=-=-=-=-=-=-=-=-=-[Task {pos}]-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n")
                output += (f"Task:\t\t   {my_task_split[1]}\n")
                output += (f"Assigned to:\t   {my_task_split[0]}\n")
                output += (f"Date Assigned:\t   {my_task_split[3]}\n")
                output += (f"Due Date:\t   {my_task_split[4]}\n")
                output += (f"Task Complete?:\t   {my_task_split[5]}")
                output += (f"Task Description:  {my_task_split[2]}\n")

                print(output)

    # conditional to print or not if there 0 tasks avaliable or not   
    if my_task_number != 0:

        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    while True:
        # again to not interact unless there is a task avaliable
        if my_task_number == 0:
            break

        try:
            # ask the user which task to select
            my_task_choice = input("Select which task number you want to modify or enter '0' to exit: ")

            print("")

            if my_task_choice == "exit":
                break

            my_task_choice = int(my_task_choice)

            # splitting the chosen task into sections
            edit_line = tasks_lines[(my_task_choice - 1)]
            split_line = edit_line.split(", ")

            if my_task_choice == 0:
                break

            if type(my_task_choice) != int:

                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                print("Invalid input, try again. ")
                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                continue

            # conditional to make sure an avaliable task is chosen
            if my_task_choice not in pos_list:

                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                print("Invalid task, try again. ")
                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                continue

            if my_task_choice > pos or my_task_choice < 0:

                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                print("Invalid input, try again. ")
                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                continue

            else:
                # only interact with incomplete tasks
                if split_line[-1] != "Yes\n":

                    while True:
                        # choices to modify the chosen task number
                        my_choice = input("Enter 'edit' to edit the task, 'complete' to mark as complete or 'exit' to exit: ").lower()

                        print("")

                        if my_choice == "exit":
                            break

                        # conditionals for the choice input
                        if my_choice == "edit":
                            edit_choice = input("Enter 'user' to change the assigned username, 'date' to change the due date or 'exit' to exit: ").lower()

                            print("")

                            if edit_choice == "exit":
                                break

                            if edit_choice == "user":

                                while True:
                                    edit_user = input("Enter the username you want to assign this task to or enter 'exit' to exit: ")

                                    print("")

                                    if edit_user == "exit":

                                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                        break

                                    if edit_user == "":

                                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                        print("Invalid input, try again. ")
                                        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                        continue

                                    # make sure the user inputted is already registered
                                    if edit_user not in usernames:

                                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                        print("Invalid username, try again. ")
                                        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                        continue

                                    # editing the username in the chosen task and line
                                    if edit_user in usernames:
                                        split_line[0] = edit_user
                                        change_user = ", ".join(split_line)

                                        with open("tasks.txt", "r") as my_tasks_read:
                                            user_mine = my_tasks_read.readlines()
                                            user_mine[(my_task_choice - 1)] = change_user

                                        # write the new username into the file
                                        with open("tasks.txt", "r+") as my_task_write:
                                            my_task_write.writelines(user_mine)

                                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                        print(f"Task {(my_task_choice)}'s user changed. ")
                                        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                        break

                                    else:

                                        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                        print("Invalid input, try again. ")
                                        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                        continue

                                break

                            if edit_choice == "date":

                                while True:
                                    my_new_date = input("Enter the new due date or enter 'exit' to exit: ")

                                    print("")

                                    if my_new_date == "exit":

                                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                        break

                                    else:
                                        my_current_date = datetime.datetime.today()

                                        # defensive programming and error handling to check the format of the date entered
                                        try:
                                            my_new_date = datetime.datetime.strptime(my_new_date, "%d/%m/%Y")

                                        except ValueError:

                                            try:
                                                my_new_date = datetime.datetime.strptime(my_new_date, "%d %b %Y")

                                            except ValueError:

                                                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                                print("Invalid date format, use dd/mm/YYYY or dd Mmm YYYY")
                                                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                                continue

                                        # conditional to check if the date has passed or not
                                        if my_new_date < my_current_date:

                                            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                            print("That date has already passed, choose a future date.")
                                            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                            continue

                                        else:
                                            # remove the 00:00:00 and being written into the file
                                            my_new_date = my_new_date.strftime("%d/%m/%Y")
                                            # editing the date in the chosen task and line
                                            split_line[-2] = my_new_date
                                            changed_date = ", ".join(split_line)

                                            with open("tasks.txt", "r") as my_task_read:
                                                date_line = my_task_read.readlines()
                                                date_line[(my_task_choice-1)] = changed_date

                                            # write the new date into the file
                                            with open("tasks.txt", "r+") as my_task_write:
                                                my_task_write.writelines(date_line)

                                            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                            print(f"Task {my_task_choice}'s due date changed. ")
                                            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                            break

                                break

                            else:

                                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                print("Invalid input, try again. ")
                                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                continue

                        if my_choice == "complete":

                            # only allow uncompleted tasks to be edited
                            if split_line[-1] == "Yes\n":

                                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                print("This task is already complete and cannot be edited, chose another task to edit. ")
                                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                continue

                            else:
                                # replacing the last word in the task ("No\n") with "Yes\n"
                                split_line[-1] = "Yes\n"
                                new_line = ", ".join(split_line)

                                # implement the new line
                                with open("tasks.txt", "r") as my_task_read:
                                    task_line = my_task_read.readlines()
                                    task_line[(my_task_choice - 1)] = new_line

                                # write the new line into the file
                                with open("tasks.txt", "r+") as my_task_write:
                                    my_task_write.writelines(task_line)

                                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                print(f"Task {(my_task_choice)} has been marked as complete. ")
                                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                                break

                        else:

                            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                            print("Invalid input, try again.")
                            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                            continue

                else:

                    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                    print("This task is already complete and cannot be edited, chose another task to edit. ")
                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                    continue

        except ValueError:

            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
            print("Invalid input, try again.")
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
            continue

        except IndexError:

            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
            print("Invalid task, try again.")
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
            continue

        except TypeError:

            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
            print("Invalid input, try again.")
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
            continue

    # close the files
    user_read.close()
    tasks_read.close()

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    print("End of View My Task/s. ")
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

def generate_tasks():

    """
    This function generates the files "user_overview.txt" and "task_overview.txt" only if they don't exist in
    the first place, ready for the statistics to be written, read and outputted from without modifying the file.
    """

    open("task_overview.txt", "x").close()
    open("user_overview.txt", "x").close()

def generate_reports():

    """
    This Funtion is to be run by 'admin' only and will generate a report based on the data in 
    "user.txt" and "tasks.txt" and calculates statistics about the tasks and for each user which
    are then written to "user_overview.txt" and "task_overview.txt", ready to be outputted.
    """
    
    # conditional for the admin only
    if user_input == "admin":

        while True:
            # error handling to check if the files exist
            try:
                with open("task_overview.txt", "r") as task_overview, open("user_overview.txt", "r") as user_overview:
                    # open the files
                    user_read = open("user.txt", "r")
                    user_lines = user_read.readlines()
                    tasks_read = open("tasks.txt", "r")
                    tasks_lines = tasks_read.readlines()

                    # empty integer based variables
                    total_tasks = 0
                    completed_num = 0
                    incomplete_num = 0
                    incomplete_overdue_num = 0

                    # today's date as a variable
                    today = datetime.datetime.today()

                    for line in tasks_lines:
                        total_tasks += 1

                    # calculating the amount of complete and incomplete tasks
                    for line in tasks_lines:
                        if line.split(", ")[-1] == "Yes\n":
                            completed_num += 1

                        elif line.split(", ")[-1] == "No\n":
                            incomplete_num += 1

                            # calculating the overdue tasks and formulating the correct dates
                            if "/" in line.split(", ")[-2]:
                                date = datetime.datetime.strptime(line.split(", ")[-2], "%d/%m/%Y")

                            else:
                                date = datetime.datetime.strptime(line.split(", ")[-2], "%d %b %Y")

                            if date < today:
                                incomplete_overdue_num += 1

                    incomplete_perc = round((incomplete_num/total_tasks) * 100, 2)
                    overdue_perc = round((incomplete_overdue_num/total_tasks) * 100, 2)

                    # write the statistics to the task overview file
                    with open("task_overview.txt", "w") as task_overview_write:
                        task_overview_write.write(str(f"There are {total_tasks} total task/s.\n"))
                        task_overview_write.write(str(f"There are {completed_num} task/s completed.\n"))
                        task_overview_write.write(str(f"There are {incomplete_num} task/s uncompleted.\n"))
                        task_overview_write.write(str(f"There are {incomplete_overdue_num} task/s that are incomplete and overdue.\n"))
                        task_overview_write.write(str(f"There are {incomplete_perc}% of tasks are incomplete.\n"))
                        task_overview_write.write(str(f"There are {overdue_perc}% of tasks are overdue.\n"))

                    # empty list to re-store the username/s
                    usernames = []

                    # copying the username/s algorithm for new registered users and formulate the list again
                    username = [line.split()[0].strip(", ") for line in user_lines]
                    usernames += username

                    # empty dictionaries
                    username_tasks = {}
                    username_completed = {}
                    username_incomplete = {}
                    username_incomplete_overdue = {}

                    number_of_tasks = 0

                    # today's date as a variable
                    today = datetime.datetime.today()

                    for line in tasks_lines:
                        number_of_tasks += 1
                        
                        # condtionals to formulate the statistics of the usernames and their tasks
                        for username in usernames:
                            if line.split(", ")[0] == username:
                                username_tasks[username] = username_tasks.get(username, 0) + 1
                                # print(username, username_tasks)

                            else:
                                if username in username_tasks:
                                    pass

                                # for any usernames with 0 tasks to be assigned to the dictionaries
                                else:
                                    username_tasks[username] = 0

                            # getting completed tasks of each username
                            if line.split(", ")[0] == username and line.split(", ")[-1] == "Yes\n":
                                username_completed[username] = username_completed.get(username, 0) + 1

                            else:
                                if username in username_completed: 
                                    pass

                                else:
                                    username_completed[username] = 0

                            # getting incomplete tasks of each username
                            if line.split(", ")[0] == username and line.split(", ")[-1] == "No\n":
                                username_incomplete[username] = username_incomplete.get(username, 0) + 1

                                # formulating the correct dates of the tasks
                                if "/" in line.split(", ")[-2]:
                                    date = datetime.datetime.strptime(line.split(", ")[-2], "%d/%m/%Y")

                                else:
                                    date = datetime.datetime.strptime(line.split(", ")[-2], "%d %b %Y")

                                if date < today:
                                    username_incomplete_overdue[username] = username_incomplete_overdue.get(username, 0) + 1

                                else:
                                    if username in username_incomplete_overdue:
                                        pass

                                    # for any usernames with 0 tasks to be assigned to the dictionaries
                                    else:
                                        username_incomplete_overdue[username] = 0

                            else:
                                if username in username_incomplete:
                                    pass

                                # for any usernames with 0 tasks to be assigned to the dictionaries
                                else:
                                    username_incomplete[username] = 0
                                    username_incomplete_overdue[username] = 0
                    
                    

                    # write the statistics to the task overview file
                    with open("user_overview.txt", "w") as user_overview_write:
                        for username in usernames:
                            user_overview_write.writelines(str(f"\033[4mUser: {username}\033[0m\n")) 
                            user_overview_write.writelines(str(f"User {username} has {username_tasks[username]} task/s assigned to them.\n"))
                            user_overview_write.writelines(str(f"User {username} has {round((username_tasks[username] / number_of_tasks) * 100, 2)}% of the total task/s assigned.\n"))

                            # for any usernames with 0 tasks add 1 to the total tasks to not affect the percentages
                            if username_tasks[username] == 0:
                                username_tasks[username] = 1

                            else:
                                pass

                            user_overview_write.writelines(str(f"User {username} has completed {round((username_completed[username] / username_tasks[username]) * 100, 2)}% of tasks assigned to them.\n"))
                            user_overview_write.writelines(str(f"User {username} has {round((username_incomplete[username] / username_tasks[username]) * 100, 2)}% of tasks assigned to them incomplete.\n"))
                            user_overview_write.writelines(str(f"User {username} has {round((username_incomplete_overdue[username] / username_tasks[username]) * 100, 2)}% of tasks assigned to them incomplete and overdue.\n"))
                            user_overview_write.writelines(str("\n"))

                    print("Reports have been generated. ")
                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

                    # close the files
                    user_read.close()
                    tasks_read.close()

                    print("End of Generate Reports. ")
                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                    break

            except FileNotFoundError:
                generate_tasks()
                continue

    else:

        print("User 'admin' access specific. ")
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

def display_statistics():

    """
    This function requires only admin to print statistics of the data in the user and tasks files from the 
    "user_overview.txt" and "task_overview.txt" files and uses defensive programming to handle any errors.
    """

    if user_input == "admin":

        # error handling to check if the files exist and create them if otherwise
        try:
            with open("task_overview.txt", "r") as open_task_overview_read:
                read_task_lines = open_task_overview_read.readlines()
                
                # print the statistics in order
                for line in read_task_lines:

                    print(line.strip("\n"))

                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

        except FileNotFoundError:

            print("'task_overview.txt' file not found, generate a report first. ")
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

        try:
            with open("user_overview.txt", "r") as open_user_overview_read:
                read_user_lines = open_user_overview_read.readlines()

                # print the statistics in order
                for line in read_user_lines:

                    print(line.strip("\n"))

                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

        except FileNotFoundError:

            print("'user_overview.txt' file not found, generate a report first. ")
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

        print("End of Display Statistics. ")
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    else:

        print("User 'admin' access specific. ")
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")


while True:
    menu = input('''Select one of the following Options below:

r - Registering a User
a - Adding a Task
va - View All Tasks
vm - View My Task/s
gr - Generate Reports
ds - Display Statistics
e - Exit
: ''').lower()

    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    if menu == 'r':
        pass

        reg_user()


    elif menu == 'a':
        pass

        add_task()


    elif menu == 'va':
        pass

        view_all()


    elif menu == 'vm':
        pass

        view_mine()


    elif menu == 'gr':
        pass

        generate_reports()


    elif menu == 'ds':
        pass

        display_statistics()


    elif menu == 'e':

        print('Goodbye!!!')
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

        # close the files
        user_read.close()
        tasks_read.close()

        exit()


    else:

        print("You have made a wrong choice, please try again. ")
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")


# Stop