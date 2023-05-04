import random
import string

def gen_password(length):
    # Possible characters of a password including numbers and letters
    characters = string.ascii_letters + string.digits 
    
    # Generate a password with the specified length of 12 
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Example usage: generate a random password with length 12
password = gen_password(12)
print("The random password is",password)
