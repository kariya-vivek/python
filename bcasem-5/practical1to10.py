#practical1
print("Hello World", end="\nthis is python")


#practical2

#string
s1="welcome to ksc"
print(s1)
print(s1[0])
print(s1[5])
print(s1[2:5])
print(s1[4:])
print(s1[-2:])
print(s1[:-1])

#int,float,complex,boolean
#numeric datatype
print("int and float datatype")
#(1)int and (2)float
a=10
b=20.30
print(a,b)
print(type(a))
print(type(b))

#(3)complex
print("complex datatype")
c=2.5+3.8j
d=3.5-4
e=c+d
print("sum=",e)

#boolen datatype
print("boolen datatype")
a=10
b=20
if(a<b):
    print("b is big");

else:
    print("b is small")

print(10==10)
print(10>20)
print(10!=10)
print(10>=20)
print(10<10)
print(10<=20)
print(bool(""))
print(bool("welcome"))

#practical3
print("use id(),type(),range() function")
print("id() function example")
x = 10
print("The id of x is:", id(x))
a = 100
b = 100
print("a == b:", a == b)
print("id(a):", id(a))
print("id(b):", id(b))
print("type() function example")
l=["rohit",1,1.5,50,-20]
print(type(l))
t=("rohit",1,1.5,50,-20)
print(type(t))
print("range() function example")
for i in range(2, 11, 2):
    print(i)
    
#practical4
print("type conversion function")
x = "123"
print("Original type of x:", type(x))

# Convert string to integer
y = int(x)
print("After conversion, type of y:", type(y))
print("y + 1 =", y + 1)

#practical5
print("operator in python")
#arithmatic operator
print("arithmatic operator")
a=100
b=10
print("a+b=",a+b)
print("a-b",a-b)
print("a*b",a*b)
print("a/b",a/b)
print("a%b",a%b)
print("a**b",a**b)
print("a//b",a//b)

#assignment operator
print("assignment operator")
x=60
y=10
x+=y
print("x+=y=",x)
x-=y
print("x-=y=",x)
x*=y
print("x*=y=",x)
x/=y
print("x/=y",x)
x%=y
print("x%=y",x)
x**=y
print("x**=y",x)
x//=y
print("x//=y",x)

#relational operator
print("relational operator")
a=10
b=20
print("a=10 and b=20 check a==b",a==b)
print("a=10 and b=20 check a!=b",a!=b)
print("a=10 and b=20 check a>=b",a>=b)
print("a=10 and b=20 check a<b",a<b)
print("a=10 and b=20 check a>b",a>b)
print("a=10 and b=20 check a<=b",a<=b)

#logical operator
print("Logical operator")
a=100
b=20
c=30
print("a=100,b=20,c=30 and check a>b and a>c=",a>b and a>c)
print("a=100,b=20,c=30 and check a>b or a<c=",a>b or a<c)

#bitwise operator
print("bitwise operator")
a=20
b=30
print("a & b=",a & b)
print("a | b=",a | b)
print("a << b",a << b)
print("a >> b",a >> b)

#ternary operator
print("ternary operator")
a = 5
b = 10
max_value = a if a > b else b
print("Maximum value is:", max_value)


#practical6
print("example of input")
name =input("Enter your name:")
print("Hello", name)
print("example of print")
print("This is a Python print function example.")
print("example of sep")
print("Python", "is", "fun", sep=" - ")
print("example of end")
print("Welcome to", end=" ")
print("Craftzon!")
print("example of replacement operator")
name = "Amit"
age = 25
print("My name is {} and I am {} years old.".format(name, age))

#practical7
print("conditional statment")
print("example of if")
i=int(input("enter any number to check even or odd="))
if(i%2==0):
  print("even")
  
print("example of if-else to check which number is big")
i=int(input("enter value of num1="))
y=int(input("enter value of num2="))
if(i>y):
  print("num1 is big",i)
else:
  print("num2 is big",y)
  
print("example of if-elif-else  to enter 3 number and check which is big")
n1=int(input("enter value of num1="))
n2=int(input("enter value of num2="))
n3=int(input("enter value of num3="))
if(n1>n2 and n1>n3):
  print("n1 is big",n1)
elif(n2>n1 and n2>n3):
  print("n2 is big")
else:
  print("n3 is big",n3)

#practical8
print("work with itractive statment")
print("print table using while loop")
a=int(input("enter any number to print table="))
i=1
while(i<=10):
  print(a, "*", i, "=", a * i)
  i+=1
print("print sum from list")
li=[10,20,30,60,70,80]
sum=0
for i in li:
  sum+=i
print("total",sum)

#practical9
print("break,continue,pass")
#break
print("example of break")
li=[1,2,3,4,5]
for i in li:
  if(i==3):
    break
  print(i)
  
#continue
print("example of continue")
li=[1,2,3,4,5]
for i in li:
  if(i==3):
    continue
  print(i)
  
  
#pass statment
print("example of pass statment")
#retrive neagative number
li=[1,2,3,4,-5,-6,-7,-8]
for i in li:
  if(i>0):
    pass
  else:
    print(i)

#practical10
text = "Craftzon"

print("Original string:", text)

print("\nIndexing:")
print(text[0])
print(text[3])
print(text[-1])
print(text[-8])

print("\nSlicing:")
print(text[0:5])
print(text[::2])
print(text[1:7:2])
print(text[:4])
print(text[4:])
print(text[:])
print(text[::-1])
