# Create a class called Person
# Add two attributes: name and age that can be set when the object is created.
# Create a method called introduce that prints a string in the format:
# Hi, My name is Joe and I am 12 years old.



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, My name is {self.name} and I am {self.age} years old.")

# Example usage
p = Person("Joe", 12)
p.introduce()