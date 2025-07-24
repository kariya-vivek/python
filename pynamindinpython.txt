#nested loop

#pyramind
print("\npyramind")
for i in range(1,6):
  for j in range(1,i+1):
    print("*",end=" ")
  print()

print("\n\nreversed * pyramind")
  
#reversed * pyramind

for i in range(5,0,-1):
  for j in range(1,i+1):
    print("*",end=" ")
  print()

print("\n\neven number pyramind")

  
#even number pyramind
for i in range(1,6):
  n=2
  for j in range(1,i+1):
    print(n,end=" ")
    n+=2
  print()
  
print("\n\nodd number pyramind")

#odd number pyramind
for i in range(1,6):
  n=1
  for j in range(1,i+1):
    print(n,end=" ")
    n+=2
  print()

print("\n\nprint number pyramind")

  
#print number pyramind
for i in range(1,6):
  for j in range(1,i+1):
    print(j,end=" ")
  print()

print("\n\nprint number reversed pyramind")

#print number reversed pyramind
for i in range(5,0,-1):
  x=5
  for j in range(1,i+1):
    print(x,end=" ")
    x-=1
  print()
  
print("\n\nprint number  pyramind (1) (2 2)")

#print number reversed pyramind
for i in range(1,6):
  for j in range(1,i+1):
    print(i,end=" ")
  print()
  

  
