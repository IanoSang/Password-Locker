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
