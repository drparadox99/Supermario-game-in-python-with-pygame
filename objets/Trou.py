from  objets.Objet import Objet

class Trou(Objet):

	def __init__(self,x,y,monde):
		if monde == "Monde_1":
			super().__init__(x,y,60,57,"Images/Divers/Trou_bleue.png")
		else:
			super().__init__(x,y,60,57,"Images/Divers/Trou_noir.png")
