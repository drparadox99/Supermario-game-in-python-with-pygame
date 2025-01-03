from  objets.Objet import Objet

class Feu(Objet):
	def __init__(self,x,y,direction, img):
		super().__init__(x,y,24,8,img)
		self.directionDroite = direction

	def getDirectionDroite(self):
		return self.directionDroite
	def setDirectionDroite(self, direction):
		self.directionDroite = direction

	def contactFeu(self,obj):
		#il y a pas de contact avec les pièces et supermario
		rect1 = self.retourneRectangle(obj.getX(),obj.getY(),obj.getLargeur(),obj.getHauteur())
		rect2 = self.retourneRectangle(self.x,self.y,self.largeur,self.hauteur)
		#pygame.draw.rect(game.gameFenetre,(3,3,4),(obj1.getX(),obj1.getY(),28,58))
		#pygame.draw.rect(game.gameFenetre,(3,3,4),(obj1.getX(),obj1.getY(),25,30))
		if(rect1.colliderect(rect2)):
			return True
		else:
			return False