import pygame
import os
import random

POTIONS = {'shield':
           pygame.image.load(os.path.join('assets/Potions', 'shield.png')),
           'heal':
           pygame.image.load(os.path.join('assets/Potions', 'heal.png')),
           'speed':
           pygame.image.load(os.path.join('assets/Potions', 'speed.png'))
           }
    
class Potion:
    def __init__(self, type):
        self.image = POTIONS
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = 1100
        self.rect.y = 325

    def update(self, game_speed):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            return True
        return False

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)
