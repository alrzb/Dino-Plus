import pygame
import os


RUNNING = [
    pygame.image.load(os.path.join("assets/Dino", "DinoRun1.png")),
    pygame.image.load(os.path.join("assets/Dino", "DinoRun2.png")),
]
JUMPING = pygame.image.load(os.path.join("assets/Dino", "DinoJump.png"))
DUCKING = [
    pygame.image.load(os.path.join("assets/Dino", "DinoDuck1.png")),
    pygame.image.load(os.path.join("assets/Dino", "DinoDuck2.png")),
]
class Dinosaur:

    def __init__(self):
        self.running_images = RUNNING
        self.jumping_image = JUMPING
        self.ducking_images = DUCKING
        
        self.x_pos = 80
        self.y_pos = 310
        self.y_pos_duck = 340
        self.jump_vel = 8.5
        
        self.is_running = True
        self.is_jumping = False
        self.is_ducking = False
        self.step_index = 0
        
        self.image = self.running_images[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos

    def update(self, userInput):
        if self.is_ducking:
            self.duck()
        if self.is_running:
            self.run()
        if self.is_jumping:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.is_jumping:
            #Jump with KEY_UP if not jumpping already
            pygame.mixer.Sound("assets/Sounds/jump.mp3").play()
            self.is_ducking = False
            self.is_running = False
            self.is_jumping = True
        elif userInput[pygame.K_DOWN] and not self.is_jumping:
            #Duck with KEY_DOWN if not jumpping
            self.is_ducking = True
            self.is_running = False
            self.is_jumping = False
        elif not (self.is_jumping or userInput[pygame.K_DOWN]):
            #Run if no changes made
            self.is_ducking = False
            self.is_running = True
            self.is_jumping = False

    def run(self):
        self.image = self.running_images[self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos
        self.step_index += 1

    def jump(self):
        if self.is_jumping:
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -8.5:
            self.is_jumping = False
            self.is_running = True
            self.jump_vel = 8.5

    def duck(self):
        self.image = self.ducking_images[self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos_duck
        self.step_index += 1
        

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
