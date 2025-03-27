import torch
import numpy
import pygame as pg
import random

import neural_network.network as network
import flappy_game.obstacle as obstacle
import flappy_game.flappy as flappy

def f(x):
    with torch.no_grad():
        pred = model(torch.tensor([x]).unsqueeze(1).float().to(device))
    print(pred.item())
    return pred.item()

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Rodando na {device}")

model = network.Network().to(device)
model.load_state_dict(torch.load("model/model.pt", weights_only=True))
model.eval()

data = []

pg.init()
screen = pg.display.set_mode((600, 350))
clock = pg.time.Clock()

running = True

obj1 = obstacle.Obstacle((255,0,0), [600, -215], [30,350], 100)
obj2 = obstacle.Obstacle((255,0,0), [600, 215], [30,350], 100)
obj3 = obstacle.Obstacle((255,255,0), [0, 0], [10,10], 100)
bird = flappy.Flappy((0,255,0), [300, 75], [20, 20], 600)

jump = 1
cooldown = 0.0

while running:
    click = 0
    dist = 0
    cooldown += clock.get_time()/1000

    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False
    
    screen.fill("blue")

    obj3.position = [175, obj1.position[1] + 390] 

    if obj1.position[0] > 0 :
        obj1.move(-1, clock.get_time()/1000)
        obj2.move(-1, clock.get_time()/1000)       
    else:
        v = random.choice([30, -30, 40, -40])
        obj1.position = [600, -215 + v]
        obj2.position = [600, 215 + v]
    
    dist = bird.position[1]-(obj1.position[1] + 390)

    if f(dist) >= 1:
        jump = -1
        cooldown = 0

    bird.position[1] += jump*300*clock.get_time()/1000

    if(cooldown > 0.1):
        jump = 1
        cooldown = 0
        bird.position[1] += jump*bird.force*clock.get_time()/1000

    bird.draw(screen)
    obj1.draw(screen)
    obj2.draw(screen)
    obj3.draw(screen)

    if bird.colli(obj1) or bird.colli(obj2) or bird.position[1] > 350:
        running = False

    pg.display.flip()
    clock.tick(60)

pg.quit()