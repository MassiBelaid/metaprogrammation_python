class SalleDeCoursSingleton(type):
	"""La méta classe"""
	"""liste qui va contenire toute les instances de pile"""
	_instances = list()
	n = 5

	def __call__ (cls, *args, **kwargs):
		if len(cls._instances)+1 < cls.n :
			instanceCree = super(SalleDeCoursSingleton, cls).__call__(*args, **kwargs)
			cls._instances.append(instanceCree)
			return instanceCree
		else :
			raise Exception("Impossible, nombre de salles disponibles atteint")



class SalleDeCours(metaclass = SalleDeCoursSingleton):
	pass