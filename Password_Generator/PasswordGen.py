import time    #time module for add a time space between intro and instructions 
import random    #module to generate random characters and values
import string    
from headerText import print_logo

def generate_password(length, include_uppercase, include_digits, special_characters):
    characters = string.ascii_lowercase  # Always include lowercase letters
    
    # Add other character sets based on user choices
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if special_characters:
        characters += string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to get a valid integer input for the password length
def get_password_length():
    while True:
        try:
            length = int(input("Hii user!\nEnter the length of password you want to create: "))
            if length > 0:
                return length
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the password length.")
# for ASCII GENERATOR AS TOP
print_logo()
time.sleep(1)
# Get user inputs
length = get_password_length()
include_uppercase = input("Do you want to include UPPERCASE letters in your password? (y/n): ").lower() == 'y'
include_digits = input("Do you want to include DIGITS in your password? (y/n): ").lower() == 'y'
special_characters = input("Do you want special characters? (y/n): ").lower() == 'y'

# Generate and display the password
password = generate_password(length, include_uppercase, include_digits, special_characters)
time.sleep(1)
print("Generated password:", password)
time.sleep(2)
print("THANKS FOR USING ME")
