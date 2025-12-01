from teacher import Teacher

t = Teacher()
t.setid(101)
t.setname("vivek")
t.setaddress("babra")
t.setsalary(75000.00)

print("id =", t.getid())
print("Name =", t.getname())
print("Address =", t.getaddress())
print("Salary =", t.getsalary())
