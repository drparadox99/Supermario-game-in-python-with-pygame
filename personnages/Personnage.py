import pygame
from objets.Trou import Trou
class Personnage:
	#constructeur
	def __init__(self,x,y,largeur,hauteur):
		self.x = x
		self.y = y
		self.largeur = largeur
		self.hauteur = hauteur
		self.compteur = 0;
		self.marche = False
		self.isVersDroite = True
		self.vivant = True
		self.tabImgs = []


	#Getters
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def getLargeur(self):
		return self.largeur
	def getHauteur(self):
		return self.hauteur
	def getCompteur(self):
		return self.compteur
	def getMarche(self):
		return self.marche
	def getIsVersDroite(self):
		return self.isVersDroite
	def getVivant(self):
		return self.vivant

	#Setters
	def setX(self,x):
		self.x = x
	def setY(self,y):
		self.y = y
	def setLargeur(self,largeur):
		self.largeur = largeur
	def setHauteur(self,hauter):
		self.hauteur = hauteur
	def setMarche(self,marche):
		self.marche = marche
	def setCompteur(self,compteur):
		self.compteur = compteur
	def setIsVersDroite(self,isVersDroite):
		self.isVersDroite = isVersDroite
	def setVivant(self,vivant):
		self.vivant = vivant

	#création et retour des rectangles à partir des cordonnées |Hit Box ?|
	def retourneRectangle(self,x,y,largeur,hauteur):
		rectangle = pygame.Rect(x,y,largeur,hauteur)
		return rectangle
	#vérification de collision à gauche de mario (objet 2)
	def collisionGauche(self,obj1, obj2):
		rect1 = self.retourneRectangle(obj1.getX(),obj1.getY(),5,obj1.getHauteur())
		rect2 = self.retourneRectangle(obj2.getX()+obj2.getLargeur(),obj2.getY(),5,obj2.getHauteur())
		if(rect1.colliderect(rect2)):
			#if rect2.right >= rect1.left and not isinstance(obj2, Trou):
			return True
		else:
			return False
	#vérification de collision à droite de mario
	def collisionDroite(self,obj1, obj2):
		#if isinstance(obj1,Magic_Mushroom):
		rect1 = self.retourneRectangle(obj1.getX()+obj1.getLargeur(),obj1.getY(),5,obj1.getHauteur())
		rect2 = self.retourneRectangle(obj2.getX(),obj2.getY(),5,obj2.getHauteur())

		if(rect1.colliderect(rect2)):			
			return True
		else:
			return False
	#vérification de collision en dessous de mario
	def collisionDessous(self,obj1,obj2,game):
		'''
			pygame.draw.rect(game.gameFenetre,(3,3,4),(obj1.getX(),obj1.getY()+obj1.getHauteur(),obj1.getLargeur(),10))
			pygame.draw.rect(game.gameFenetre,(3,3,4),(obj2.getX(),obj2.getY()+obj2.getHauteur(),obj2.getLargeur(),10))
		'''
		rect1 =  self.retourneRectangle(obj1.getX(),obj1.getY()+obj1.getHauteur(),obj1.getLargeur(),10)
		rect2 = self.retourneRectangle(obj2.getX(),obj2.getY(),obj2.getLargeur(),10)
		if(rect1.colliderect(rect2)):
			return True
		else:
			return False


	#vérification de collision au dessus de mario
	def collisionDessus(self,obj1,obj2):
		rect1 = self.retourneRectangle(obj1.getX(),obj1.getY(),obj1.getLargeur(),10)
		rect2 = self.retourneRectangle(obj2.getX(),obj2.getY()+obj2.getHauteur(),obj2.getLargeur(),10)
		#pygame.draw.rect(game.gameFenetre,(3,3,4),(obj1.getX(),obj1.getY(),obj1.getLargeur(),10))
		#pygame.draw.rect(game.gameFenetre,(225,225,225),(obj2.getX(),obj2.getY()+obj2.getHauteur(),obj2.getLargeur(),10))
		if(rect1.colliderect(rect2)):
			return True
		else:
			return False

	def chute(self,obj1,obj2):
		if obj1.getX() > obj2.getX() and  obj1.getX()+obj1.getLargeur() < obj2.getX() + obj2.getLargeur():
			return True
		else:
			return False

	#fait marcher le personnage en renvoyant l'image appopriée
	def marcher(self,nom,frequence):
		strImg = " "
		#si mario ne bouge pas ou s'il se situe au point de départ
		if not self.marche:
			if self.isVersDroite:
				#strImg  = "Images/" + nom + "ArretDroite.png"
				strImg = self.tabImgs[1]
			else:
				#strImg = "Images/" + nom + "ArretGauche.png"
				strImg = self.tabImgs[0]
		else:
			#mario est en train de marcher
			self.compteur = self.compteur + 1
            #Le compteur sert à determiner la vitesse d'alternance entre deux Images de mario pendant son déplacement
            #pendant l'alternance, on envoie compteur fois une image avant de faire pareil avec la deuxième
			if int(self.compteur / frequence) == 0:
				if self.isVersDroite:
				  	#strImg = "Images/" + nom + "ArretDroite.png"
					strImg = self.tabImgs[1]
				else:
					#strImg = "Images/" + nom + "ArretGauche.png"
					strImg = self.tabImgs[0]
			else:
				if self.isVersDroite:
				 	#strImg = "Images/" +nom+ "MarcheDroite.png"
					strImg = self.tabImgs[3]
				else:
				 	#strImg = "Images/" + nom + "MarcheGauche.png"
					strImg = self.tabImgs[2]
			if self.compteur == 2*frequence:
				self.compteur = 0
		return strImg

	#permet la déctection des collisions qu'entre les objets proches
	def proche(self,objet):
		if self.x > objet.getX()-10 and self.x < objet.getX()+objet.getLargeur()+10 or self.x + self.largeur > objet.getX()-10 and self.x+self.largeur < objet.getX()+objet.getLargeur()+10:
			return True
		else:
			return False

	#déplacement du personnage en fonction du déplacement du font(provoqué par le déplacement de mario)
	def deplacer(self,xPos,dx):
		if xPos >= 0 and xPos < 4430:
			self.x -= dx
