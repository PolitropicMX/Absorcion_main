#ok banda hoy hare un vaso, un recipiente en python
import pygame, sys
import numpy as np
import math
from class_projection import Draw3d 
# Initialize the pygame
pygame.init()

#Create the screen
HEIGHT, WIDTH = 600,600
screen = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("Pygame project")
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

#Create the clock
clock = pygame.time.Clock()

#Codeline for the image background
#background = pygame.image.load('')

font = pygame.font.Font('freesansbold.ttf',32)


 # variables
segundero = 0
 # [X, Y]
cur_vel = [0, 0]
cur = [100,100]
# programare visualmente el diagrama de

# instanciamos un objeto de la clase Draw3d
Lapiz = Draw3d(screen,20,(WIDTH/2,HEIGHT/2))

class Corriente:
    # CREAMOS EL CONSTRUCCTOR Y LE PASAMOS 2 COORDENADAS
    # PUEDE SER UN PUNTO 2D O 3D, PRIMERO EMPEZAREMOS CON 2D
    def __init__(self,A,B,propiedad):
        self.desde = A
        self.hasta = B
        self.color = propiedad

        
        

    





# Funciones de dibujo
##def dot(xi,yi,r):
##    pygame.draw.circle(screen,(255,255,0),(xi,yi),r)
##def line(xi,yi,xf,yf):
##    pygame.draw.line(screen,(255,255,255),(xi,yi),(xf,yf),1)
##def rect(xi,yi,w,h):
##    pygame.draw.rect(screen,(255,255,255),(xi,yi,w,h))
##def text(string,xi,yi):
##    textsurface = font.render(string,False,(10,100,100))
##    screen.blit(textsurface,(xi,yi))
##def panel(xi,yi,string):
##    w,h = 250,40
##    pygame.draw.rect(screen,(25,25,255),(xi,yi,w,h))
##    textsurface = font.render(string,False,(255,255,255))
##    screen.blit(textsurface,(xi,yi))
##def cursor(xi,yi):
##    ri,re = 10,12
##    pygame.draw.circle(screen,(0,0,0),(xi,yi),re)
##    pygame.draw.circle(screen,(255,255,255),(xi,yi),ri)
##def vaso(xi,yi,w,h,e):
##    pygame.draw.rect(screen,(255,255,255),(xi,yi,w,h))
##    pygame.draw.rect(screen,(0,0,0),(xi+e,yi,w-2*e,h-e))
    
aux = 1
#### INICIALIZADORES ####
X,Y,H,W = 100,100,500,300
while True:
    tiempo = pygame.time.get_ticks()
    # LOS CONTROLES
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # EL ORDEN DE ESTOS DOW SI IMPORTA
            pygame.quit()
            sys.exit()
            
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_q:
                pass
            if event.key == pygame.K_w:
                cur_vel[1] = -10
            if event.key == pygame.K_a:
                cur_vel[0] = -10
            if event.key == pygame.K_x:
                pass
            if event.key == pygame.K_d:
                cur_vel[0] = 10
            if event.key == pygame.K_s:
                cur_vel[1] = 10
            if event.key == pygame.K_n:
                pass
            if event.key == pygame.K_f:
                pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_q:
                pass
            if event.key == pygame.K_w:
                cur_vel[1] = 0
            if event.key == pygame.K_e:
                pass
            if event.key == pygame.K_r:
                pass
            if event.key == pygame.K_a:
                cur_vel[0] = 0
            if event.key == pygame.K_s:
                cur_vel[1] = 0
            if event.key == pygame.K_d:
                cur_vel[0] = 0
            if event.key == pygame.K_f:
                pass




    screen.fill((0,0,0))
    # A partir de aqui dibujas
    #print(segundero)

    # Columna
    anccol = 100
    larcol = 200
    cx,cy = (WIDTH-anccol)/2,200
    Lapiz.rect(cx,cy,anccol,larcol)
    # corrientes
    # L2
    l210 = Lapiz.line(cx+anccol*3/4,cy,cx+anccol*3/4,cy-50)
    l211 = Lapiz.line(cx+anccol*3/4,cy-50,cx+anccol*3/4+100,cy-50)
    # L1
    l110 = Lapiz.line(cx+anccol*3/4,cy+larcol,cx+anccol*3/4,cy+larcol+50)
    l111 = Lapiz.line(cx+anccol*3/4,cy+larcol+50,cx+anccol*3/4+100,cy+larcol+50)
    # G2
    l210 = Lapiz.line(cx+anccol/4,cy,cx+anccol/4,cy-50)
    l211 = Lapiz.line(cx+anccol/4,cy-50,cx+anccol/4-100,cy-50)
    # L1
    l110 = Lapiz.line(cx+anccol/4,cy+larcol,cx+anccol/4,cy+larcol+50)
    l111 = Lapiz.line(cx+anccol/4,cy+larcol+50,cx+anccol/4-100,cy+larcol+50)
    # L
    l = Lapiz.flujo([cx+anccol*3/4,cy],[cx+anccol*3/4,cy+larcol],(anccol/2),segundero,'liq')
    # G
    g = Lapiz.flujo([cx+anccol/4,cy+larcol],[cx+anccol/4,cy],(anccol/2),segundero,'vap')
    
    
    
    
    #cursor
    cur[0] += cur_vel[0]
    cur[1] += cur_vel[1]
    #Aqui termina el loop
    segundero = segundero + 1
    pygame.display.update()
    clock.tick(30)
