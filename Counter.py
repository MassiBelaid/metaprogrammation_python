def create ():
	x = 0
	return lambda: x + 1


f = create()
g = create()


print(f())
print(g())

print("Second call to functions")

print(f())
print(g())
