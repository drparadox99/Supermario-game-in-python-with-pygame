from  objets.Objet import Objet

class Piece(Objet):

	def __init__(self,x,y):
		super().__init__(x,y,30,50,'Images/Monde_1/piece1.png') #calling the superclass,parent's class constructor to deal with the three parameeters instead refining them in the child class's constructor
		self.compteur = 0
		self.PAUSE = 15


	#alternance entre les Images des pièces d'or
	def alternanceImg(self):
		strImg = ""
		self.compteur = self.compteur +  1
		if int(self.compteur)  < 5:
			strImg = 'Images/Monde_1/piece1.png'
		else:
			if int(self.compteur)  >= 5 and int(self.compteur) < 10:
				strImg = 'Images/Monde_1/piece2.png'
			else:
				if int(self.compteur)  >= 10 and int(self.compteur) < 15:
					strImg = 'Images/Monde_1/piece3.png'
				else:
					if int(self.compteur)  >= 15 and int(self.compteur) < 20:
						strImg = 'Images/Monde_1/piece4.png'
					else:
						self.compteur = 0
						strImg = 'Images/Monde_1/piece1.png'
		return strImg

	#A quoi ça sert???
	def ajouterImg(self):
		if(self.largeur != 0 and self.hauteur != 0):
			self.largeur -= 1
			self.hauteur -= 1
			return False
		else:
			return True
