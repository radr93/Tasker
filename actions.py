# Import Modules
import os

# [MODULE NAME]
# Actions.py
#
# [MODULE SUMMARY]
# This module is used to handle the Tasker Action Menu (TAM).
#
# The TAM is handled by one class - "Action", that contains the following methods:
#
#   Action.get_action()
#   Prompt the user for an action [View, Add, Remove, Send, Exit] to interact with the tasklist.
#
#   Action.view_tasklist()
#   Print all tasks in the tasklist
#
#   Action.new_task(category, name)
#   Add a new task to the tasklist
#
#   Action.perform_task(action)
#   Perform the action entered by Action.get_action()


# Create the Action class
class Action:

    # Create the get_action method
    def get_action():

        # [SYNTAX]:
        # <variable_name> = Action.get_action()
        #
        # [ARGUMENTS]:
        # This method takes no arguments.
        #
        # [SUMMARY]:
        # This method prompts the user for input to enter one of the following commands:
        #
        #   View:   View all tasks in the current task list
        #   Add:    Add a new task to the task list
        #   Remove: Remove a task from the task list
        #   Send:   Send the task list to an email address or phone via SMS
        #
        # It will loop indefinitely until a valid action has been entered.
        #
        # [RETURNS]:
        # When a valid action has been entered, this method will return the selected action as a lowercase string.

        while True:

            # Define the list of valid action options for the user to choose from
            choices = ["view", "add", "remove", "send", "exit", "v", "a", "r", "s", "e"]

            # Get the user's choice
            print("\n[Tasker Action Menu]")
            print("Please select from one of the following options:")
            print("\nView:    View the current task list.")
            print("Add:     Add an item to the task list")
            print("Remove:  Remove an item from the list.")
            print("Send:    Send the list to a provided email address or phone number.")
            print("Exit:    Exit the program.")

            action = input("\n[Type \"View\", \"Add\" \"Remove\" \"Send\" or \"Exit\" and press ENTER]: ")

            # Ensure action choice matches one of possible choices
            action = action.lower()
            if action in choices:
                return action

            # If an defined action was not entered, restart loop
            else:
                print("\n<"+action+"> is not a valid action. Please select a valid action from the list.")

    # Create the view_tasklist method
    def view_tasklist():

        # [SYNTAX]:
        # Action.view_tasklist()
        #
        # [ARGUMENTS]:
        # This method takes no arguments.
        #
        # [SUMMARY]:
        # If the task list has any entries, this method will print them. If there are no entries, it will provide a
        # message stating that the task list is empty.
        #
        # [RETURNS]:
        # Returns (1) when complete.

        # Perform the action selected by the user
        print("\n[View Task List]\nFetching tasks.....\n")

        # Open the task list file for reading
        tasklist = open("tasklist.txt", "w+")

        # If the task list is empty
        if tasklist.read() == "":
            print("There are currently no tasks assigned to your list.")

        # If the task list in not empty
        else:
            print(tasklist.readlines())

        # Close the task list file
        tasklist.close()
        return 1

    # Create the new_task method
    def new_task(task_name):

        # [SYNTAX]:
        # Action.new_task(task_category, task_name)
        #
        # [ARGUMENTS]:
        #   task_category   The task's location.        e.g. "Superstore", "MPI"
        #   task_name       The task's name.            e.g. "Ham", "Renew insurance"
        #
        # [SUMMARY]:
        # This method adds a new task to the task list
        #
        # [RETURNS]:
        # Returns (1) when complete.

        asd = ["asd1", "asd2", "asd3"]
        asd.remove("asd2")
        print(asd)

        os.remove("task_list.txt")

    # Create the perform_action method
    def perform_action(action):

        # [SYNTAX]:
        # Action.perform_action(action)
        #
        # [ARGUMENTS]:
        #   _action An action previously provided by the Action.getAction method
        #
        # [SUMMARY]:
        # Once the user provides TAM with an action with Action.getAction, it should be stored in a variable and
        # passed as an argument to this method.
        #
        # It will then perform the corresponding action.
        #
        # [RETURNS]:
        # Returns True if successful or False if failed.
        # Note that this would only fail as a result of a bug.

        # Perform the action selected by the user

        # [VIEW TASK LIST ACTION]
        # This
        if action == "view" or action == "v":

            # View the task list
            Action.view_tasklist()
            return True

        # [ADD TASK ACTION]
        elif action == "add" or action == "a":

            Action.new_task()
            return True

        # [REMOVE TASK ACTION]
        elif action == "remove" or action == "r":
            print("\nSelected remove. Preparing to remove item...")
            return True

        # [SEND TASK LIST ACTION]
        elif action == "send" or action == "s":
            print("\nSelected send. Preparing to send item...")
            return True

        # [EXIT TASKER ACTION MENU]
        elif action == "exit" or action == "e":
            print("\n\nExiting tasker...\n")
            exit()

        # [BUG/ERROR CATCHING]
        else:
            print("\n\n$*!@$#%&$**&$*!@&$*@$*#&%&@(^#(!@*^\n\nERROR 404: INCORRECT COMMAND ISSUED\n\n&!(@^(#*@#(!&#@|")
            return False
