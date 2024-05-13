import pygame

class PhisicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]

    def update(self, mvmnt=(0, 0)):
        frame_mvmnt = (mvmnt[0] + self.velocity[0] + mvmnt[1] + self.velocity[1]) 

        self.pos[0] += frame_mvmnt[0] 
        self.pos[1] += frame_mvmnt[1]

    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)
