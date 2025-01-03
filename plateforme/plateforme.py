class Plateforme:

	def __init__(self,x,y,largeur,hauteur):
		self.x = x
		self.y = y
		self.largeur = largeur
		self.hauteur = hauteur

	#Getters
	def getLargeur(self):
		return self.largeur
	def getHauteur(self):
		return self.hauteur
	def getX(self):
		return self.x
	def getY(self):
		return self.y

	#Setters
	def setLargeur(self,largeur):
		self.largeur = largeur
	def setHauteur(self,hauteur):
		self.hauteur = hauteur
	def setX(self,x):
		self.x = x
	def setY(self,y):
		self.y = y

	#déplace l'objet
	def deplacer(self,xPos,dx):
		if xPos >= 0 and xPos < 4430: #taille de la map ? 
			#print("je suis à l'intérieur")
			self.x -= dx

class Sol (Plateforme):

	def __init__(self,x,y,largeur,hauteur):
		super().__init__(x,y,largeur,hauteur)