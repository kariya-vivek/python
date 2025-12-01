#arithmatic operator

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


#unary minus operator

n=10

print("value of n=",n)

print("value of n after unary minus=",-n)

num=-100

print("befor value of num=",num)

print("after unary minus value of num=",num)


#relational operator

a=10

b=20

print("a=10 and b=20 check a==b",a==b)

print("a=10 and b=20 check a!=b",a!=b)

print("a=10 and b=20 check a>=b",a>=b)

print("a=10 and b=20 check a<b",a<b)

print("a=10 and b=20 check a>b",a>b)

print("a=10 and b=20 check a<=b",a<=b)


#logical operator

a=100

b=20

c=30

print("a=100,b=20,c=30 and check a>b and a>c=",a>b and a>c)

print("a=100,b=20,c=30 and check a>b or a<c=",a>b or a<c)


#boolean operator

a=True

b=False

print("a and a",a and a)

print("a or b",a or a)



#bitwise operator

a=20

b=30

print("a & b=",a & b)

print("a | b=",a | b)

print("a << b",a << b)

print("a >> b",a >> b)


# membership operator

#in

citys=["babra","amreli","rajkot","atkot"]

for city in citys:
    print(city,end="\t")

#not in

f=30

x=[100.300,30,20,50]

if(f not in x):
    print("\n f is not present")

else:
    print("\nf is present")


#identity operator

a=20

b=20

print("a is b=",a is b)

a=[10,20]

b=[10,20]

print("check list varable a is b=", a is b)

print("check list varable a is not b=", a is not b)
