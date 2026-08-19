password = input("Enter your password: ")
if len(password) < 14:
    print("Password is too short. It must be at least 14 characters long. ")
elif len(password) < 14:
    print("WARNING : Password does not meet minimum length(14+)")
elif password.lower() == password:
    print("WARNING : Password must contain uppercase letters.")
else:
    print("OK: Password meets basic checks.")