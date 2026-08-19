user = {
    "username": "admin",
    "password": "abc",
    "role": "DBA"
}

print(user["username"])
print(user["password"])
print(user["role"])


def check_account(account):
    issues = []
    
    if len(account["password"]) < 14:
        issues.append("Weak password (too short)")
    
    if account["password"].lower() == account["password"]:
        issues.append("Weak password (no uppercase)")
    
    if account["role"] == "DBA":
        issues.append("Excessive privilege (DBA role)")
    
    return issues


accounts = [
    {"username": "admin", "password": "abc", "role": "DBA"},
    {"username": "app_user", "password": "SecurePass123456", "role": "read-only"},
    {"username": "backup_svc", "password": "qwerty12345678", "role": "DBA"},
]

for account in accounts:
    findings = check_account(account)
    print("Account:", account["username"])
    if findings:
        for issue in findings:
            print("  -", issue)
    else:
        print("  No issues found")