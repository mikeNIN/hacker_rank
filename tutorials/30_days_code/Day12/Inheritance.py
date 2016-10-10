    
class Person:
    def __init__(self, firstName, lastName, idNumber):
            self.firstName = firstName
            self.lastName = lastName
            self.idNumber = idNumber
    def printPerson(self):
            print "Name:", self.lastName + ",", self.firstName
            print "ID:", self.idNumber

class Student(Person):
    def __init__(self, firstName, lastName, idNumber,   scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
    def printPerson(self):
        Person.printPerson(self)
    def calculate(self):
        avarage = sum(scores)/len(scores)
        if 90 <= avarage <= 100:
            return 'O'
        elif 80 <= avarage < 90:
            return 'E'
        elif 70 <= avarage < 80:
            return 'A'
        elif 55 <= avarage < 70:
            return 'P'
        elif 40 <= avarage < 55:
            return 'D'
        else:
            return 'T'


line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input()) # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()
