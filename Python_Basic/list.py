L=[1,2,3,4,5,6,7,8,9]
print(L[0:2])
print(L[0:])
print(L[-1])

del(L[6])
print(L[0:])

L[3]=2*3
print(L[0:])

L.append(7)
print(L[0:])

L.sort()
print(L[0:])

L.sort(reverse=True)
print(L[0:])


L.pop()

print(L)

L.pop(5)

L.pop(6)

print(L)

L.clear()

print(L)

L.extend([6,7,8,9,10,11])

print(L)

print(L.count(6))
print(max(L))
print(min(L))
print(sum(L))