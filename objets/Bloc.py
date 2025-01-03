from  objets.Objet import Objet

class Bloc(Objet):
	def __init__(self,x,y):
		super().__init__(x,y,30,30,"Images/Monde_1/bloc.png")
		self.contenu_vide = False
		self.casse = False
	def getCasse(self):
		return self.casse
	def setCasse(self,casse):
		self.casse = casse

class Bloc_Nazo(Bloc):
	def __init__(self,x,y):
		super().__init__(x,y)
		self.imgObjet = "Images/Monde_1/bloc_nazo.png"
	def setVide(self,contenu_vide):
		self.contenu_vide = contenu_vide
	def getVide(self):
		return self.contenu_vide
	def changeImg(self):
		self.imgObjet = "Images/Monde_1/bloc_nazo_vide.png"
