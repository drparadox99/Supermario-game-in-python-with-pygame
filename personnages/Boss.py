import pygame
from  personnages.Personnage import Personnage
import random
from objets.Feu import Feu

class Boss(Personnage):

	def __init__(self,x,y,img):
		super().__init__(x,y,50,50) #calling the superclass,parent's class constructor to deal with the three parameeters instead refining them in the child class's constructor
		self.img = img
		self.compteurSaut = 12
		self.saut = False
		self.isVersDroite = False
		self.saut = False
		self.pasD = 0
		self.pasG = 0
		self.pdv = 5
		self.tabBoules = []
		self.compteurBoules = 0
		self.tirage = False
		self.dxBoss = 5
		self.superAttack = 0
		self.ultimate = False
		self.viesBoss = 10


	def getTirage(self):
		return self.tirage
	def setTirage(self, tirage):
		self.tirage = tirage
	def getTabBoules(self):
		return self.tabBoules
	def deleteBoules(self, obj):
		self.tabBoules.remove(obj)
	def getViesBoss(self):
		return self.viesBoss
	def setViesBoss(self,viesBoss):
		self.viesBoss = viesBoss


	#Permet au boss de se retourner si Mario est à sa droite /Reciproquement
	def findMario(self,mario):
		if mario.getX() > self.getX() and self.pasD <=20:
			self.isVersDroite = True
		else:
			self.isVersDroite = False

	def trouverMario(self, mario):
		if mario.getX() > self.getX():
			return "droite"
		elif mario.getX() < self.getX():
			return "gauche"

	def tirer(self, mario):
		if self.ultimate:
			self.ultimate = False
			feu = Feu(self.x +10, self.y +8, True, 'Images/Monde_3/superAttack.png')
			feu.setLargeur(24)
			feu.setHauteur(24)
			if self.trouverMario(mario) == "droite":
				self.tabBoules.append(feu)
			elif self.trouverMario(mario) == "gauche":
				feu.setDirectionDroite(False)
				self.tabBoules.append(feu)
		if self.tirage:
			rand = random.randint(10,32)
			if self.trouverMario(mario) == "droite":
				self.tabBoules.append(Feu(self.x +10, self.y +rand, True, 'Images/Monde_3/BossFeuDroite.png'))
			elif self.trouverMario(mario) == "gauche":
				self.tabBoules.append(Feu(self.x -10, self.y +rand,False, 'Images/Monde_3/BossFeuGauche.png'))
			#self.compteurBoules -= 1

	def bouger(self,dx):

		if self.getIsVersDroite() and self.pasD <= 10 :
			self.dxBoss = dx * 1
			self.pasD +=1
			if(self.pasD > 10):
				self.pasD = 0
				self.isVersDroite = False
		else:
			if self.pasG <= 10:
				self.dxBoss = dx * -1
				self.pasG += 1
				if(self.pasG > 10):
					self.pasG = 0
					self.isVersDroite = True
		self.setX(self.getX()+self.dxBoss)

	def getCentre(self):
		return self.centre
	def setCentre(self, centre):
		self.centre = centre
	def sauter(self,hauteurPlafond,ySol):
		strImg = " "
		rand = random.randint(0,10)
		if rand == 1 or self.saut:
			self.saut = True
			self.compteurSaut += 3
			#Montée du saut
			if self.compteurSaut <= 22:
				#mario monte de 4 pixels
				if self.y > hauteurPlafond: #vérification de la position y du plafond
					self.y = self.y - 10
				else:
					#on atteint  la hauteur maximale du saut
			        #on modifie compteurSaut pour éviter de rentrer de nouveau dans ce if et arrêter la montée du saut
					self.compteurSaut = 36
				#retourne l'image correspodante à son orientation
				if self.isVersDroite:
					strImg = "Images/Monde_3/bossDroite.png"
				else:
					strImg = "Images/Monde_3/bossGauche.png"

			#Retombé du saut de maio
			elif self.y + self.hauteur < ySol and self.y + self.hauteur  <= ySol: #vérification de la position y du sol
				#mario descend doucement vers le bas

				self.y = self.y + 7
				if not (self.y + self.hauteur < ySol and self.y + self.hauteur  <= ySol):
					self.saut=False
				#retourne l'image correspodante à son orientation
				if  self.isVersDroite:
					strImg ="Images/Monde_3/bossDroite.png"
				else:
					strImg = "Images/Monde_3/bossGauche.png"
				#saut terminé
			else:
				self.saut = False
				self.compteurSaut = 0
			#print("saut fini")
			#retourne l'image correspodante à son orientation
		if self.isVersDroite:
			strImg = "Images/Monde_3/bossDroite.png"
		else:
			strImg = "Images/Monde_3/bossGauche.png"
		#mise à jour de l'état du saut
		#remise  à zero du compteur du saut


		return strImg

	def proche(self,mario):
		self.compteurBoules -= 1
		if  mario.getX() >= self.x - 300  and mario.getX() <= self.x + 300:
			if self.superAttack == 50:
				self.superAttack =0
				self.ultimate = True
				self.compteurBoules = 100
				return True
			elif self.compteurBoules <=0:
				self.tirage = True
				self.compteurBoules = 25
				self.superAttack += 10
				return True
			else:
				return False
		else:
			return False
