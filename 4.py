import requests

# DATA TO SEND
student = {
    "name": "Rahul",
    "email": "rahul@example.com",
    "marks": 90
}

# POST REQUEST
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=student
)

# CHECK STATUS
print("Status:", response.status_code)

# READ SERVER RESPONSE
created_student = response.json()

print("Created data:")
print(created_student)