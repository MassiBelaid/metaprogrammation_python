from Pile import Pile
import inspect

class RefactorPile(Pile):
	def __new__(cls, taille=None):
		cls.tailleDefaut = 5
		return object.__new__(cls)
	
	@classmethod
	def do(cls):
		"""Création dynamiquement de la classe PileGrossissante"""
		PileGrossissante = type('PileGrossissante',(Pile, ), dict())

		"""Récupérer la mehode grow de la class Pile"""
		for fun in inspect.getmembers(Pile, inspect.isfunction) :
			if fun[0] == 'grow' :
				growMethode = fun[1]

		"""Suppression de grow de Pile"""
		del Pile.grow
		"""ajout pour la classe RefacorPile la méthode récupéréé"""
		setattr(RefactorPile, 'grow', growMethode)

	def push(self, object):
		"""redefintion de push"""
		if self.isFull() :
			self.grow()
		else :
			self.contenu[self.index] = object
			self.index += 1

