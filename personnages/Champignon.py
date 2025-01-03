from  personnages.Personnage import Personnage
from objets.Trou import Trou


class Champignon(Personnage):

    def __init__(self,x,y):
        super().__init__(x,y,24,24)
		#super().__init__(x,y,28,50) #calling the superclass,parent's class constructor to deal with the three parameeters instead refining them in the child class's constructor
        super().setMarche(True)
        super().setIsVersDroite(True)
        self.imgChampignon = 'Images/piece1.png'
        self.dxChampignon = 2
        self.tabImgs = ["Images/Monde_1/champArretGauche.png","Images/Monde_1/champArretDroite.png","Images/Monde_1/champMarcheGauche.png","Images/Monde_1/champMarcheDroite.png","Images/Monde_1/champEcraseGauche.png","Images/Monde_1/champEcraseDroite.png"]

    #return l'image du champignon
    def getImgChampignon(self):
        return self.imgChampignon

    #déplace le champignon sur le terrain
    def bouger(self):
        if self.getIsVersDroite():
            self.dxChampignon = 2
        else:
            self.dxChampignon = -2
        self.setX(self.getX()+self.dxChampignon)

    def tomber(self, hauteurPlafond, ySol):
        #mario descend doucement vers le bas
        self.y = self.y + 15


    #gère les contacts entre le champignon et des objets sur l'écran
    def contactChamp(self,objet, game):
        if self.collisionDroite(self,objet) and self.getIsVersDroite():
            self.setIsVersDroite(False)
            self.dxChampignon = -2
            if isinstance(objet, Trou):
                if self.x >= objet.getX()+(objet.getLargeur()/2):
                    self.dxChampignon=0
        else:
            if self.collisionGauche(self,objet) and not  self.getIsVersDroite():
                self.setIsVersDroite(True)
                self.dxChampignon = 2
                if isinstance(objet, Trou):
                    if self.x <= objet.getX()+(objet.getLargeur()/2):
                        self.dxChampignon=0
        if self.y+self.hauteur >= objet.getY() and self.x>=objet.getX() and self.x+self.largeur <= objet.getX()+objet.getLargeur() and isinstance(objet, Trou) and self.chute(self,objet):
            self.tombe = True
            self.tomber(game.getHauteurPlafond(), objet.getY()+objet.getHauteur())

    #détéction de mort du champignon, en envoyant l'image appopriée
    def mourir(self,):
        img = ""
        #self.setY(self.getY()+20)
        self.largeur = 24
        self.hauteur = 16
        self.dxChampignon = 0
        if self.getIsVersDroite():
            #img = './Images/champEcraseDroite.png'
            img = self.tabImgs[5]
        else:
            #img = './Images/champEcraseGauche.png'
            img = self.tabImgs[4]
        self.y = 260
        self.vivant = False
        return img
