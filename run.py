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
