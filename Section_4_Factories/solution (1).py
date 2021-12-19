class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'User: {self.name} is registered by number: {self.id}'

class PersonFactory:
    id = 0

    # def __init__(self):
    #     self.classa = Person

    def create_person(self, name):
        p = Person(PersonFactory.id, name)
        PersonFactory.id += 1
        return p

if __name__ == '__main__':
    p1 = PersonFactory.create_person(Person, 'Alex')
    p2 = PersonFactory.create_person(Person, 'Jane')
    print(p1)
    print(p2)
