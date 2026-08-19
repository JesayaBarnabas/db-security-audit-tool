password = input("Enter your password: ")

while len(password) < 14 or password.lower() == password:
    if len(password) < 14:
        print("Password is too short. It must be at least 14 characters long. ")
    elif password.lower() == password:
        print("Password must contain uppercase letters.")
    password = input("Try again: ")
print("OK: Password meets basic checks.")