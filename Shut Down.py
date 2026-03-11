def shutdown(system):
    if system == "yes":
        print("Shutting down...")
    elif system == "no":
        print("Shutdown aborted.")
    else:
        print("Sorry, invalid input.")
user_input = input("Do you want to shutdown the system? (yes/no): ")
shutdown(user_input)