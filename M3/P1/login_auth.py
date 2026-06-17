stored_users = {
    "admin": {"password": "secure123", "role": "admin"},
    "user": {"password": "userpass", "role": "user"}
}

attempts = 0
max_attempts = 3
locked_accounts = set()

def authenticate(username, password):
    user_data = stored_users.get(username)
    if not user_data:
        return False
    return user_data["password"] == password

while attempts < max_attempts:
    username = input("Username: ")
    password = input("Password: ")

    if username in locked_accounts:
        print("Account already locked.")
        break
        
    if authenticate(username, password):
        user_data = stored_users[username]
        print("Login successful.")
        if user_data["role"] == "admin":
            print("Admin dashboard access granted.")
        else:
            print("User dashboard access granted.")
        break
    
    attempts += 1
    print(f"Invalid credentials. Attempts left: {max_attempts - attempts}")
    
    if attempts >= max_attempts:
        locked_accounts.add(username)
    
else:
    print("Account locked.")

