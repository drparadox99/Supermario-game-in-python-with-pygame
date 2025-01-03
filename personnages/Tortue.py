from  personnages.Personnage import Personnage
from objets.Trou import Trou

class Tortue(Personnage):

    def __init__(self,x,y):
        super().__init__(x,y,21,32)
        super().setMarche(True)
        super().setIsVersDroite(True)
        self.PAUSE = 15  #A quoi sert cet attribut ?
        self.dxTortue = 2
        self.walkingDead = False   #La tortue se cache sous sa carcasse
        self.tombe = False
        self.cachee = False
        self.tabImgs = ["Images/Monde_1/tortueArretGauche.png","Images/Monde_1/tortueArretDroite.png","Images/Monde_1/tortueMarcheGauche.png","Images/Monde_1/tortueMarcheDroite.png","Images/Monde_1/tortueFermee.png"]
        self.imgTortue = self.tabImgs[3]

    #retourne l'image du Tortue
    def getImgTortue(self):
        return self.imgTortue

    def setWalkingDead(self,etat):
        self.walkingDead = etat
    def setDxTortue(self,dx):
        self.dxTortue = dx


    def getDxTortue(self):
        return self.dxTortue
    def getWalkingDead(self):
        return self.walkingDead
    def getCachee(self):
        return self.cachee
    def setCachee(self, cachee):
    	self.cachee = cachee
    def getTombe(self):
    	return self.tombe

    #déplace le Tortue sur le terrain
    def bouger(self,dx):
        if self.getIsVersDroite():
            self.dxTortue = dx * 1
        else:
            self.dxTortue = dx * -1
        self.setX(self.getX()+self.dxTortue)

    def tomber(self, ySol):
        strImg = " "
        #tortue descend doucement vers le bas
        self.y = self.y + 15

    #gère les contacts entre la torue et les objets sur l'écran
    def contactTortue(self,objet, game):
        if self.collisionDroite(self,objet) and self.getIsVersDroite():
            self.setIsVersDroite(False)
            self.dxTortue = -2
        else:
            if self.collisionGauche(self,objet) and not  self.getIsVersDroite():
                self.setIsVersDroite(True)
                self.dxTortue = 2
            elif self.y+self.hauteur>= objet.getY() and self.x>objet.getX() and self.x+self.largeur < objet.getX()+objet.getHauteur() and isinstance(objet, Trou) and self.chute(self,objet):
                self.tombe = True
                self.tomber( objet.getY()+objet.getHauteur())
                #self.vivant = True
                if self.y > game.getHauteurEcran() +10:
                    pass
                    self.vivant = False


    #détéction de la mort de la tortute en envoyant l'iamge appopriée
    def mourir(self):
        img = ""
        img = self.tabImgs[4]
        return img
