a = [66.25, 333, 333, 1, 1234.5]
print("a:", a)

print(a.count(333), a.count(66.25), a.count('x'))

a.insert(2, -1)
print("a.insert(2, -1)")
print("a:", a)

a.append(333)
print("a.append(333)")
print("a:", a)

print("a.index(333)=", a.index(333))

a.remove(333)
print("a.remove(333)")
print("a:", a)

a.reverse()
print("a.reverse():")
print("a:", a)

a.sort()
print("a.sort()")
print("a:", a)

print("a.pop", a.pop())

print("a:" ,a)
