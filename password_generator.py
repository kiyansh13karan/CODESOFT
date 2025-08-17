'''
A password generator is a useful tool that generates strong and
random passwords for users. This project aims to create a
password generator application using Python, allowing users to
specify the length and complexity of the password.


User Input: Prompt the user to specify the desired length of the password.
Generate Password: Use a combination of random characters to generate a password of the specified length.
Display the Password: Print the generated password on the screen.
'''



import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length <= 0:
            print("Please enter a positive number for the password length.")
            return

        generated_password = generate_password(length)
        
        print(f"Generated Password: {generated_password}")
        
    except ValueError:
        print("Invalid input. Please enter a number for the password length.")

if __name__ == "__main__":
    main()