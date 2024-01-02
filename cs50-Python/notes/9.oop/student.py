class Student:
    def __init__(self, name, house):
        #this is specifically called an instance method
        self.name = name
        self.house = house

    def __str__(self):
        #python will autcomatically come to this function when a string is wanted from the object like a print()
        return f"{self.name} is in {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)




main()