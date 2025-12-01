#print sum of square
print("print sum of square")
n=int(input("enter value of num="))
sum=0
for i in range(1,n+1):
  sum+=(i*i)
print(sum)

#print sum of odd number
print("print sum of odd number")
n=int(input("enter any number="))
sum=0
for i in range(1,n+1,2):
  sum+=i
print(sum)

#print sum of even num
print("print sum of even number")
n=int(input("enter value of num="))
sum=0
for i in range(2,n+1,2):
  sum+=i
print(sum)

#print sum of 1/1+1/2
print("print sum of 1/1+1/2")
n=int(input("enter value of num="))
sum=0
for i in range(1,n+1):
    sum+=1/i
print(sum)


#print sum of factorial
print("print sum of factorial")
n =int(input("enter value of num="))
sum = 0
for i in range(1,n+1):
    f=1
    for j in range(1,i+1):
      f*=j
    sum+=f
print(sum)


