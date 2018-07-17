import numpy

infospace = 35
size = width, height = 1300, 400 + infospace
w = 10
cols = int(width / w)
rows = int((height-infospace) / w)

black = (0, 0, 0)
white = (255, 255, 255)
grey = (51, 51, 51)
yellow = (255, 255, 0)
green = (0, 255, 0)

def randomAlive(p, mesh):
    for i in range(cols):
        for j in range(rows):
            if numpy.random.uniform() < p:
                mesh[i][j].state = 1

def gliderGun(x, y, mesh):
    alive = list()

    alive.append(mesh[x+0][y+4])
    alive.append(mesh[x+0][y+5])
    alive.append(mesh[x+1][y+4])
    alive.append(mesh[x+1][y+5])

    alive.append(mesh[x+10][y+4])
    alive.append(mesh[x+10][y+5])
    alive.append(mesh[x+10][y+6])
    alive.append(mesh[x+11][y+3])
    alive.append(mesh[x+11][y+7])
    alive.append(mesh[x+12][y+2])
    alive.append(mesh[x+12][y+8])
    alive.append(mesh[x+13][y+2])
    alive.append(mesh[x+13][y+8])
    alive.append(mesh[x+14][y+5])
    alive.append(mesh[x+15][y+3])
    alive.append(mesh[x+15][y+7])
    alive.append(mesh[x+16][y+4])
    alive.append(mesh[x+16][y+5])
    alive.append(mesh[x+16][y+6])
    alive.append(mesh[x+17][y+5])

    alive.append(mesh[x+20][y+2])
    alive.append(mesh[x+20][y+3])
    alive.append(mesh[x+20][y+4])
    alive.append(mesh[x+21][y+2])
    alive.append(mesh[x+21][y+3])
    alive.append(mesh[x+21][y+4])
    alive.append(mesh[x+22][y+1])
    alive.append(mesh[x+22][y+5])

    alive.append(mesh[x+24][y+0])
    alive.append(mesh[x+24][y+1])
    alive.append(mesh[x+24][y+5])
    alive.append(mesh[x+24][y+6])

    alive.append(mesh[x+34][y+2])
    alive.append(mesh[x+34][y+3])
    alive.append(mesh[x+35][y+2])
    alive.append(mesh[x+35][y+3])

    for cell in alive:
        cell.state = 1
