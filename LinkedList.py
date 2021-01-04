def TEST():
	print("call to affich")

Test = type('Meta', (None.__class__.__name__, ), dict(affiche=TEST))