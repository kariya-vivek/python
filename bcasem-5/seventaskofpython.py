#prime number
a=int(input("enter any number="))
c=0
for i in range(2,a+1):
  if(a%i==0):
    c+=1
if(c<=2):
  print("number is prime")
else:
  print("number is not prime")

print("print prime number between 1 to 100")
#check prime number between 1 to 100
for i in range(2,100):
  c=0
  for j in range(1,i+1):
    if(i%j==0):
      c+=1
  if(c==2):
    print(i,end=" ")
    
print("\nprint reverse number")
#print reverse number
a=int(input("enter any number="))
t=a
v=0
while(a>0):
  c=a%10
  a=a//10
  v=v*10+c
print("number reverse is=",v)

print("print armstrong  number")
#check and print number is armstrong or not
a=int(input("enter any number="))
t=a
v=0
while(a>0):
  c=a%10
  a=a//10
  v+=c*c*c
if(v==t):
  print("number is armstrong")
else:
  print("number is not armstrong")
  
print("print palindrom  number")
#print palindrom number
a=int(input("enter any number="))
t=a
v=0
while(a>0):
  c=a%10
  a=a//10
  v=v*10+c
if(v==t):
  print("number is palindrom=",v)
else:
  print("number is not palindrom")

print("print factorial  number")
#print factorial number
a=int(input("enter any number"))
v=1
for i in range(1,a+1):
  v*=i
print("number factorial is=",v)
  
  

  
