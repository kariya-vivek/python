from teacher import Teacher

class Student(Teacher):
    def setmarks(self, marks):
        self.marks = marks

    def getmarks(self):
        return self.marks

s = Student()
s.setid(1)
s.setname("vivek")
s.setaddress("babra")
s.setmarks(95)

print("Id =", s.getid())
print("Name =", s.getname())
print("Address =", s.getaddress())
print("marks =", s.getmarks())
