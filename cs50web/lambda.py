people = [
    {"name": "Mark", "house": "big"},
    {"name": "Daniel", "house": "medium"},
    {"name": "Callejas", "house": "alot"}
]

people.sort(key=lambda person: person["name"])

print(people)