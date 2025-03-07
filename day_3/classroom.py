class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def full_name(self):
        return f"{self.firstname} {self.lastname}"

class Student(Person):
    def __init__(self, firstname, lastname, subject):
        super().__init__(firstname, lastname)
        self.subject = subject
    
    def printNameSubject(self):
        print(f"{self.full_name()}, {self.subject}")

if __name__ == "__main__":
    me = Student('Benedikt', 'Daurer', 'physics')
    me.printNameSubject()