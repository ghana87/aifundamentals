class student:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"city: {self.city}")
        print(f"country: {self.country}")

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. I live in {self.city}, {self.country}.")   
    def info(self):
        return f"Name: {self.name}, Age: {self.age}, City: {self.city}, Country: {self.country}"
    
student1 = student("Alice", 30, "New York", "USA")
student2 = student("Bob", 25, "Los Angeles", "USA")

student_list = []
student_list.append(student1)
student_list.append(student2)

for student in student_list:
    print(student.greet())