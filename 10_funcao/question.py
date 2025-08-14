#!usr/bin/env python3

def welcome():
    print("Welcome to the test.")
    input("When you are ready press enter.") 

def question():
    name = input("name:")
    (f"It is nice to meet you {name}")

    color = input("Quat is your favorite color?")
    print(f"{color} is a great color!")

    input("Describe yourself")
    print("admirable!")

def goodbye():
    print("Thank you for participating in the test.") 


welcome()
question()
goodbye()
