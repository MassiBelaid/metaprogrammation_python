from Pile import Pile
import unittest
import random


class PileTest(unittest.TestCase):
	"""Classe qui va nous perlettre de tester la classe Pile"""

	def test_initialisation(self):
		"""test du constructeur"""
		tailleInitiale = random.randint(1,100)


		"""Création d'une pile de taille aléatoire"""
		p = Pile(tailleInitiale)

		"""Vérification des différente initialisations"""
		self.assertEqual(p.capacite, tailleInitiale)
		self.assertEqual(p.index, 0)
		self.assertTrue(p.isEmpty)


	def test_isEmpty(self):
		"""test methode isEmpty"""
		p = Pile()
		"""Vérification sur une pile tout juste crée avec taille par defaut"""
		self.assertTrue(p.isEmpty)

		"""Vérification exception levée lors appels a pop et push sur pile vide"""
		self.assertRaises(Exception, p.pop)
		self.assertRaises(Exception, p.top)



	def test_isFull(self):
		"""test methode isFull"""
		tailleInitiale = random.randint(1,100)
		"""Creéation pile avec taille aléatoire"""
		p = Pile(tailleInitiale)
		i = 0

		"""Remplissage au complet de la pile"""
		while i < tailleInitiale :
			p.push("test")
			i+=1
		self.assertTrue(p.isFull)
		"""Vérifcation exception levée lors appel à push sur pile pleine"""
		self.assertRaises(Exception, p.push)


	def test_push(self):
		"""test methode push"""

		p = Pile()
		"""génération d'un entier aléatoire, et le push dans notre pile"""
		aleaiInt = random.randint(1,100)
		p.push(aleaiInt)

		"""Vérification existance de cet objet dans la pile"""
		self.assertIn(aleaiInt, p.contenu)




	def test_pop(self):
		"""test methode pop"""

		p = Pile()
		"""génération d'un entier aléatoire, et le push dans notre pile"""
		aleaiInt = random.randint(1,100)
		p.push(aleaiInt)

		"""Suppression de cet dernier"""
		p.pop()

		"""Vérification de non existance de cet objet dans la pile"""
		self.assertNotIn(aleaiInt, p.contenu)




"""Lancez les tests"""
unittest.main()

