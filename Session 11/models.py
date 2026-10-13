import csv


print("hello World")
print("AI is the future")
print("Let's build something amazing together!")
print("Keep learning and growing every day.")
print("Embrace challenges and never give up.")
print("Collaboration leads to innovation.")
print("Stay curious and explore new ideas.")
print("Success comes from perseverance and hard work.")
print("Believe in yourself and your abilities.")
# 
#  CSV writing mode
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Grade"])
    writer.writerow(["Alice", 30, "A"])
    writer.writerow(["Bob", 25, "B"])   

# CSV reading mode
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for i in reader:
        print(i)

# JSON writing mode
import json

data = {
    "students": [
        {"name": "Alice", "age": 30, "grade": "A"},
        {"name": "Bob", "age": 25, "grade": "B"}
    ]
}

with open("students.json", "w") as file:
    json.dump(data, file)

# JSON reading mode
with open("students.json", "r") as file:
    data = json.load(file)
    for student in data["students"]:
        print(student)