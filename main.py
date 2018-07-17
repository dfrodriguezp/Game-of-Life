from params import *
from cell import *
import sys
import numpy
import pygame
pygame.init()
pygame.font.init()

# Setup
canvas = pygame.display.set_mode(size)
pygame.display.set_caption("Conway's Game of Life")

cells = [[None for j in range(rows)] for i in range(cols)]

for i in range(cols):
    for j in range(rows):
        if numpy.random.uniform() < 0.3:
            cells[i][j] = Cell(i, j, w, 1)
        else:
            cells[i][j] = Cell(i, j, w, 0)
text = pygame.font.SysFont("Arial", 15)
text.set_bold(True)

# Draw
generation = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    canvas.fill(grey)
    alive = 0
    for i in range(cols):
        for j in range(rows):
            cells[i][j].show(canvas)
            alive += cells[i][j].state

    generation += 1
    aliveText = text.render("Alive cells: {}".format(alive), True, white)
    genText = text.render("Generation: {}".format(generation), True, white)
    canvas.blit(aliveText, (50, height-infospace+10))
    canvas.blit(genText, (200, height-infospace+10))
    nxt = [[None for j in range(rows)] for i in range(cols)]

    for i in range(cols):
        for j in range(rows):
            current = cells[i][j].state
            nhbs = cells[i][j].countAlive(cells)
            if (current == 0) and (nhbs == 3):
                nxt[i][j] = Cell(i, j, w, 1)
            elif (current == 1) and ((nhbs < 2) or (nhbs > 3)):
                nxt[i][j] = Cell(i, j, w, 0)
            else:
                nxt[i][j] = Cell(i, j, w, current)

    cells = nxt
    pygame.display.update()
