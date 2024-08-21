import random
import string

# Simulated database to store password sets
password_db = {}

# Function to generate a strong password suggestion
def generate_strong_password():
    length = 12  # Fixed length for strong password suggestion
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Function to create a new password set
def create_new_password_set():
    account_name = input("Enter the name for the password set (e.g., 'Email', 'Bank', etc.): ")
    if account_name in password_db:
        print("An account with this name already exists.")
        return
    
    # Function to get password input with an option for strong suggestion
    def get_password_input(password_type):
        print(f"\n{password_type} Password:")
        print("1) Provide your own password")
        print("2) Use a strong password suggestion")
        choice = input("Choose an option (1-2): ")

        if choice == '1':
            return input(f"Enter your {password_type.lower()} password: ")
        elif choice == '2':
            suggested_password = generate_strong_password()
            print(f"Suggested {password_type.lower()} password: {suggested_password}")
            return suggested_password
        else:
            print("Invalid choice. Please select a valid option.")
            return get_password_input(password_type)
    
    # Collect passwords for all three levels
    textual_password = get_password_input("Textual")
    graphical_password = get_password_input("Graphical")
    behavioral_password = get_password_input("Behavioral")
    
    # Save the password set to the database
    password_db[account_name] = {
        "textual": textual_password,
        "graphical": graphical_password,
        "behavioral": behavioral_password
    }
    print(f"\nPassword set for '{account_name}' created successfully!")

# Function to log in to an account
def login_to_account():
    if not password_db:
        print("No accounts available to log in.")
        return

    print("\nAvailable accounts:")
    for i, account_name in enumerate(password_db, 1):
        print(f"{i}: {account_name}")
    
    account_choice = int(input("Select an account by number: ")) - 1
    account_name = list(password_db.keys())[account_choice]

    # Verify passwords for all three levels
    def verify_password_input(password_type, correct_password):
        attempt = input(f"Enter your {password_type.lower()} password: ")
        return attempt == correct_password
    
    if verify_password_input("Textual", password_db[account_name]["textual"]):
        if verify_password_input("Graphical", password_db[account_name]["graphical"]):
            if verify_password_input("Behavioral", password_db[account_name]["behavioral"]):
                print("Login successful!")
            else:
                print("Behavioral password is incorrect!")
        else:
            print("Graphical password is incorrect!")
    else:
        print("Textual password is incorrect!")

# Function to delete a password set
def delete_password_set():
    if not password_db:
        print("No accounts available to delete.")
        return

    print("\nAvailable accounts:")
    for i, account_name in enumerate(password_db, 1):
        print(f"{i}: {account_name}")
    
    account_choice = int(input("Select an account to delete by number: ")) - 1
    account_name = list(password_db.keys())[account_choice]

    del password_db[account_name]
    print(f"Password set for '{account_name}' deleted successfully!")

# Main function to run the password manager
def password_manager():
    while True:
        print("\nPassword Manager")
        print("1: Create a new secure password set")
        print("2: Login to an account")
        print("3: Delete a password set")
        print("4: Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            create_new_password_set()
        elif choice == '2':
            login_to_account()
        elif choice == '3':
            delete_password_set()
        elif choice == '4':
            print("Exiting Password Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the password manager
password_manager()
