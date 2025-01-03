#from Personnage import Personnage


from  personnages.Personnage import Personnage
from  personnages.Tortue import Tortue
from  personnages.Plante import Plante
import pygame
from objets.Trou import Trou
from objets.Sol import Sol
from objets.Bloc import Bloc
from objets.Bloc import Bloc_Nazo
from objets.Boule import Boule
from personnages.Magic_Mushroom import Magic_Mushroom

class Mario(Personnage):

	def __init__(self,x,y):
		super().__init__(x,y,20,26) #calling the superclass,parent's class constructor to deal with the three parameeters instead refining them in the child class's constructor
		self.compteurSaut = 12
		self.saut = False
		self.compteurSaut = 0
		self.tombe = False
		self.SoundTracksTab = ["SoundTracks/main.ogg","SoundTracks/end.ogg","SoundTracks/break.wav" ]
		self.pieces = 0
		self.viesDeMario = 3
		self.tabBoules = []
		self.compteurBoule = 1
		self.tabImgs = ["Images/Mario/marioArretGauche.png","Images/Mario/marioArretDroite.png","Images/Mario/marioMarcheGauche.png","Images/Mario/marioMarcheDroite.png","Images/Mario/marioSautGauche.png","Images/Mario/marioSautDroite.png","Images/Mario/MarioMeurt.png"]
		self.img = self.tabImgs[3]
		self.tirage = False
		self.soundTrack = None
		self.playMusik("play")
		self.mortFatale = False
		self.compteurMortel = 0


	#Getter
	def getImg(self):
		return self.img
	def getCompteurSaut(self):
		return self.compteurSaut
	def getSaut(self):
		return self.saut
	def getTombe(self):
		return self.tombe
	def getTabBoules(self):
		return self.tabBoules
	def getTirage(self):
		return self.tirage
	def getMorteFatale(self):
		return self.mortFatale
	def setMortFatale(self,mortFatale):
		self.mortFatale = mortFatale

	#Setter
	def setImg(self,img):
		self.imgMario = imgMario
	def setCompteurSaut(self,compteur):
		self.compteurSaut = compteur
	def setSaut(self, saut):
		self.saut = saut
	def setTombe(self, tombe):
		self.tombe = tombe
	def playMusik(self,etat,track=None):
		if track == None:
			if etat == "play":
				self.soundTrack = pygame.mixer.Sound(self.SoundTracksTab[0]).play()
			else:
				print("le stop")
				self.soundTrack.stop()
		else:
			pygame.mixer.Sound(track).play()
	def getPieces(self):
		return self.pieces
	def setPieces(self,pieces):
		self.pieces = pieces
	def getVieDeMario(self):
		return self.viesDeMario
	def setVieDeMario(self,viesDeMario):
		self.viesDeMario = viesDeMario
	def setTirage(self,tirage):
		self.tirage = tirage

	def tomber(self, hauteurPlafond, ySol):
		strImg = " "
		if self.y + self.hauteur < ySol and self.y + self.hauteur  <= ySol: #vérification de la position y du sol
			#mario descend doucement vers le bas
			self.y = self.y + 7
			#retourne l'image correspodante à son orientation
			if  self.isVersDroite:
				strImg = self.tabImgs[5]
			else:
				strImg = self.tabImgs[4]
		else:
			#retourne l'image correspodante à son orientation
			if self.isVersDroite:
				strImg = self.tabImgs[1]
			else:
				strImg = self.tabImgs[0]
			#mise à jour de l'état du saut
			self.tombe = False
			#remise  à zero du compteur du saut
		return strImg



	def tirer(self,sol,vitesse):
		#boule = self.tabBoules[0]
		strImg = ""
		self.compteurBoule += 1
		#if self.compteurBoule <= 25:
		for boule in self.tabBoules:
			if boule.getRebondissement() > 0:
				if not boule.getAscendance():
					if boule.getY() <= sol:
						boule.setY( boule.getY() + vitesse)
						if boule.getDirectionDroite():
							boule.setX( boule.getX() + vitesse )
						else:
							boule.setX( boule.getX() + vitesse * -1)
						return "Images/Mario/Boules/boule0.png"
					else:
						boule.setRebondissement(boule.getRebondissement()- 1)
						boule.setAscendance(True)
						return "Images/Mario/Boules/boule1.png"
				if boule.getAscendance():
					if boule.getY() >= sol - 12:
						boule.setY( boule.getY() - vitesse)
						if boule.getDirectionDroite():
							boule.setX( boule.getX() + vitesse)
						else:
							boule.setX( boule.getX() + vitesse * -1)
						return "Images/Mario/Boules/boule2.png"
					else:
						boule.setRebondissement(boule.getRebondissement()- 1)
						boule.setAscendance(False)
						return "Images/Mario/Boules/boule3.png"
			else:
				self.tirage = False
				self.tabBoules.clear()
				return "Images/Mario/Boules/boule0.png"

	def perdreVie(self,sol,game):
		self.compteurMortel += 3
		self.img = self.tabImgs[6]
		if self.compteurMortel < 42:
			self.y = self.y - 10
		else:
			self.y = self.y + 10
		if self.y > sol + 20:
			self.mortFatale = False
			self.saut = False
			self.viesDeMario += -1
			self.compteurMortel = 3
			game.setTransition(True)
		return self.img

	def sauter(self,hauteurPlafond,ySol):
		strImg = " "
		self.compteurSaut += 3
		#Montée du saut
		if self.compteurSaut <= 32:
			#mario monte de 4 pixels
			if self.y > hauteurPlafond: #vérification de la position y du plafond
				self.y = self.y - 10
			else:
				#on atteint  la hauteur maximale du saut
                #on modifie compteurSaut pour éviter de rentrer de nouveau dans ce if et arrêter la montée du saut
				self.compteurSaut = 36
			#retourne l'image correspodante à son orientation
			if self.isVersDroite:
				strImg = self.tabImgs[5]
			else:
				strImg = self.tabImgs[4]

		#Retombé du saut de maio
		elif self.y + self.hauteur < ySol and self.y + self.hauteur  <= ySol: #vérification de la position y du sol
			#mario descend doucement vers le bas
			self.tombe = True
			self.y = self.y + 7
			#retourne l'image correspodante à son orientation
			if  self.isVersDroite:
				strImg = self.tabImgs[5]
			else:
				strImg = self.tabImgs[4]
		else:
			#retourne l'image correspodante à son orientation
			if self.isVersDroite:
				strImg = self.tabImgs[1]
			else:
				strImg = self.tabImgs[0]
			#mise à jour de l'état du saut
			self.saut = False
			#remise  à zero du compteur du saut
			self.compteurSaut = 0
		return strImg

	#gère toutes les autres collisions
	def contact(self,mario,objet,monde):
			#collision gauche et droite de mario
		if self.collisionDroite(mario,objet) and mario.getIsVersDroite() and not isinstance(objet,Trou) or self.collisionGauche(mario,objet) and not  mario.getIsVersDroite() and not isinstance(objet,Trou):
			monde.setDx(0)
			mario.setMarche(False)
		#collsion en dessous de mario
		#Si collision en dessous et mario est en train de tombe
		if self.collisionDessous(mario,objet,monde):
			if mario.getTombe():
				if isinstance(objet, Trou) and mario.chute(mario,objet): #si trou = tombe a l'infini
					monde.setYSol(500)
					mario.tombe = True
					mario.tomber(monde.getHauteurPlafond(), monde.getYSol())
				else: #sinon se receptionne sur la plate forme
					if mario.getY()+mario.getHauteur() < objet.getY():
						monde.setYSol(objet.getY())
						#print("sur un objet")
						mario.setY(monde.getYSol()-mario.getHauteur())
			#Si collision en dessous et mario n'est pas en train de tomber
			elif not mario.getTombe():
				if isinstance(objet, Trou) and mario.chute(mario,objet):
					monde.setYSol(500)
					mario.tombe = True
					mario.tomber(monde.getHauteurPlafond(), monde.getYSol())
				else:
					mario.setY(objet.getY()-mario.getHauteur())
					monde.setYSol(objet.getY())
		elif not self.collisionDessous(mario,objet,monde)  and not isinstance(objet, Sol) and not isinstance(objet, Trou):
				#Verifie si il n'y a aucune collision sous Mario (donc pas de "sol")
				#Si c'est le cas on remet le sol à la valeur du sol
				monde.setYSol(monde.getSolAbsolu())
				self.tombe = True
				#fait descendre mario lorqu'il a déja monté sur objet sans sauter
				if not mario.getSaut() and mario.getTombe():
					mario.tomber(monde.getHauteurPlafond(),monde.getYSol()),(mario.getX(),mario.getY())
			  #au cas où mario est monté sur un objet

				#Collision au dessus de mario
		if self.collisionDessus(mario,objet) and mario.y >= objet.getY()+objet.getHauteur():
			self.playMusik("play",self.SoundTracksTab[2])
			monde.setHauteurPlafond(objet.getY()+objet.getHauteur())
			if isinstance(objet, Bloc_Nazo):
				if not objet.getVide():
					#self.changerEtat = False
					monde.getTabPersonnages().append(Magic_Mushroom(objet.getX()+8,objet.getY() -20))
					objet.setVide(True)
					#monde.getTabObjets().remove(objet)
			if isinstance(objet,Bloc) and not isinstance(objet,Bloc_Nazo):
				objet.setCasse(True)
				#remet la hauteur du plafond, à la suite d'une collsion
		elif not self.collisionDessus(mario,objet) and not mario.getSaut():
			monde.setHauteurPlafond(0)

	#détection de contact entre mario et des pièces d'or
	def contactAbsolu(self,obj1,obj2):
		rect1 = self.retourneRectangle(obj1.getX(),obj1.getY(),obj1.getLargeur(),obj1.getHauteur())
		rect2 = self.retourneRectangle(obj2.getX(),obj2.getY(),obj2.getLargeur(),obj2.getHauteur())
		if(rect1.colliderect(rect2)):
			return True
		else:
			return False

	def contactPlante(self,plante):
		if (self.contactAbsolu(self,plante)):
			self.mortFatale = True
			self.saut = True


    #contact entre mario et des personnages comme la tortue
	def contactPersonnage(self,personnage,game):
		if isinstance(personnage,Plante):
			self.contactPlante(personnage)
		else:
			#pygame.draw.rect(game.gameFenetre,(3,3,4),(personnage.getX(),personnage.getY(),personnage.getLargeur(),personnage.getHauteur()))
			if self.collisionGauche(self,personnage) or self.collisionDroite(self,personnage):
				if isinstance(personnage,Tortue):
					if personnage.getCachee() :
						personnage.setWalkingDead(True)
						if(self.collisionGauche(self,personnage)):
							personnage.setIsVersDroite(False)
						else:
							if(self.collisionDroite(self,personnage)):
								personnage.setIsVersDroite(True)
				#if isinstance(personnage,Tortue) and personnage.getCachee():
				if not isinstance(personnage,Tortue) or not personnage.getCachee():
					self.mortFatale = True
					self.saut = True
			else:
				if self.collisionDessous(self,personnage,game):
					if(isinstance(personnage,Tortue)):
						personnage.setCachee(True)
					if(self.getX() - 2 < personnage.getX()):
						personnage.setX(personnage.getX() + 30)
					else:
						personnage.setX(personnage.getX()- 30)
					personnage.setMarche(False)
					if not isinstance(personnage,Tortue):
						personnage.setVivant(False)



class BigMario(Mario):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.tabImgs = ["Images/Mario/BigMarioArretGauche.png","Images/Mario/BigMarioArretDroite.png","Images/Mario/BigMarioMarcheGauche.png","Images/Mario/BigMarioMarcheDroite.png","Images/Mario/BigMarioSautGauche.png","Images/Mario/BigMarioSautDroite.png","Images/Mario/MarioMeurt.png"]
        self.img = self.tabImgs[3]
        self.largeur = 16
        self.hauteur = 32
        self.soundTrack.stop()
#help(importlib.util.spec_from_file_location)
class SuperMario(BigMario):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.tabImgs = ["Images/Mario/superMarioArretGauche.png","Images/Mario/superMarioArretDroite.png","Images/Mario/superMarioMarcheGauche.png","Images/Mario/superMarioMarcheDroite.png","Images/Mario/superMarioSautGauche.png","Images/Mario/superMarioSautDroite.png","Images/Mario/MarioMeurt.png"]
        self.img = self.tabImgs[3]
        self.largeur = 16
        self.hauteur = 32
        self.soundTrack.stop()
