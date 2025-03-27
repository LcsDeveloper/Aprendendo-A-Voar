import pygame as pg

class Obstacle():
    def __init__(self, color: tuple, position: list[int], size: list[int], speed: float):
        self.color = color
        self.position = position
        self.size = size
        self.speed = speed
        self.rect = pg.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
    
    def draw(self, screen) -> None:
        self.rect = pg.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        pg.draw.rect(screen, self.color, self.rect)

    def move(self, direction: int, deltatime: float) -> None:
        self.position[0] = self.position[0] + direction*self.speed*deltatime
    
    def colli(self, obj) -> bool:
        return self.rect.colliderect(obj.rect)
