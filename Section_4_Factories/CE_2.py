class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'Person {self.name} is  registered by ID = {self.id} '

    class PersonFactory:
        id = 0

        @staticmethod
        def create_person(self, name):
            p = Person(Person.PersonFactory.id,name)
            Person.PersonFactory.id += 1
            return p

if __name__ == '__main__':

    p1 = Person.PersonFactory.create_person('Anton')
    p2 = Person.PersonFactory.create_person('Alex')
    p3 = Person.PersonFactory.create_person('Kirill')
    p4 = Person.PersonFactory.create_person('Vesna')
    print(p1)
    print(p2)
    print(p3)
    print(p4)