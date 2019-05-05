# Import Modules
from actions import Action

# Show launch welcome message and version information
version = 0.04
welcome_message = "\nWelcome to Tasker! Current version is "
print(welcome_message, version,".")

# Main Program Loop
while True:

    # START UP TASKER ACTION MENU (TAM)

    # Prompt the user for an action
    action = Action.get_action()

    # Execute the action that the user performed
    success = Action.perform_action(action)

    # <Glitch/bug error catching - success should never return false>
    if success is False:
        print("Error in main.py!")
        print("Bug caused program to crash - success is False (line 23)")
        print("Unsuccessfully performed action:", action)

        # Crash the program
        exit()