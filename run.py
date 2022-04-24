#!/usr/bin/env python3.9

from passwordlock import User, Credentials


def create_new_user(username, password):
    """
    Function to create a new user
    """
    new_user = User(username, password)
    return new_user


def save_user(user):
    """
    Function to save a new user
    """
    user.save_user()


def display_user():
    """
    Function to display existing user
    """
    return User.display_user()


def login_user(username, password):
    """
    function that checks whether a user exist and then login the user in.
    """

    check_user = Credentials.verify_user(username, password)
    return check_user


def create_new_credential(account, username, password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account, username, password)
    return new_credential


def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials.save_details()


def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()


def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list
    """
    credentials.delete_credentials()


def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)


def check_credentials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false
    """
    return Credentials.if_credential_exist(account)


def generate_password():
    """
    generates a random password for the user.
    """
    auto_password = Credentials.generatePassword()
    return auto_password


def copy_password(account):
    """
    Function to copy the password using the pyperclip framework.
    """
    return Credentials.copy_password(account)


def main():
    global username, password
    print(
        "Hello Welcome to your You Password Locker\n Please enter one of the following to proceed.\n CN ---  "
        "Create New Account  \n LG ---  Login to an Existing Account  \n")
    short_code = input("").lower().strip()
    if short_code == "cn":
        print("Sign Up")
        print('=' * 60)
        username = input("User_name: ")
        while True:
            print(" TP - To type your own password:\n GP - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_password()
                break
            else:
                print("Invalid input please try again")
        save_user(create_new_user(username, password))
        print("*" * 60)
        print(f"Hello {username}, Your account has been created successfully! Your password is: {password}")
        print("*" * 60)
    elif short_code == "lg":
        print("*" * 50)
        print("Enter your User name and your Password to log in:")
        print('*' * 50)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username, password)
        if login_user == login:
            print(f"Hello {username}.Welcome To PassWord Locker Manager")
            print('\n')
    while True:
        print('=' * 60)
        print(
            "Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a "
            "credential \n GP - Generate A random password \n DL - Delete credential \n EX - Exit the application \n")
        print('=' * 60)
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("." * 20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            username = input()
            while True:
                print(
                    " TP - To type your own password if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_password()
                    break
                else:
                    print("Invalid password Please try again!")
            save_credentials(create_new_credential(account, username, password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {username} - Password:{password} created successfully")
            print('\n')
        elif short_code == "dc":
            if display_accounts_details():
                print("Here's your list of accounts: ")

                print('*' * 50)
                print('_' * 50)
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_' * 50)
                print('*' * 50)
            else:
                print("You don't have any credentials saved yet!!")
        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"User Name: {search_credential.username} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print(f"{search_name} Credentials does not exist!!")
                print('\n')
        elif short_code == "dl":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_" * 50)
                search_credential.delete_credentials()
                print('\n')
                print(f"You  have deleted {search_credential.account} credentials successfully!!")
                print('\n')
            else:
                print(f"The {search_name} credentials You want to delete does not Exist in this locker!!")

        elif short_code == 'gp':

            password = generate_password()
            print(f" {password} Has been generated successful. You can proceed to use it to your account")
        elif short_code == 'ex':
            print(f"Thanks for using Passwords Locker. Byee {username}!\n IanSang © 2022 ")
            break
        else:
            print("Invalid input, Please use the short codes")


if __name__ == '__main__':

    main()
