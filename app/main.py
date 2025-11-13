class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self

def create_person_list(people: list) -> list:
    [Person(person["name"], person["age"]) for person in people]
    for p in people:
        person_obj = Person.people[p["name"]]
        wife_name = p.get("wife")
        if wife_name is not None:
            person_obj.wife = Person.people[wife_name]
        husband_name = p.get("husband")
        if husband_name is not None:
            person_obj.husband = Person.people[husband_name]
    return [Person.people[p["name"]] for p in people]
