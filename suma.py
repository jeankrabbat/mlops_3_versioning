def suma(a, b):
    "suma dos numeros"
    return a + b

def login(username, password):
    if username == "admin":
        return "Login Successful"
    return "Login Failed"

if __name__ == '__main__':
    print(suma(2, 3))
    print(login("admin", "admin"))