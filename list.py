l=[10,30,20,50,40,60]
print("Type of object is:", type(l))
l.append(70)
print("70 is appended:",l)

l.insert(2,90)
print("90 is inserted:",l)

l1=[100,300,500]
l.extend(l1)
print("list is extended:",l)

l.sort()
print("sorted list:",l)

l.reverse()
print("reverse list is:",l)

l2=l.copy()
print("copied list",l)

l.pop()
print("popped element",l)

x=l.index(40)
print(x)