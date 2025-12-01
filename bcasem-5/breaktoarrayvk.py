#break
li=[1,2,3,4,5]
for i in li:
  if(i==3):
    break
  print(i)
  
#continue
li=[1,2,3,4,5]
for i in li:
  if(i==3):
    continue
  print(i)
  
  
#pass statment


#retrive neagative number
li=[1,2,3,4,-5,-6,-7,-8]
for i in li:
  if(i>0):
    pass
  else:
    print(i)
	
	
#example 2
x=5
while x<100:
  x+=10
  if x>5:
    pass
  print('x=',x)
print("out of loop")


#assert expression
x=10
assert x>0,"wrong input enter"
print("u entered:",x)

#assertion error
x=-10
try:
  assert(x>0)
  print("you entered",x)
except AssertionError:
  print("wrong number entered")
  
  
  
#return statment
#function with argument and with return
def sum1(x,y):
  return x+y
ans=sum1(10,20)
print(ans)

#function with argument and without return
def sum1(x,y):
  print(x+y)
sum1(10,40)

#function without argument and without return
def sum1():
  print(50+20)
sum1()

#function without argument and with return
def sum1():
  return 10+80
ans=sum1()
print(ans)

#array
#normal array example
cars=["ford","volvo","bmw"]
print(cars[0])
for i in cars:
  print(i,end=" ")
x=len(cars)
print("total company",x)
cars.append("oddy")
print(cars)
cars.pop()
print(cars)
cars.remove("volvo")
print(cars)
