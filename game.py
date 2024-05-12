import pygame, sys


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Mi primer Juego :D')

        self.screen = pygame.display.set_mode((640,480)) # creamos la variable que contiene la ventana donde existirá el juego

        self.clock = pygame.time.Clock() #clock es para limitar el ratio de fps

        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0, 0, 0)) #Elimina los sobrantes del png

        self.img_pos = [160,260]
        self.mvmnt = [False, False] #Variable de movimiento
    def run(self):
        while True:
            self.screen.fill((14, 219, 248)) #fill() nos pinta la pantalla con un color (RGB), tambien evita las nubes repetidas
            self.img_pos[1] += (self.mvmnt[1] - self.mvmnt[0])*5
            self.screen.blit(self.img, self.img_pos)

            for event in pygame.event.get(): #Capturamos el input de la Ventana de lo contrario el SO pensará que la ventana no responde
                if event.type == pygame.QUIT: #Para cerrar la ventana... literalmente la "X" de la parte superior derecha 
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: # Aqui le Decimos si detecta que se pulse una tecla hacia abajo
                    if event.type == pygame.K_UP:
                        self.mvmnt[0] = True
                    if event.type == pygame.K_DOWN:
                        self.mvmnt[1] = True
                if event.type == pygame.KEYUP: # Aqui le Decimos si detecta que se pulse una tecla arriba
                    if event.type == pygame.K_UP:
                        self.mvmnt[0] = False
                    if event.type == pygame.K_DOWN:
                        self.mvmnt[1] = False

            pygame.display.update()
            self.clock.tick(60)  #Limitamos los fps a 60 con tick

Game().run()