from Pile import Pile
from Pile import PileSingleton
from RefactorPile import RefactorPile
import inspect

p = Pile()
p2 = Pile(10)

#print(p.isEmpty())
print(p2.isEmpty())

#print(p.isFull())
print(p2.isFull())

p2.push("travail")
print(p2.isEmpty())
print(p2.isFull())


p2.printOn()

p2.pop()

p2.printOn()
print(p2.isEmpty())
print(p2.isFull())


print(p2.capacite)

print("----------------------------------------")
p = Pile()
p2 = Pile(10)
p.printOn()
p2.printOn()


print("----------------------------------------")

#print(Pile.__class__)
#print(inspect.getmembers(Pile, inspect.isclass))
#print(inspect.getmembers(Pile, inspect.ismethod))
#print((inspect.getmembers(Pile, inspect.isfunction))['push'])
#print(inspect.getmembers(Pile, inspect.isfunction))


for fun in inspect.getmembers(Pile, inspect.isfunction) :
	if fun[0] == 'push' :
		pushFunction = fun[1]

#print(pushFunction)

print('------------------------')
refP = RefactorPile(1)
p = Pile(1)
p.push('10')
refP.push('10')
refP.grow()
refP.push('10')


print('------------------------')
print(PileSingleton._instances)

input("====")