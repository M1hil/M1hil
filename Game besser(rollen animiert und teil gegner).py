
from os import X_OK
import pygame
import sys
from pygame.constants import BLEND_PREMULTIPLIED

pygame.init()
hintergrund = pygame.image.load("Documents/PyxelEdit/Game/Grafiken/hintergrund/400x400gruen.png")
screen = pygame.display.set_mode([400,400])
clock = pygame.time.Clock()
pygame.display.set_caption("Game")

linksRollen = [pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenL_1.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenL_2.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenL_3.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenL_4.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenL_5.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenL_6.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenL_7.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenL_8.png")]
rechtsRollen = [pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenR_1.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenR_2.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenR_3.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenR_4.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenR_5.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenR_6.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenR_7.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenR_8.png")]
untenRollen = [pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenU_1.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenU_2.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenU_3.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenU_4.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenU_5.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenU_6.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenU_7.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenU_8.png")]
obenRollen = [pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenU_1.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenU_8.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenU_7.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenU_6.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenU_5.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenU_4.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenU_3.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slspieler/slimepinkRollenU_2.png")]
linksListe = [pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenL_1.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenL_2.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenL_3.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenL_4.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenL_5.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenL_6.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenL_7.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenL_8.png")]
rechtsListe = [pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenR_1.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenR_2.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenR_3.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenR_4.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenR_5.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenR_6.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenR_7.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenR_8.png")]
untenListe = [pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenU_1.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenU_2.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenU_3.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenU_4.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenU_5.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenU_6.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenU_7.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenU_8.png")]
obenListe = [pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenU_1.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenU_8.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenU_7.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenU_6.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenU_5.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenU_4.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenU_3.png"), pygame.image.load("Documents/PyxelEdit/Game/Grafiken/slgegner/slimegruenRollenU_2.png")]
       
class spieler:
    def __init__(self,x,y,geschw,breite,hoehe,richtg,schritteRechts,schritteLinks,schritteUnten,schritteOben):
        self.x = x
        self.y = y
        self.geschw = geschw
        self.breite = breite
        self.hoehe = hoehe
        self.richtg = richtg
        self.schritteRechts = schritteRechts
        self.schritteLinks = schritteLinks
        self.schritteUnten = schritteUnten
        self.schritteOben = schritteOben
        self.last = [0,0,1,0]
        self.ok = True

    def laufen(self,liste):
        if liste[0]:
            self.x -= self.geschw
            self.richtg = [1,0,0,0,0]
            self.schritteLinks += 1
        if liste[1]:
            self.x += self.geschw
            self.richtg = [0,1,0,0,0]
            self.schritteRechts += 1
        if liste[2]:
            self.y += self.geschw
            self.richtg = [0,0,1,0,0]
            self.schritteUnten += 1
        if liste[3]:
            self.y -= self.geschw
            self.richtg = [0,0,0,1,0]
            self.schritteOben += 1

    def resetSchritte(self):
        self.schritteLinks = 0
        self.schritteRechts = 0
        self.schritteUnten = 0
        self.schritteOben = 0
    def stehen(self):
        self.richtg = [0,0,0,0,1]
        self.resetSchritte()

    def spZeichnen(self):
        if self.schritteLinks == 47:
            self.schritteLinks = 0
        if self.schritteRechts == 47:
            self.schritteRechts = 0
        if self.schritteUnten == 47:
            self.schritteUnten = 0
        if self.schritteOben == 47:
            self.schritteOben = 0
        
        if self.richtg[0]:
            screen.blit(linksRollen[self.schritteLinks//6], (self.x,self.y))
            self.last = [1,0,0,0]

        if self.richtg[1]:
            screen.blit(rechtsRollen[self.schritteRechts//6], (self.x,self.y))
            self.last = [0,1,0,0]

        if self.richtg[2]:
            screen.blit(untenRollen[self.schritteUnten//6], (self.x,self.y))
            self.last = [0,0,1,0]

        if self.richtg[3]:
            screen.blit(obenRollen[self.schritteOben//6], (self.x,self.y))
            self.last = [0,0,0,1]

        if self.richtg[4]:
            if self.last[0]:
                screen.blit(linksRollen[0], (self.x,self.y))
            elif self.last[1]:
                screen.blit(rechtsRollen[0], (self.x,self.y))
            elif self.last[2]:
                screen.blit(untenRollen[0], (self.x,self.y))
            elif self.last[3]:
                screen.blit(obenRollen[0], (self.x,self.y))
                
class gegner:
    def __init__(self,x,y,geschwx,geschwy,breite,hoehe,richtg,xMin,xMax,yMin,yMax):
        self.x = x
        self.y = y
        self.geschwx = geschwx
        self.geschwy = geschwy
        self.breite = breite 
        self.hoehe = hoehe
        self.richtg = richtg
        self.ListeRechts = 0
        self.ListeLinks = 0
        self.ListeUnten = 0
        self.ListeOben = 0
        self.xMin = xMin
        self.xMax = xMax 
        self.yMin = yMin
        self.yMax = yMax
        self.leben = 6
        self.linksListe = linksListe
        self.rechtsListe = rechtsListe
        self.untenListe = untenListe
        self.obenListe = obenListe

        #self.ganz = pygame.image.load("Desktop/Python/Pygame1YT/Grafiken/voll.png")
        #self.halb = pygame.image.load("Desktop/Python/Pygame1YT/Grafiken/halb.png")
        #self.leer = pygame.image.load("Desktop/Python/Pygame1YT/Grafiken/leer.png")
    #def herzen(self):
    #    if self.leben >= 2:
    #        screen.blit(self.ganz, (507,15))
    #    if self.leben >= 4:
    #        screen.blit(self.ganz, (569,15))
    #    if self.leben == 6:
    #        screen.blit(self.ganz, (631,15))

    #    if self.leben == 1:
    #        screen.blit(self.halb, (507,15))
    #    elif self.leben == 3:
    #        screen.blit(self.halb, (569,15))
    #    elif self.leben == 5:
    #        screen.blit(self.halb, (631,15))

    #    if self.leben <= 0:
    #        screen.blit(self.leer, (507,15))
    #    if self.leben <= 2:
    #        screen.blit(self.leer, (569,15))
    #    if self.leben <= 4:
    #        screen.blit(self.leer, (631,15))

    def slgrZeichnen(self):
        if self.ListeLinks == 47:
            self.ListeLinks = 0
        if self.ListeRechts == 47:
            self.ListeRechts = 0
        if self.ListeUnten == 47:
            self.ListeUnten = 0
        if self.ListeOben == 47:
            self.ListeOben = 0

        if self.richtg[0]:
            screen.blit(linksListe[self.ListeLinks//6], (self.x,self.y))
            #self.last = [1,0,0,0]

        if self.richtg[1]:
            screen.blit(rechtsListe[self.ListeRechts//6], (self.x,self.y))
            #self.last = [0,1,0,0]

        if self.richtg[2]:
            screen.blit(untenListe[self.ListeUnten//6], (self.x,self.y))
            #self.last = [0,0,1,0]

        if self.richtg[3]:
            screen.blit(obenListe[self.ListeOben//6], (self.x,self.y))
            #self.last = [0,0,0,1]

        #if self.richtg[4]:
        #    if self.last[0]:
        #        screen.blit(linksStehen, (self.x,self.y))
        #    elif self.last[1]:
        #        screen.blit(rechtsStehen, (self.x,self.y))
        #    elif self.last[2]:
        #        screen.blit(untenStehen, (self.x,self.y))
        #    elif self.last[3]:
        #        screen.blit(obenStehen, (self.x,self.y))

    def Laufen(self):
        self.x += self.geschwx
        self.y += self.geschwy
        if self.geschwx < 0:
            self.richtg = [1,0,0,0,0]
            self.ListeLinks += 1
        if self.geschwx > 0:
            self.richtg = [0,1,0,0,0]
            self.ListeRechts += 1
        if self.geschwy < 0:
            self.richtg = [0,0,1,0,0]
            self.ListeUnten += 1
        if self.geschwy > 0:
            self.richtg = [0,0,0,1,0]
            self.ListeOben += 1

    def hinHer(self):
        if self.x < self.xMin:
            self.geschwx *= -1
        if self.y < self.yMax:
            self.geschwy *= -1
        if self.x > self.xMax:
            self.geschwx *= -1
        if self.y > self.yMin:
            self.geschwy *= -1
        self.Laufen() 

def zeichnen():
    screen.blit(hintergrund, (0,0))
    spieler1.spZeichnen()
    slimegr.slgrZeichnen()
    #slimegr.herzen()
    #if gewonnen:
    #    screen.blit(siegBild,(0,0))
    #elif verloren:
    #    screen.blit(verlorenBild,(0,0))
    pygame.display.update() 

def Kollision():
    global kugeln, verloren, gewonnen, go
    gegnerRechteck = pygame.Rect(slimegr.x,slimegr.y,slimegr.breite,slimegr.hoehe)
    spielerRechteck = pygame.Rect(spieler1.x,spieler1.y,spieler1.breite,spieler1.hoehe)
    
    if gegnerRechteck.colliderect(spielerRechteck):
        verloren = True
        gewonnen = False
        go = False

#x,y,geschw,breite,hoehe,sprungarray,[Richtungsarray],xMin,xMax
spieler1 = spieler(100,200,2,16,16,[0,0,0,0,1],0,0,0,0)
slimegr = gegner(300,200,2,2,16,16,[0,0,0,0],20,380,20,38)
verloren = False
gewonnen = False

go = True
richtg = [0,0,0,0,0]
schritteRechts = 0
schritteLinks = 0
schritteUnten = 0
schritteOben = 0
while go:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    spielerRechteck = pygame.Rect(spieler1.x,spieler1.y,16,16)
    gedrueckt = pygame.key.get_pressed()
    if gedrueckt[pygame.K_a]:
        spieler1.laufen([1,0,0,0])   
    if gedrueckt[pygame.K_d]:
        spieler1.laufen([0,1,0,0])  
    if gedrueckt[pygame.K_s]:
        spieler1.laufen([0,0,1,0])      
    if gedrueckt[pygame.K_w]:
        spieler1.laufen([0,0,0,1])      
    else:
        spieler1.stehen() 
    
    zeichnen()
    slimegr.hinHer()
    Kollision()
    clock.tick(60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    zeichnen()
