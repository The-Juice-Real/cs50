students = [
    {"name" : "Harry", "house" : "Gryffindor", "sex" : "male"},
    {"name" : "Tuguldur", "house" : "Cards", "sex" : "sex symbol of UB"},
    {"name" : "Draco", "house" : "Slytherin", "sex" : "male"},
    {"name" : "Hermione", "house" : "Gryffindor", "sex" : "female"},
    {"name" : "A random Soka student", "house" : "The Cult of Ikeda", "sex" : None}
]

for student in students:
    print(student["name"], student["house"], student["sex"])