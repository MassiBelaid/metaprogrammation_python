from Pile import Pile
import inspect

class RefactorPile(Pile):
	def __new__(cls, taille=None):
		cls.tailleDefaut = 5
		return object.__new__(cls)
	
	@classmethod
	def do(cls):
		PileGrossissante = type('PileGrossissante',(Pile, ), dict())
		print(len(dir(Pile)))
		for fun in inspect.getmembers(Pile, inspect.isfunction) :
			if fun[0] == 'grow' :
				growMethode = fun[1]
		print(growMethode)
		Pile().grow()
		del Pile.grow
		print(len(dir(Pile)))
		setattr(RefactorPile, 'grow', growMethode)
		RefactorPile().grow()

	def push(self, object):
		if self.isFull() :
			self.grow()
		else :
			self.contenu[self.index] = object
			self.index += 1


RefactorPile.do()
