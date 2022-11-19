from data_manager import DataManager

data = DataManager()


def post_user_credentials():
    # Post user credentials into google sheet
    print("Welcome to David's Flight Club.")
    print("We find the best flight deals and email you.")
    first_name = input("What is your first name?\n").title()
    last_name = input("What is your last name?\n").title()
    email = input("What is your email?\n")
    if email == input("Type your email again.\n"):
        data.post_users(first_name, last_name, email)


post_user_credentials()
