# JSON writing mode
import json

data = {
    "students": [
        {"name": "Alice", "age": 30, "grade": "A"},
        {"name": "Bob", "age": 25, "grade": "B"}
    ]
}

with open("data.json", "w") as file:
    json.dump(data, file)

# JSON reading mode
with open("data.json", "r") as file:
    data = json.load(file)
    for student in data["students"]:
        print(student)