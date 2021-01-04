class Pile:
	"""Implémentation de la classe Pile vue en TP"""

	def __new__(cls, taille=None):
		"""méthode new qui initialise la variable static tailleDefaut"""
		cls.tailleDefaut = 5
		return object.__new__(cls)

	@classmethod
	def GET_TAILLE_DEFAUT(cls):
		"""Methode static qui retourne la valeur de la variable static tailleDefaut"""
		return 5


	def __init__(self, taille=None):
		"""ainsi le contructeur devient"""
		if taille is None :
			"""si pas de taille"""
			taille = Pile.GET_TAILLE_DEFAUT()
		self.index = 0
		self.capacite = taille
		self.contenu = [None] * self.capacite

	def isEmpty(self) :
		return self.index == 0

	def isFull(self) :
		return self.index == self.capacite

	def push(self, object):
		if self.isFull() :
			raise Exception("Impossible d'empiler sur une pile pleine")
		else :
			self.contenu[self.index] = object
			self.index += 1

	def pop(self) :
		if self.isEmpty():
			raise Exception("Impossible du une pile vide")
		else :
			self.index -= 1
			self.contenu[self.index] = None

	def top(self) :
		if self.isEmpty():
			raise Exception("Impossible du une pile vide")
		else :
			return self.contenu[self.index - 1]

	def printOn(self):
		c = ""
		for cont in self.contenu :
			if cont is not None :
				c = "{} {}".format(c, cont)
		print("une pile de taille {}, contenant {} objets : ({})".format(self.capacite, self.index, c))

	def grow(self):
		self.capacite += 1
		self.contenu += [None]