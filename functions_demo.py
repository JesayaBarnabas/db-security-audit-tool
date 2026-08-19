def check_password(password):
    if len(password) < 14:
        return "WEAK (too short)"
    elif password.lower() == password:
        return "WEAK (no uppercase)"
    else:
        return "OK"


passwords = ["abc", "helloworld12345", "HelloWorld12345", "qwerty", "SuperSecurePass99", "Short1", "nouppercase12345", "ValidPassword12345"]

for password in passwords:
    result = check_password(password)
    print(password, "->", result)