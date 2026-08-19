passwords = ["abc", "helloworld12345", "HelloWorld12345", "qwerty", "SuperSecurePass99" ]

for password in passwords:
    if len(password) <14:
        print(password,  "-> WEAK(too short)")
    elif password.lower() == password:
        print(password, "-> WEAK(no uppercase letters)")
    else:
        print(password, "-> STRONG")
        