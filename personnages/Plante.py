from  personnages.Personnage import Personnage

class Plante(Personnage):
	def __init__(self,x,y):
		super().__init__(x+6,y+20,16,23)
		self.imgObjet = "Images/Monde_1/planteFermee.png"
		self.hauteurMax = 0
		self.zenith = False
		self.mod = 0


	def getImgObjet(self):
		return self.imgObjet
	def bouger(self):
		self.mod += 1
		if not self.zenith:
			self.hauteurMax += 1
			if self.mod % 4 == 0:
				self.imgObjet = "Images/Monde_1/planteFermee.png"
				self.y -= 1
			else:
				self.imgObjet ="Images/Monde_1/planteOuverte.png"
				self.y -= 1
		else:
			self.hauteurMax -= 1
			self.y += 1
			if self.mod % 4 == 0:
				self.imgObjet = "Images/Monde_1/planteFermee.png"
			else:
				self.imgObjet = "Images/Monde_1/planteOuverte.png"
		if self.hauteurMax == 25:
			self.zenith = True
		if self.hauteurMax == -10:
			self.zenith = False
