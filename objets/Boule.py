from  objets.Objet import Objet

class Boule(Objet):
	def __init__(self,x,y,direction):
		super().__init__(x,y,8,8,'Images/Mario/Boules/boule0.png')
		self.ascendance = False
		self.rebondissement = 5
		self.directionDroite = direction

	def getAscendance(self):
		return self.ascendance
	def setAscendance(self,ascendance):
		self.ascendance = ascendance
	def getRebondissement(self):
		return self.rebondissement
	def setRebondissement(self,rebondissement):
		self.rebondissement = rebondissement
	def getHauteurBoule(self):
		return self.hauteurBoule
	def sethauteurBoule(self,hauteurBoule):
		self.hauteurBoule = hauteurBoule
	def getDirectionDroite(self):
		return self.directionDroite
	def setDirectionDroite(self,directionDroite):
		self.directionDroite = directionDroite

	def contactBoule(self,obj):
		#il y a pas de contact avec les pièces et supermario
		rect1 = self.retourneRectangle(obj.getX(),obj.getY(),obj.getLargeur(),obj.getHauteur())
		rect2 = self.retourneRectangle(self.x,self.y,self.largeur,self.hauteur)
		#pygame.draw.rect(game.gameFenetre,(3,3,4),(obj1.getX(),obj1.getY(),28,58))
		#pygame.draw.rect(game.gameFenetre,(3,3,4),(obj1.getX(),obj1.getY(),25,30))
		if(rect1.colliderect(rect2)):
			return True
		else:
			return False
