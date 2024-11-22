username = "admin"
password = "admin123"

input_user = input("Enter username: ")
input_password = input("Enter password: ")

if username == input_user and password == input_password:
    print("Login successful")
else:
    print("Login failed.")