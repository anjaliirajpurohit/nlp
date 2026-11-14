import re

def validate_password(password):
    # 1. Check if it has at least 8 characters
    if len(password) < 8:
        print("Invalid: Password must be at least 8 characters long.")
        return False
        
    # 2. Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        print("Invalid: Password must contain at least one uppercase letter.")
        return False
        
    # 3. Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        print("Invalid: Password must contain at least one lowercase letter.")
        return False
        
    # 4. Check for at least one digit
    if not re.search(r'[0-9]', password):
        print("Invalid: Password must contain at least one digit.")
        return False
        
    # 5. Check for at least one special character
    if not re.search(r'[@#$%&*]', password):
        print("Invalid: Password must contain at least one special character.")
        return False
        
    # If it passes all the checks above, it is valid!
    print("Success: Password is valid!")
    return True

# Accept a password from the user
user_password = input("Enter a password to validate: ")
validate_password(user_password)