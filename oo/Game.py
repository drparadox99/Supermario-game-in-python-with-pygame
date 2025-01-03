import pygame
import time
import random
from personnages.Personnage import Personnage
from personnages.Mario import Mario
from personnages.Mario import SuperMario
from personnages.Mario import BigMario
from objets.Piece import Piece
from personnages.Champignon import Champignon
from personnages.Tortue import Tortue
from objets.TuyauRouge import TuyauRouge
from objets.Trou import Trou
from objets.Bloc import Bloc
from objets.Bloc import Bloc_Nazo
from objets.Murs import Murs
from objets.Sol import Sol
from objets.Boule import Boule
from personnages.Plante import Plante
from personnages.Magic_Mushroom import Magic_Mushroom
import pickle
import copy



class Monde_2:
	#constructeur de la classe Game
	def __init__(self):
		#initialise le module pygame
		#pour le décalage des images fixes du fond
		self.dx = 0
		#position x de la première image du fond
		self.xFond1 = -50
		#postion x de la deuxième image du fond
		self.xFond2 = 1610
		#emplacement de l'image du fond
		#self.strImgFond = "Images/Monde_1/fondEcran.png"
		self.strImgFond = "Images/World2_1.png"
		#img du château
		self.imgChateau = "Images/Monde_1/chateau1.png"
		#img du pancard de depart
		self.imgDepart = "Images/Monde_1/depart.png"
		#position absolue de mario dans le jeu à partir du point de depart qui est egal à 0
		self.xPos = -1
		#la position y du sol
		self.ySol = 294
		#la position y du plafond
		self.hauteurPlafond = 0
		#image du chateau de fin
		self.imgChateauFin = "Images/Monde_1/chateauFin.png"
		#image drapeau de fin
		self.imgDrapeau = "Images/Monde_1/drapeau.png"
		self.tabObjetsTxt = ["Positionnements/Monde_2/murs.txt","Positionnements/Monde_2/tuyau.txt","Positionnements/Monde_2/bloc.txt","Positionnements/Monde_2/bloc_nazo.txt","Positionnements/Monde_2/trou.txt","Positionnements/Monde_2/sol.txt"]
		self.tabPersTxt = ["Positionnements/Monde_2/champignon.txt","Positionnements/Monde_2/tortue.txt","Positionnements/Monde_2/plante.txt"]
		self.tabObjets = []
		self.tabPersonnages = []
		self.tabPieces = []
		self.time = 90
		self.solAbsolu = 301
		self.peupler()

	#Getters
	def getDx(self):
		return self.dx
	def getxFond1(self):
		return self.xFond1
	def getxFond2(self):
		return self.xFond2
	def getStrImgFond(self):
		return self.strImgFond
	def getXPos(self):
		return self.xPos
	def getImgChateau(self):
		return self.imgChateau
	def getImgDepart(self):
		return self.imgDepart
	def getHauteurPlafond(self):
		return self.hauteurPlafond
	def getYSol(self):
		return self.ySol
	def getimgChateauFin(self):
		return self.imgChateauFin
	def getimgDrapeau(self):
		return self.imgDrapeau
	def getTime(self):
		return self.time
	def getSolAbsolu(self):
		return self.solAbsolu
	def getTabPersonnages(self):
		return self.tabPersonnages
	def getTabObjets(self):
		return self.tabObjets
	def getTabPieces(self):
		return self.tabPieces

	#Setters
	def setDx(self,dx):
		self.dx = dx
	def setHauteurPlafond(self,hauteurPlafond):
		self.hauteurPlafond = hauteurPlafond
	def setYSol(self,ySol):
		self.ySol = ySol
	def setXPos(self,xPos):
		self.xPos = xPos
	def setXFond1(self,xFond1):
		self.xFond1 = xFond1
	def setXFond2(self,xFond2):
		self.xFond2 = xFond2
	def setTime(self,time):
		self.time = time
	def setSolAbsolu(self,solAbsolu):
		self.solAbsolu = solAbsolu
	def setTabObjet(self,tabObjets):
		self.tabObjets = tabObjets


	#déplacement des objets 'fixes' du jeu
	def deplacementFond(self):
		if self.xPos >= 0 and self.xPos <= 4430:
			#mise à jour de la position absolue
			self.xPos += self.dx
			#déplacement du fond de l'écran
			self.xFond1 = self.xFond1 - self.dx;
			self.xFond2 = self.xFond2 - self.dx;
		#alternance entre les deux images du fond
		if self.xFond1 <= -1665:
			self.xFond1 = 1665
		elif self.xFond2 <= -1665:
				self.xFond2 = 1665
		elif self.xFond1 >= 1665:
				self.xFond1 = -1665
		elif self.xFond2 >= 1665:
			 	self.xFond2 = -1665

	def peupler(self):
		for fichier in self.tabObjetsTxt:
			fr = open(fichier,'r')
			text = fr.read()
			cordsTab = []
			for i in text.split():
				cordsTab.append(i)
				if fichier == "Positionnements/Monde_2/sol.txt":
					tabTuples = zip(cordsTab[0::4], cordsTab[1::4], cordsTab[2::4], cordsTab[3::4])
					for x,y,l,h in tabTuples:
						self.tabObjets.append(Sol(int(x) ,int(y), int(l), int(h)))
				else:
					tabTuples =  zip(cordsTab[0::2], cordsTab[1::2])
					for x,y in tabTuples:
						if fichier == "Positionnements/Monde_2/murs.txt":
							self.tabObjets.append(Murs(int(x),int(y)))
						if fichier == "Positionnements/Monde_2/tuyau.txt":
							self.tabObjets.append(TuyauRouge(int(x),int(y)))
						if fichier == "Positionnements/Monde_2/bloc.txt":
							self.tabObjets.append(Bloc(int(x),int(y)))
						if fichier == "Positionnements/Monde_2/bloc_nazo.txt":
							self.tabObjets.append(Bloc_Nazo(int(x),int(y)))
						if fichier == "Positionnements/Monde_2/trou.txt":
							self.tabObjets.append(Trou(int(x) ,int(y)))

		#on ouvre le fichier piece.txt contenant les Coordonnées des pièces sur l'écran
		fr = open("Positionnements/Monde_2/piece.txt",'r')
		text = fr.read()

		#on remplit le fichier piece.txt contentant les coordonnées des pièces sur l'écran
		cordsPiece = []

		#on crée un tuple(x,y) à partir de la liste
		for i in text.split():
		    cordsPiece.append(i)
		pieces = zip(cordsPiece[0::2], cordsPiece[1::2])

		for fichier in self.tabPersTxt:
			fr = open(fichier,'r')
			text = fr.read()
			cordsTab = []
			for i in text.split():
				cordsTab.append(i)
			tabTuples =  zip(cordsTab[0::2], cordsTab[1::2])
			for x,y in tabTuples:
				if fichier == "Positionnements/Monde_2/champignon.txt":
					self.tabPersonnages.append(Champignon(int(x) ,int(y)))
				if fichier == "Positionnements/Monde_2/tortue.txt":
					self.tabPersonnages.append(Tortue(int(x) ,int(y)))
				if fichier == "Positionnements/Monde_2/plante.txt":
					self.tabPersonnages.append(Plante(int(x),int(y)))
		fr.close
		#on crée une liste d'objets Tuyau,Bloc et des pièces d'or
		for x,y in pieces:
			self.tabPieces.append(Piece(int(x),int(y)))



##remettre tous les compteurs à 0 ! ! !

class Monde_1:
	#constructeur de la classe Game
	def __init__(self):
		#initialise le module pygame
		#pour le décalage des images fixes du fond
		self.dx = 0
		#position x de la première image du fond
		self.xFond1 = -50
		#postion x de la deuxième image du fond
		self.xFond2 = 750
		#emplacement de l'image du fond
		self.strImgFond = "Images/Monde_1/fondEcran.png"
		#img du château
		self.imgChateau = "Images/Monde_1/chateau1.png"
		#img du pancard de depart
		self.imgDepart = "Images/Monde_1/depart.png"
		#position absolue de mario dans le jeu à partir du point de depart qui est egal à 0
		self.xPos = -1
		#la position y du sol
		self.ySol = 294
		#la position y du plafond
		self.hauteurPlafond = 0
		#image du chateau de fin
		self.imgChateauFin = "Images/Monde_1/chateauFin.png"
		#image drapeau de fin
		self.imgDrapeau = "Images/Monde_1/drapeau.png"
		self.tabObjetsTxt = ["Positionnements/Monde_1/murs.txt","Positionnements/Monde_1/tuyau.txt","Positionnements/Monde_1/bloc.txt","Positionnements/Monde_1/bloc_nazo.txt","Positionnements/Monde_1/trou.txt","Positionnements/Monde_1/sol.txt"]
		self.tabPersTxt = ["Positionnements/Monde_1/champignon.txt","Positionnements/Monde_1/tortue.txt","Positionnements/Monde_1/plante.txt"]
		self.tabObjets = []
		self.tabPersonnages = []
		self.tabPieces = []
		self.time = 90
		self.solAbsolu = 285
		self.peupler()

	#Getters
	def getDx(self):
		return self.dx
	def getxFond1(self):
		return self.xFond1
	def getxFond2(self):
		return self.xFond2
	def getStrImgFond(self):
		return self.strImgFond
	def getXPos(self):
		return self.xPos
	def getImgChateau(self):
		return self.imgChateau
	def getImgDepart(self):
		return self.imgDepart
	def getHauteurPlafond(self):
		return self.hauteurPlafond
	def getYSol(self):
		return self.ySol
	def getimgChateauFin(self):
		return self.imgChateauFin
	def getimgDrapeau(self):
		return self.imgDrapeau
	def getTime(self):
		return self.time
	def getSolAbsolu(self):
		return self.solAbsolu
	def getTabPersonnages(self):
		return self.tabPersonnages
	def getTabObjets(self):
		return self.tabObjets
	def getTabPieces(self):
		return self.tabPieces

	#Setters
	def setDx(self,dx):
		self.dx = dx
	def setHauteurPlafond(self,hauteurPlafond):
		self.hauteurPlafond = hauteurPlafond
	def setYSol(self,ySol):
		self.ySol = ySol
	def setXPos(self,xPos):
		self.xPos = xPos
	def setXFond1(self,xFond1):
		self.xFond1 = xFond1
	def setXFond2(self,xFond2):
		self.xFond2 = xFond2
	def setTime(self,time):
		self.time = time
	def setSolAbsolu(self,solAbsolu):
		self.solAbsolu = solAbsolu
	def setTabObjet(self,tabObjets):
		self.tabObjets = tabObjets


	#déplacement des objets 'fixes' du jeu
	def deplacementFond(self):
		if self.xPos >= 0 and self.xPos <= 4430:
			#mise à jour de la position absolue
			self.xPos += self.dx
			#déplacement du fond de l'écran
			self.xFond1 = self.xFond1 - self.dx;
			self.xFond2 = self.xFond2 - self.dx;
		#alternance entre les deux images du fond
		if self.xFond1 <= -800:
			self.xFond1 = 800
		elif self.xFond2 <= -800:
				self.xFond2 = 800
		elif self.xFond1 >= 800:
				self.xFond1 = -800
		elif self.xFond2 >= 800:
			 	self.xFond2 = -800

	def peupler(self):
		for fichier in self.tabObjetsTxt:
			fr = open(fichier,'r')
			text = fr.read()
			cordsTab = []
			for i in text.split():
				cordsTab.append(i)
				if fichier == "Positionnements/Monde_1/sol.txt":
					tabTuples = zip(cordsTab[0::4], cordsTab[1::4], cordsTab[2::4], cordsTab[3::4])
					for x,y,l,h in tabTuples:
						self.tabObjets.append(Sol(int(x) ,int(y), int(l), int(h)))
				else:
					tabTuples =  zip(cordsTab[0::2], cordsTab[1::2])
					for x,y in tabTuples:
						if fichier == "Positionnements/Monde_1/murs.txt":
							self.tabObjets.append(Murs(int(x),int(y)))
						if fichier == "Positionnements/Monde_1/tuyau.txt":
							self.tabObjets.append(TuyauRouge(int(x),int(y)))
						if fichier == "Positionnements/Monde_1/bloc.txt":
							self.tabObjets.append(Bloc(int(x),int(y)))
						if fichier == "Positionnements/Monde_1/bloc_nazo.txt":
							self.tabObjets.append(Bloc_Nazo(int(x),int(y)))
						if fichier == "Positionnements/Monde_1/trou.txt":
							self.tabObjets.append(Trou(int(x) ,int(y)))

		#on ouvre le fichier piece.txt contenant les Coordonnées des pièces sur l'écran
		fr = open("Positionnements/Monde_1/piece.txt",'r')
		text = fr.read()

		#on remplit le fichier piece.txt contentant les coordonnées des pièces sur l'écran
		cordsPiece = []

		#on crée un tuple(x,y) à partir de la liste
		for i in text.split():
		    cordsPiece.append(i)
		pieces = zip(cordsPiece[0::2], cordsPiece[1::2])

		for fichier in self.tabPersTxt:
			fr = open(fichier,'r')
			text = fr.read()
			cordsTab = []
			for i in text.split():
				cordsTab.append(i)
			tabTuples =  zip(cordsTab[0::2], cordsTab[1::2])
			for x,y in tabTuples:
				if fichier == "Positionnements/Monde_1/champignon.txt":
					self.tabPersonnages.append(Champignon(int(x) ,int(y)))
				if fichier == "Positionnements/Monde_1/tortue.txt":
					self.tabPersonnages.append(Tortue(int(x) ,int(y)))
				if fichier == "Positionnements/Monde_1/plante.txt":
					self.tabPersonnages.append(Plante(int(x),int(y)))
		fr.close
		#on crée une liste d'objets Tuyau,Bloc et des pièces d'or
		for x,y in pieces:
			self.tabPieces.append(Piece(int(x),int(y)))



class  Main:
	def __init__(self,titre,WINDOW_WIDTH,WINDOW_HEIGHT,monde=None,mario=None):
		pygame.init()
		self.WINDOW_WIDTH = WINDOW_WIDTH
		self.WINDOW_HEIGHT = WINDOW_HEIGHT
		self.gameFenetre = pygame.display.set_mode((self.WINDOW_WIDTH,self.WINDOW_HEIGHT))
		pygame.key.set_repeat(300,200)
		self.clock = pygame.time.Clock()
		self.font1 = pygame.font.Font("Fonts/font1.ttf", 15)
		self.font2 = pygame.font.Font("Fonts/font3.ttf", 25)
		self.font3 = pygame.font.Font("Fonts/font2.ttf", 15)
		self.font4 = pygame.font.Font("Fonts/font3.ttf", 17)
		self.FPS = 30
		pygame.display.set_caption(titre)
		self.monde = monde
		self.mario = mario
		#self.time = 90
		self.provisoire = 0
		self.intro = True
		self.regles = False
		self.languageMenu = False
		self.langue = "Fr"
		self.hudEn = ["Score : ","Time : ", "Lives :"]
		self.hudFr = ["Score : ","Temps : ", "Vies : "]
		self.hud = []
		self.verifier = False #Empeche le cursueur de commencer a Langage
		self.transition = False
		self.rgbNoir = (0,0,0)
		#self.rgbNoir = (255,255,255)
	def getHauteurEcran(self):
		return self.WINDOW_HEIGHT
	def getHUD(self, nb):
		return self.hud[nb]
	def setIntro(self,intro):
		self.intro = intro
	def setTransition(self,transition):
		self.transition = transition
	def transitionner(self):
		if self.transition:
			self.monde = Monde_2()
			self.mario.setY(self.monde.getSolAbsolu()-20)
		while self.transition:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
					self.transition = False

			self.gameFenetre.fill(self.rgbNoir)
			menuImg = pygame.image.load("Images/Mario/marioArretDroite.png")
			xSymbol = self.font3.render("X",True,(255,255,255))
			vie = self.mario.getVieDeMario()
			nbrVies = self.font3.render(str(vie),True,(255,255,255))
			self.gameFenetre.blit(menuImg,(250,140))
			self.gameFenetre.blit(xSymbol,(315,145))
			self.gameFenetre.blit(nbrVies,(370,145))
			pygame.display.update()
	def game_Intro(self):
		#Tableaux qui contiennent les différentes langues du menu Langage
		tablanguageFr = ["","Langages ", ". Francais",". Anglais"]
		tablanguageEn = ["","Languages ", ". French",". English"]
		tablanguage = []

		menuImg = pygame.image.load("Images/pause.png")

		#Tableau qui contiennent les différentes règles du menu Règles
		tabtextFr = ["Touches :", ". Fleche droite : avancer vers la droite", ". Fleche gauche : avancer vers la gauche", ". Fleche du haut : avancer vers le haut (menu uniquement)", ". Fleche du bas : avancer vers le bas (menu uniquement)", ". Espace : Sauter",". Entrer : tirer une boule de feu", ". P : affiche le menu"]
		tabtextEn = ["Keys :",". Right arrow : move right", ". Left Arrow : move left",". Up Arrow : move up (menu only)",". Down Arrow : move down (menu only)", ". Space : Jump", ". Enter : throw a fire ball", ". P : Display Menu" ]
		tabtext = []

		optionSelectionnee = 1
		langueSelectionnee = 2

		#Tableaux qui contiennent le différents menu du menu pricipal
		tabOptionsFr = ["","Jouer","Charger","Sauvegarder","Langages","Regles du jeu","Quitter"]
		tabOptionsEn = ["","Play","Load","Save","Languages","Rules","Quit"]
		tabOptions = []

		tabCordsEcran = [(290,180),(290,210),(290,240),(290,270),(290,300),(290,330)]
		tabOptAff = []
		tabLangAff = []

		menuImg = pygame.image.load("Images/Menu/menu.jpeg")
		optionImg = pygame.image.load("PythonSuperMario10_02_2019/Images/options.png")

		if self.langue=="En":
			tablanguage = tablanguageEn
			tabtext = tabtextEn
			tabOptions = tabOptionsEn
			self.hud = self.hudEn
		elif self.langue=="Fr":
			tablanguage = tablanguageFr
			tabtext = tabtextFr
			tabOptions = tabOptionsFr
			self.hud = self.hudFr

		while self.intro:
			#POUR LE MENU DES REGLES
			if self.regles and not self.languageMenu:
				#On prepare l'affichage du texte :
				self.gameFenetre.blit(optionImg,(0,-30))
				y=70
				for tab in tabtext:
					#Pour chaque string dans tabtext on va créer une texture et l'afficher
					font = self.font4.render(tab,True,(255,255,255))
					self.gameFenetre.blit(font,(50,y))
					y+=30
			#POUR LE MENU DES LANGUES
			else:
				if self.languageMenu and not self.regles:
					self.verifier = True
					tabLangAff.append (-1)
					self.gameFenetre.blit(menuImg,(0,-30))
					i = 0
					#Affichage des parametres lies à la langue
					for tab in tablanguage:
						if i > 0:
							tabLangAff.append (self.font3.render(tab,True,(255,255,255)))
							self.gameFenetre.blit(tabLangAff[i],tabCordsEcran[i-1])
						i +=1

				#POUR LE MENU DES PRINCIPAL :
				else:
					if not self.regles and not self.languageMenu:
						tabOptAff.append (-1)
						self.gameFenetre.blit(menuImg,(0,-30))
						i = 0
						#Affichage du menu
						for tab in tabOptions:
							if i > 0:
								#Met en rouge le 1er element selectionne
								if i == 1:
									tabOptAff.append (self.font2.render(tabOptions[1],True,(255,0,0)))
									self.gameFenetre.blit(tabOptAff[1],tabCordsEcran[0])
								else:
									tabOptAff.append (self.font3.render(tabOptions[i],True,(255,255,255)))
									self.gameFenetre.blit(tabOptAff[i],tabCordsEcran[i-1])
							i +=1

			#Gere les touches appuyees dans le menu
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_a or optionSelectionnee == 6 and event.key == pygame.K_RETURN:
						pygame.quit()
						quit()
					if event.key == pygame.K_r:
						self.intro = False
					if event.key == pygame.K_p:
						self.regles = False
						self.languageMenu = False
					if event.key == pygame.K_UP:
						if langueSelectionnee > 2 and self.languageMenu:
							langueSelectionnee = langueSelectionnee - 1
							tabLangAff[langueSelectionnee + 1] = self.font3.render(tablanguage[langueSelectionnee + 1],True,(255,255,255))
							tabLangAff[langueSelectionnee] = self.font2.render(tablanguage[langueSelectionnee],True,(255,0,0))


						elif optionSelectionnee > 1 and not self.languageMenu:
							optionSelectionnee = optionSelectionnee - 1
							tabOptAff[optionSelectionnee + 1] = self.font3.render(tabOptions[optionSelectionnee + 1],True,(255,255,255))
							tabOptAff[optionSelectionnee] = self.font2.render(tabOptions[optionSelectionnee],True,(255,0,0))

					if event.key == pygame.K_DOWN:
						if langueSelectionnee < 3 and self.languageMenu:
							langueSelectionnee = langueSelectionnee + 1
							tabLangAff[langueSelectionnee - 1] = self.font3.render(tablanguage[langueSelectionnee - 1],True,(255,255,255))
							tabLangAff[langueSelectionnee] = self.font2.render(tablanguage[langueSelectionnee],True,(255,0,0))


						elif optionSelectionnee < 6 and not self.languageMenu:
							optionSelectionnee = optionSelectionnee + 1
							tabOptAff[optionSelectionnee - 1] = self.font3.render(tabOptions[optionSelectionnee - 1],True,(255,255,255))
							tabOptAff[optionSelectionnee] = self.font2.render(tabOptions[optionSelectionnee],True,(255,0,0))


					if optionSelectionnee == 1 and event.key == pygame.K_RETURN:
						self.intro = False
					if optionSelectionnee == 2 and event.key == pygame.K_RETURN:
						self.monde,self.mario  = self.deserialiser()
						self.intro = False
					if optionSelectionnee == 3 and event.key == pygame.K_RETURN:
						self.serialiser(self.monde,self.mario)
						self.intro = False
					if event.key == pygame.K_h:
						self.transition = True
						self.transitionner()

					if optionSelectionnee == 5 and event.key == pygame.K_RETURN:
						self.regles = True
					if optionSelectionnee == 4 and event.key == pygame.K_RETURN:
						self.languageMenu = True
						self.langueSelectionnee = 2

					if langueSelectionnee == 2 and event.key == pygame.K_RETURN and self.verifier:
						self.langue = "Fr"
						tabLangAff[langueSelectionnee] = self.font3.render(tablanguage[langueSelectionnee ],True,(255,255,255))
						langueSelectionnee = 1
						tabOptAff = []
						optionSelectionnee = 1
						self.languageMenu = False
						self.verifier = False

					if langueSelectionnee == 3 and event.key == pygame.K_RETURN and self.verifier:
						self.langue = "En"
						tabLangAff[langueSelectionnee ] = self.font3.render(tablanguage[langueSelectionnee ],True,(255,255,255))
						langueSelectionnee = 1
						tabOptAff = []
						optionSelectionnee = 1
						self.languageMenu = False
						self.verifier = False

					if self.langue=="En":
						print("IN")
						tablanguage = tablanguageEn
						tabtext = tabtextEn
						tabOptions = tabOptionsEn
						self.hud = self.hudEn
					elif self.langue=="Fr":
						print("FR")
						tablanguage = tablanguageFr
						tabtext = tabtextFr
						tabOptions = tabOptionsFr
						self.hud = self.hudFr

			pygame.display.update()




	def afficher(self):
		#à déplacer dans le main
		score = self.font2.render(self.getHUD(0) + ""+ str(mario.getPieces()),True,(255,255,255))
		tps = self.font1.render(self.getHUD(1) + "" + str(self.monde.getTime()),True,(0,0,0))
		vies = self.font3.render(self.getHUD(2) + ""+ str(mario.getVieDeMario()),True,(0,55,55))
		self.gameFenetre.blit(score,(0,0))
		self.gameFenetre.blit(vies,(600,0))
		self.gameFenetre.blit(tps,(315,0))
	def integrer(self,monde,mario):
		self.monde = monde
		self.mario = mario

	def serialiser(self,obj1,obj2):
		if isinstance(obj1,Monde):
			pickle_out = open("Sauvegardes/objMonde.pickle","wb")
			pickle.dump(monde,pickle_out)
			pickle_out.close()
		if isinstance(obj2,Mario):
			pickle_out = open("Sauvegardes/objMario.pickle","wb")
			pickle.dump(mario,pickle_out)
			pickle_out.close()

	def deserialiser(self):
		try:
			pickle_in = open("Sauvegardes/objMario.pickle","rb")
			mario = pickle.load(pickle_in)
			pickle_in = open("Sauvegardes/objMonde.pickle","rb")
			monde = pickle.load(pickle_in)
			return monde,mario
		except Exception as err:
			return self.monde,self.mario

	def gererClavier(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					pygame.quit()
					quit()
				if event.key == pygame.K_p:
					self.intro = True
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					quit()
				if event.key == pygame.K_RETURN:
					#self.mario.setTirage(True)
					self.mario.setTirage(True)
					if mario.getIsVersDroite():
						self.mario.tabBoules.append(Boule(mario.getX() + 25, self.mario.getY()+6,self.mario.getIsVersDroite()))
					else:
						self.mario.tabBoules.append(Boule(mario.getX() - 10, self.mario.getY()+6,self.mario.getIsVersDroite()))
				if event.key == pygame.K_RIGHT:
					self.monde.setDx(10)
					self.mario.setMarche(True)
					self.mario.setIsVersDroite(True)
					#pour pouvoir rentrer dans la fonction deplacementfond pour déplacer les objets du fond
					if self.monde.getXPos() <= -1:
						self.monde.setXPos(0)
				if event.key == pygame.K_LEFT:
					self.monde.setDx(-10)
					self.mario.setMarche(True)
					self.mario.setIsVersDroite(False)
					if self.monde.getXPos() >= 4430:
						self.monde.setXPos(4430)
						self.monde.setXFond1(-50)
						self.monde.setXFond2(750)
				if event.key == pygame.K_SPACE:
					self.mario.setSaut(True)
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					self.monde.setDx(0)
					self.mario.setMarche(False)
				if event.key == pygame.K_LEFT:
					self.monde.setDx(0)
					self.mario.setMarche(False)
				if event.key == pygame.K_SPACE:
					self.monde.setDx(0)
					#à revoir
					self.mario.setMarche(False)

	def demarer(self):

		while(self.monde.getTime() != 0 and self.mario.getY() <=350):
			self.transitionner()
			self.game_Intro()
			if self.provisoire != int(pygame.time.get_ticks()/1000):
				self.provisoire = int(pygame.time.get_ticks()/1000)
				self.monde.setTime ( self.monde.getTime() - 1)

			#ddétéction de collision entre mario et des objets sur l'écran
			for objet in self.monde.getTabObjets():
				if isinstance(objet,Bloc) and not isinstance(objet,Bloc_Nazo) and objet.getCasse():
					self.monde.getTabObjets().remove(objet)
				if isinstance(objet,Bloc_Nazo) and objet.getVide():
					objet.changeImg()
				if self.mario.proche(objet):
					self.mario.contact(self.mario,objet,self.monde)
				for perso in self.monde.getTabPersonnages():
					if isinstance(perso,Champignon):
					#for champignon in tabChampignons:
						if perso.proche(objet):
							perso.contactChamp(objet,self.monde)
					#détéction de collision entre mario et les champignons
						if self.mario.proche(perso):
					 		self.mario.contactPersonnage(perso,self.monde)
					if isinstance(perso,Tortue):
					#for perso in tabPersonnages:
						if perso.proche(objet):
							perso.contactTortue(objet,self)
					#détéction de coollision entre mario et les tortues
						if self.mario.proche(perso):
							self.mario.contactPersonnage(perso,self.monde)
					if isinstance(perso,Plante):
						if self.mario.proche(perso):
							self.mario.contactPersonnage(perso,self)
					if isinstance(perso,Magic_Mushroom):
						if self.mario.contactAbsolu(self.mario,perso):
							self.monde.getTabPersonnages().remove(perso)
				if not isinstance(objet,Sol) and not isinstance(objet,Trou):
					for boule in self.mario.getTabBoules():
						if boule.contactBoule(objet):
							self.mario.getTabBoules().remove(boule)
				#?????
				if isinstance(objet,Sol):
					objet.deplacer(self.monde.getXPos(),self.monde.getDx())

			#déplacement des images du fond pendant le déplacement de mario
			self.monde.deplacementFond()

			self.gameFenetre.blit(pygame.image.load(self.monde.getStrImgFond()),(self.monde.getxFond1(),0))
			self.gameFenetre.blit(pygame.image.load(self.monde.getStrImgFond()),(self.monde.getxFond2(),0))
			self.gameFenetre.blit(pygame.image.load(self.monde.getImgChateau()),(10-self.monde.getXPos(),95))
			self.gameFenetre.blit(pygame.image.load(self.monde.getImgDepart()),(220-self.monde.getXPos(),233))
			self.gameFenetre.blit(pygame.image.load(self.monde.getimgChateauFin()),(4650-self.monde.getXPos(),145))
			self.gameFenetre.blit(pygame.image.load(self.monde.getimgDrapeau()),(5000-self.monde.getXPos(),113))

			for perso in self.monde.getTabPersonnages():
				perso.deplacer(self.monde.getXPos(),self.monde.getDx())
				for boule in self.mario.getTabBoules():
					if not isinstance(perso,Mario):
						if(boule.contactBoule(perso)):
							perso.setVivant(False)
							if not self.mario.getTabBoules() == []:
								self.mario.getTabBoules().remove(boule)
				if isinstance(perso,Plante):
					self.gameFenetre.blit(pygame.image.load(perso.getImgObjet()),(perso.getX(),perso.getY()))
					perso.bouger()
					if not perso.getVivant():
						self.monde.getTabPersonnages().remove(perso)

			for boule in self.mario.getTabBoules():
				boule.deplacer(self.monde.getXPos(),self.monde.getDx())

				#on dessine des objets sur l'écran et affichage du château et du drapeau à la fin


			#détection de collision entre mario et des pièces d'or
			for piece in self.monde.getTabPieces():
				if self.mario.proche(piece):
					if (self.mario.contactAbsolu(self.mario,piece)):
						self.monde.getTabPieces().remove(piece)
						self.mario.setPieces(self.mario.getPieces() + 10)
				piece.deplacer(self.monde.getXPos(),self.monde.getDx())
				self.gameFenetre.blit(pygame.image.load(piece.alternanceImg()),(piece.getX(),piece.getY()))


			#on déssine les objets sur l'écran
			for objet in self.monde.getTabObjets():
				objet.deplacer(self.monde.getXPos(),self.monde.getDx())
				if not isinstance(objet, Sol):
					self.gameFenetre.blit(pygame.image.load(objet.getImgObjet()),(objet.getX(),objet.getY()))

			for perso in self.monde.getTabPersonnages():
				if isinstance(perso,Champignon):
					if perso.getVivant():
						perso.bouger()
						self.gameFenetre.blit(pygame.image.load(perso.marcher("champ",10)),(perso.getX(),perso.getY()))
					else:
						self.gameFenetre.blit(pygame.image.load(perso.mourir()),(perso.getX(),perso.getY()+20))
						self.monde.tabPersonnages.remove(perso)
			#affichage des tortues sur l'écran
				if isinstance(perso,Tortue):
					if not perso.getCachee() and perso.getVivant():
						perso.bouger(2)
						self.gameFenetre.blit(pygame.image.load(perso.marcher("tortue",10)),(perso.getX(),perso.getY()))
					else:
						#if(perso.getPresqueMorte() ): elle ne bouge pas
						if perso.getCachee() and not perso.getWalkingDead():
							self.gameFenetre.blit(pygame.image.load(perso.mourir()),(perso.getX(),perso.getY()+22))
						elif perso.getCachee() and  perso.getWalkingDead():
							perso.bouger(6)
							self.gameFenetre.blit(pygame.image.load(perso.mourir()),(perso.getX(),perso.getY()+22))
					if not perso.getVivant(): #envlène les torutes mortes dans la liste des personnages
						self.monde.tabPersonnages.remove(perso)
				if isinstance(perso,Magic_Mushroom):
					self.gameFenetre.blit(pygame.image.load(perso.getImgMagicMushroom()),(perso.getX(),perso.getY() ))
					perso.bouger(self.monde,self)

			#affichage du text sur l'écran
			if self.mario.getSaut():
				if not self.mario.getMorteFatale():
					self.gameFenetre.blit(pygame.image.load(self.mario.sauter(self.monde.getHauteurPlafond(),self.monde.getYSol())),(self.mario.getX(),self.mario.getY()) )
				else:
					self.gameFenetre.blit(pygame.image.load(self.mario.perdreVie(monde.getSolAbsolu(),self)),(self.mario.getX(),self.mario.getY()) )
			elif mario.getTombe():
				self.gameFenetre.blit(pygame.image.load(self.mario.tomber(self.monde.getHauteurPlafond(),self.monde.getYSol())),(self.mario.getX(),self.mario.getY()))
			else:
				self.gameFenetre.blit(pygame.image.load(self.mario.marcher("mario",2)),(self.mario.getX(),self.mario.getY()))

			if self.mario.getTirage() :
				for boule in self.mario.getTabBoules():
					self.gameFenetre.blit(pygame.image.load(self.mario.tirer(self.monde.getSolAbsolu(),5)),(boule.getX(),boule.getY()))
			'''
			for personnage in self.monde.getTabPersonnages():
				if isinstance(personnage,Personnage):
					pygame.draw.rect(self.gameFenetre,(3,3,4),(personnage.getX(),personnage.getY(),personnage.getLargeur(),personnage.getHauteur()))
			pygame.draw.rect(self.gameFenetre,(3,3,4),(self.mario.getX(),self.mario.getY(),self.mario.getLargeur(),self.mario.getHauteur()))
			'''
			#gère les événements du clavier
			self.gererClavier()
			#met à jour l'écran
			self.clock.tick(self.FPS)
			#dessine des objets sur l'écran et gère le nombre de frames par second
			self.afficher()
			pygame.display.update()

main = Main("Super Mario in Python",700,350)
monde = Monde_1()
#mario = Mario(300,monde.getSolAbsolu()-20)
#mario = SuperMario(300,monde.getSolAbsolu()-20)
mario = BigMario(300,monde.getSolAbsolu()-22)

main.integrer(monde,mario)
main.demarer()


pygame.quit()
