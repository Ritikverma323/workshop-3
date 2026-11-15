import requests

# GET REQUEST
response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

# CHECK STATUS
print("Status:", response.status_code)

# CONVERT JSON RESPONSE INTO PYTHON DATA
users = response.json()

# READ DATA
print(users[0])

# PRINT USING LOOP
for user in users:
    print(user["name"], user["email"])