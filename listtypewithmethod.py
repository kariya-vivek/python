a=[10,20,30,"abc",'xyz',20.5,60.6,20,10]
print(a[0])
print(a[3:])
print(a[3:5])
print(a[:3])
print(a[-2])
print(a[-3:])
print(a[:-3])
print(a[-1])
print(a[3:5:2])
a[3]=400

#list method

#1)append

a.append(100)
print(a)

#2)copy

b=a.copy()
print(a)
print(b)

#3)clear

b.clear()
print(b)

#4) count

print(a.count(20))

#5)extend

a.extend([500,600])
print(a)

#6)index

print(a.index(30))

#7)insert

a.insert(6,250)
print(a)

#8) pop

a.pop()
print(a)

#9)remove

a.remove(60.6)
print(a)

#10)reverse

a.reverse()
print(a)

#11)sort

c=[500,50,60,70]
c.sort()
print(c)



#tupple datatype

t=(10,30,50,"abc",'xyz',50.65)
print(t)
print(type(t))
print(t[0])
#t[5]=550

#range datatype

a=range(10)
print(a)
for i in a:
    print(i,end=" ")

#odd number using range
print("odd number ")
a=range(1,100,2)
for i in a:
        print(i,end=" ")


#even number using range
print()
print("even number ")
a=range(2,101,2)
for i in a:
        print(i,end=" ")
