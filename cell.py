from params import *
import pygame
pygame.init()

class Cell(object):
    def __init__(self, i, j, w, state):
        self.i = i
        self.j = j
        self.w = w
        self.state = state

    def show(self, screen):
        if self.state == 1:
            pygame.draw.rect(screen, yellow, (self.i*w, self.j*w, self.w, self.w))
        else:
            pygame.draw.rect(screen, grey, (self.i*w, self.j*w, self.w, self.w))
        pygame.draw.rect(screen, (150, 150, 150), (self.i*w, self.j*w, self.w, self.w), 1)

    def countAlive(self, mesh):
        total = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                nxt_i = (self.i + i) % cols
                nxt_j = (self.j + j) % rows
                total += mesh[nxt_i][nxt_j].state

        total -= self.state
        return total