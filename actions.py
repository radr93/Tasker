# Import Modules

# [MODULE NAME]     Actions.py
#
# [MODULE SUMMARY]
# This module is used to handle the Tasker Action Menu (TAM).
#
# The TAM is managed by one class - "Action", that contains the following methods:
#
#   get_action():
#       Prompt the user for an action (i.e. [View, Add, Remove, Send, Exit]) to interact with the tasklist.
#
#   perform_action(action):
#       Perform actions associated with a variable passed as an argument that stores the return value from get_action().
#
#   view_tasklist():
#       Print all tasks in the tasklist.txt file or creates the file if it doesn't exist yet.
#
#   new_task(name):
#       Add a new task to the tasklist.txt file.
#
#   remove_task(name):
#       Remove a task from the tasklist.txt file.


# Create the Action class
class Action:

    # Create the get_action method
    def get_action():

        # [SYNTAX]: action = Action.get_action()
        #
        # [ARGUMENTS]:
        # This method takes no arguments.
        #
        # [SUMMARY]:
        # This method will prompt the user for input to enter one of the following commands:
        #
        #   View:   View all tasks in the current task list
        #   Add:    Add a new task to the task list
        #   Remove: Remove a task from the task list
        #   Send:   Send the task list to an email address or phone via SMS
        #   Exit:   Exit Tasker Action Menu and terminate the program.
        #
        # It will loop indefinitely until a valid action has been entered.
        #
        # [RETURNS]:
        # Once a valid action has been entered, this method will return the selected action as a lowercase string.
        #
        # If stored in a variable, such as "action" in the syntax example, that variable can then be passed through to
        # the Action.perform_action method to perform the action that the user inputted.

        while True:

            # Define the list of valid action options for the user to choose from.
            choices = ["view", "add", "remove", "send", "exit", "v", "a", "r", "s", "e"]

            # List the valid action options for the user.
            print("\n{Tasker Action Menu}")
            print("Please select from one of the following options:")
            print("\nView:    View the current task list.")
            print("Add:     Add an item to the task list")
            print("Remove:  Remove an item from the list.")
            print("Send:    Send the list to a provided email address or phone number.")
            print("Exit:    Exit the program.")

            # Get the user's choice of action
            action = input("\n[Type \"View\", \"Add\" \"Remove\" \"Send\" or \"Exit\" and press ENTER]: ")

            # Ensure action entered by the user is a valid choice
            action = action.lower()

            # If a valid action was entered
            if action in choices:

                # Return the action and continue on with the main loop
                return action

            # If an invalid action was entered
            else:

                # Tell the user it was invalid and restart this method.
                print("\n<"+action+"> is not a valid action. Please select a valid action from the list.")

    # Create the perform_action method
    def perform_action(action):

        # [SYNTAX]: Action.perform_action(action)
        #
        # [ARGUMENTS]:
        #   action  <String>    The action (i.e. "view", "v", "add", "a", etc.) to be performed.
        #
        # [SUMMARY]:
        # With the action variable passed as an argument (which was returned from the get_action method), this method
        # will perform the corresponding action.
        #
        # [RETURNS]:
        # Returns True if successful or False if failed.
        #
        # *** Note that this should always return True and will only return False as a result of a bug ***

        # PERFORM THE ACTION SELECTED BY THE USER
        # [VIEW]:   View all entries that are currently in the Task List.
        if action == "view" or action == "v":

            # View the task list
            Action.view_tasklist()
            return True

        # [ADD]:    Add a new entry to the Task List.
        elif action == "add" or action == "a":

            Action.new_task()
            return True

        # [REMOVE]: Remove an entry from the task list.
        elif action == "remove" or action == "r":
            print("\nSelected remove. Preparing to remove item...")
            return True

        # [SEND]:   Send the task list to an email address or SMS device.
        elif action == "send" or action == "s":
            print("\nSelected send. Preparing to send item...")
            return True

        # [EXIT]:   Exit Tasker Action Menu and terminate the program.
        elif action == "exit" or action == "e":
            print("\n\nExiting tasker...\n")
            exit()

        # [INVALID ACTION]: This should never happen and is only here to catch bugs/glitches.
        else:
            print(
                "\n\n$*!@$#%&$**&$*!@&$*@$*#&%&@(^#(!@*^\n\nERROR 404: INCORRECT COMMAND ISSUED\n\n&!(@^(#*@#(!&#@|")
            return False

    # Create the view_tasklist method
    def view_tasklist():

        # [SYNTAX]: Action.view_tasklist()
        #
        # [ARGUMENTS]:
        # This method takes no arguments.
        #
        # [SUMMARY]:
        # If the task list has any entries in the tasklist.txt file, this method will print them. If there are no
        # entries, it will print a message stating that the task list is empty and then return to the main TAM
        # interface.
        #
        # [RETURNS]:
        # Returns (1) when complete.

        # Tell the user that the task list is currently opening.
        print("\n{View Task List}\n")

        # Open the task list file for reading
        tasklist = open("tasklist.txt", "r+")

        # If the task list is empty
        if tasklist.read() == "":
            print("\nThere are currently no tasks assigned to your list.\n\nReturning to Tasker Action Menu.")

        # If the task list is not empty
        else:
            tasklist.seek(0)
            print(tasklist.read())

        # Close the task list file.
        tasklist.close()

        # Return 1 when complete.
        return 1

    # Create the new_task method
    def new_task():

        # [SYNTAX]: Action.new_task(section, name, notes)
        #
        # [ARGUMENTS]:
        # This method takes no arguments.
        #
        # [SUMMARY]:
        # This method first prompts the user to either create a new task or go back. Back will bring the user back to
        # the TAM. Add will prompt the user for several options and then add the task to the task list.
        #
        # [RETURNS]:
        # Returns (1) when complete.

        # Tell the user they're about to create a new task
        print("\n{ADD NEW TASK}")
        print("Create a new task and add it to your task list or return to TAM.")
        print("\n    Add:    Add a new task to the task list.\n    Back:   Return to TAM.")

        # Loop until the user adds a new task or goes back to TAM.
        while True:

            # Get choice from the user
            choices = ["add", "a", "back", "b"]
            choice = input("\n[Type \"Add\" or \"Back\" and press ENTER]: ")

            # If a valid choice was entered
            choice = choice.lower()
            if choice in choices:

                # If the choice was to go back
                if choice == "back" or choice == "b":
                    print("Returning to Tasker Action Menu...")
                    break

                # If the choice was to add a task
                elif choice == "add" or choice == "a":

                    # Get the new task variables from the User
                    location = input("\nWhere will this task take place? [Please provide a task location]: ")
                    description = input("What is required of this task? [Please provide task details]: ")

                    # Tell the user task is being added
                    print("\nAdding new task...")

                    # Open the tasklist file
                    tasklist = open("tasklist.txt", "a")

                    # Add the task to the task list
                    tasklist.write(location+"      "+description+"\n")

                    # On success, close the tasklist and inform the user
                    tasklist.close()
                    print("\nOperation successful! Returning to Tasker Action Menu...")
                    return 1

            # If an invalid choice was entered
            else:

                # Tell the user it was invalid and restart this method.
                print("\n<" + choice + "> is not a valid choice. Please select a valid choice from the list.")

        # Go back to TAM
        return 1