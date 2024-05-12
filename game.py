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

        self.clsn_area = pygame.Rect(50, 50, 300, 50)


    def run(self):
        while True:
            self.screen.fill((14, 219, 248)) #fill() nos pinta la pantalla con un color (RGB), tambien evita las nubes repetidas
            self.img_pos[1] += (self.mvmnt[1] - self.mvmnt[0])*5
            self.screen.blit(self.img, self.img_pos)

            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            # if img_r.colliderect(self.clsn_area):
            #     pygame.draw.rect(self.screen, (0, 100, 255), self.clsn_area)
            # else:
            #     pygame.draw.rect(self.screen, (0, 50, 155), self.clsn_area)

            for event in pygame.event.get(): #Capturamos el input de la Ventana de lo contrario el SO pensará que la ventana no responde
                if event.type == pygame.QUIT: #Para cerrar la ventana... literalmente la "X" de la parte superior derecha 
                    pygame.quit()
                    sys.exit()

                # Moviemiento (eje y)
                if event.type == pygame.KEYDOWN: # Aqui le Decimos si detecta que se pulse una tecla hacia abajo
                    if event.key == pygame.K_UP:
                        self.mvmnt[0] = True
                    if event.key == pygame.K_DOWN:
                        self.mvmnt[1] = True
                if event.type == pygame.KEYUP: # Aqui le Decimos si detecta que se pulse una tecla arriba
                    if event.key == pygame.K_UP:
                        self.mvmnt[0] = False
                    if event.key == pygame.K_DOWN:
                        self.mvmnt[1] = False

                # Movimiento (eje x)
                # if event.type == pygame.KEY:
                #     if event.key == pygame.K_LEFT:
                #         self
            pygame.display.update()
            self.clock.tick(60)  #Limitamos los fps a 60 con tick

Game().run()