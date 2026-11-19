people = [
    {"name": "Mark", "house": "big"},
    {"name": "Daniel", "house": "medium"},
    {"name": "Callejas", "house": "alot"}
]

def f(person):
    return person["house"]

people.sort(key=f)

print(people)