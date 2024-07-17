import pygame
import random
import os

CLOUD = pygame.image.load(os.path.join("assets/Other", "Cloud.png"))

class Cloud:
    def __init__(self):
        self.x = 1100 + random.randint(800, 1000)  # SCREEN_WIDTH is 1100
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()
        self.probability = 0.2

    def update(self, game_speed):
        self.x -= game_speed
        if self.x < -self.width:
            if random.random() < self.probability:
                self.x = 1100 + random.randint(2500, 3000)
                self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))
