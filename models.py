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