import pygame
class Objet:

	def __init__(self,x,y,largeur,hauteur,imgObjet=None):
		self.x = x
		self.y = y
		self.largeur = largeur
		self.hauteur = hauteur
		self.imgObjet = imgObjet
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
			self.x -= dx

	def getImgObjet(self):
		return self.imgObjet
	def setImgObjet(self, imgObjet):
		self.imgObjet = imgObjet
	def retourneRectangle(self,x,y,largeur,hauteur):
		rectangle = pygame.Rect(x,y,largeur,hauteur)
		return rectangle
