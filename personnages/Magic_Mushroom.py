from  personnages.Personnage import Personnage
from  objets.Sol import Sol
import pygame
class Magic_Mushroom(Personnage):

	def __init__(self,x,y):
		super().__init__(x,y,16,16) #calling the superclass,parent's class constructor to deal with the three parameeters instead refining them in the child class's constructor
		self.isVersDroite = True
		self.cache = True
		self.imgMagicMushroom = 'Images/Monde_1/magic_mushroom.png'
		self.dx = 2
		self.collisionTrouvee = False
		self.SolTrouve = False

	def setCache(self,droite):
		self.cache = droite
	def getCache(self):
		return self.cache
	def getImgMagicMushroom(self):
		return self.imgMagicMushroom

	def bouger(self, monde,game):
		tabObjets = monde.getTabObjets()
		for objet in tabObjets:
			#pygame.draw.rect(game.gameFenetre,(225,225,225),(objet.getX(),objet.getY(),objet.getLargeur(),objet.getHauteur()))
			self.collisionTrouvee = self.collisionDessous(self,objet,game)
			if self.y < monde.getSolAbsolu()- 12 and not self.collisionTrouvee :
				self.collisionTrouvee = False
				self.SolTrouve = False
			else:
				if self.collisionTrouvee and not isinstance(objet,Sol):
					self.SolTrouve = False
					self.collisionTrouvee = True
					if self.getIsVersDroite():
						self.dx = 4
					else:
						self.dx = -4
					self.x = self.x + self.dx
					break
				else:
					self.SolTrouve = True
					self.collisionTrouvee = False
				if self.SolTrouve or self.collisionTrouvee:
					if self.proche(objet):
						self.contactMushroom(objet)
					if self.getIsVersDroite():
						self.dx = 3
					else:
						self.dx = -3
		if not self.collisionTrouvee and not self.SolTrouve:
			self.y = self.y + 3
		if self.SolTrouve and not self.collisionTrouvee:
			self.y = monde.getSolAbsolu() - 6
		if self.collisionTrouvee and not self.SolTrouve:
			self.y  = objet.y - 15
		if self.SolTrouve:
			self.x = self.x + self.dx



	def contactMushroom(self,objet):
		if self.collisionDroite(self,objet) and self.getIsVersDroite():
			self.setIsVersDroite(False)
			self.dx = -2
		else:
			if self.collisionGauche(self,objet) and not  self.getIsVersDroite():
				self.setIsVersDroite(True)
				self.dx = 2
