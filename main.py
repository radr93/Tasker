# Import Modules
from actions import Action

# Show launch welcome message and version information
version = 0.03
welcome_message = "\nWelcome to Tasker! Current version is "
print(welcome_message, version, ".")

# Main Program Loopv
while True:

    # Prompt the user for an action
    action = Action.get_action()

    # Execute the action that the user performed
    success = Action.perform_action(action)

    # Error catching - unsuccessfully performed action
    if success is False:
        print("Bug caused program to crash - success is False (main.py line 21)")
        print("Unsuccessfully performed action:", action)

        # Crash the program
        exit()