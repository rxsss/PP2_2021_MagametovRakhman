class MyClass:
    def __init__(self, fname = "1", lname = "2"):
        self.firstName = fname
        self.lastName = lname
    def printName(self):
        print(self.firstName, self.lastName)


m1 = MyClass("Rakhman", "Magametov")
m1.printName()

class Student(MyClass):
    def __init__(self, id, nameS):
        self.id = id
        self.nameS = nameS
    def printS(self):
        print(self.id, self.nameS)
s1 = Student("18BD", "Rxsssssss")
s1.printS()