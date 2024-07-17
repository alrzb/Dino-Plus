import pygame
import os
import random
from dinosaur import Dinosaur, RUNNING
from obstacles import *
from potions import *
from cloud import Cloud
import datetime

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Dino-Plus")

Ico = pygame.image.load("assets/DinoWallpaper.png")
pygame.display.set_icon(Ico)

BG = pygame.image.load(os.path.join("assets/Other", "Track.png"))
GAMEOVER = pygame.image.load(os.path.join("assets/Other", "GameOver.png"))

HEAL_ICON = pygame.image.load(os.path.join("assets/Potions", "heal_icon.png"))
SHIELD_ICON = pygame.image.load(os.path.join("assets/Potions", "shield_icon.png"))


def set_theme():
    global FONT_COLOR, SCREEN_COLOR, is_day
    if is_day:
        FONT_COLOR = (0, 0, 0)
        SCREEN_COLOR = (255, 255, 255)
    else:
        FONT_COLOR = (255, 255, 255)
        SCREEN_COLOR = (0, 0, 0)

def display_story():
    story_text = [
        "In a prehistoric land, a dinosaur named Drax lived a peaceful life.",
        "One day, while grazing under the sun, the ground suddenly shook!",
        "Looking up, Drax saw a bright meteorite hurtling toward Earth, lighting up the sky with flames.",
        "Panic spread as the meteorite got closer, bringing destruction with it.",
        "With adrenaline pumping, Drax ran from the impact zone, his strong legs propelling him forward.",
        "The once calm landscape turned into chaos as Drax dodged falling debris and rough terrain, determined to escape the impending disaster.",
        "Press S to Run!"
    ]

    SCREEN.fill(SCREEN_COLOR)
    font = pygame.font.Font("assets\Fonts\OpenSans_Condensed-Bold.ttf", 20)  # Replace with your preferred font and size
    text_lines = []
    
    for line in story_text:
        words = line.split(' ')
        wrapped_lines = []
        current_line = ''
        
        for word in words:
            test_line = current_line + word + ' '
            
            if font.size(test_line)[0] < SCREEN_WIDTH - 40:  # Adjusted to fit within the screen width
                current_line = test_line
            else:
                wrapped_lines.append(current_line)
                current_line = word + ' '
        
        wrapped_lines.append(current_line)
        for wrapped_line in wrapped_lines:
            text = font.render(wrapped_line, True, FONT_COLOR)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, len(text_lines) * 30 + 50))  # Adjust vertical spacing as needed
            text_lines.append((text, text_rect))
    
    for text, text_rect in text_lines:
        SCREEN.blit(text, text_rect)

    pygame.display.update()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                waiting = False

def main():
    global game_speed, x_pos_BG, y_pos_BG, points, obstacles, has_shield, has_heal, shield_enabled
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    x_pos_BG = 0
    y_pos_BG = 380
    points = 0
    pause = False

    has_heal = False
    has_shield = False
    shield_enabled = False

    potions = []
    obstacles = []
    game_speed = 20
    font = pygame.font.Font("freesansbold.ttf", 20)
    death_count = 0

    def background():
        global x_pos_BG, y_pos_BG
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_BG, y_pos_BG))
        SCREEN.blit(BG, (image_width + x_pos_BG, y_pos_BG))
        if x_pos_BG <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_BG, y_pos_BG))
            x_pos_BG = 0
        x_pos_BG -= game_speed

    def score():
        global points, game_speed, highscore, is_day
        points += 1
        if points % 100 == 0:
            game_speed += 1
        if points > highscore:
            highscore = points
        if points % 2000 == 0: #Toggle day/night mode every 2000 points
            is_day = not is_day
        if points % 1000: # heal potion every 1000 points
            heal = Potion('heal')
            potions.append(heal) 
        if points % 700 == 0: # Speed potion every 700 points
            speed = Potion('speed')
            potions.append(speed)
        if points == 2700: # shield potion every 2700 points
            shield = Potion('shield')
            potions.append(shield)

        score_text = font.render("Score: " + str(points), True, FONT_COLOR)
        score_text_rect = score_text.get_rect()
        score_text_rect.topleft = (10, 10)

        highscore_text = font.render("High Score: " + str(highscore), True, FONT_COLOR)
        highscore_text_rect = highscore_text.get_rect()
        highscore_text_rect.topleft = (10, score_text_rect.bottom + 5)

        SCREEN.blit(score_text, score_text_rect)
        SCREEN.blit(highscore_text, highscore_text_rect)

    def unpause():
        nonlocal pause, run
        pause = False
        run = True

    def paused():
        nonlocal pause
        pause = True
        font = pygame.font.Font("freesansbold.ttf", 30)
        text = font.render("Game Paused, Press 'U' to Unpause", True, FONT_COLOR)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT  // 3)
        SCREEN.blit(text, textRect)
        pygame.display.update()

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                    unpause()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                run = False
                paused()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_h and has_shield:
                    shield_enabled = True
                    has_shield = False
                    shield_enabled_time = pygame.time.get_ticks()

        set_theme()

        SCREEN.fill(SCREEN_COLOR)
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        if shield_enabled:
            shield_status = font.render(f'Shield: {15 - (pygame.time.get_ticks() - shield_enabled_time) // 1000}s Left',
                                        True, FONT_COLOR)
            shield_status_rect = shield_status.get_rect()
            shield_status_rect.center = (SCREEN_WIDTH // 2, 10)
            shield_status_rect.top = 10
            SCREEN.blit(shield_status, shield_status_rect)

        if has_heal:
            SCREEN.blit(HEAL_ICON, (player.rect.right + 10, player.rect.top))
        if has_shield:
            SCREEN.blit(SHIELD_ICON, (player.rect.right + 10, player.rect.top + 20))
            
        cloud.draw(SCREEN)
        cloud.update(game_speed)

        background()
        score()

        if len(obstacles) == 0:
            if (obs_type := random.randint(0, 2)) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif obs_type == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif obs_type == 2:
                obstacles.append(Bird(BIRD))

        for potion in potions:
            potion.draw(SCREEN)
            if potion.update(game_speed):
                potions.pop(0)
            if player.rect.colliderect(potion.rect):
                potions.pop(0)
                if potion.type == 'heal':
                    pygame.mixer.Sound("assets/Sounds/heal.mp3").play()
                    has_heal = True
                if potion.type == 'shield':
                    pygame.mixer.Sound("assets/Sounds/shield.mp3").play()
                    has_shield = True
                if potion.type == 'speed':
                    change_factor = random.choice((0.5, 2))
                    game_speed = game_speed * change_factor
                
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            if obstacle.update(game_speed):
                obstacles.pop(0)
            if player.rect.colliderect(obstacle.rect) and obstacle.deathful:
                pygame.mixer.Sound("assets/Sounds/ouch.mp3").play()
                if not (shield_enabled or has_heal):
                    death_count += 1
                    pygame.mixer.Sound("assets/Sounds/game-over.mp3").play()
                    game_over_screen()
                    menu(death_count)
                else:
                    if shield_enabled:
                        obstacle.deathful = False # Use shield and neutralize the obstecle
                    if has_heal:
                        obstacle.deathful = False # Use heal and neutralize the obstecle
                        has_heal = False

        if shield_enabled:
            current_time = pygame.time.get_ticks()
            if current_time - shield_enabled_time >= 15000:
                shield_enabled = False

        clock.tick(30)
        pygame.display.update()

def menu(death_count):
    global highscore, is_day
    current_hour = datetime.datetime.now().hour
    is_day = 6 <= current_hour < 18
    set_theme()
    display_story()

    run = True
    while run:
        SCREEN.fill(SCREEN_COLOR)
        font = pygame.font.Font("freesansbold.ttf", 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, FONT_COLOR)
            highscore = get_highscore()

        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, FONT_COLOR)
            score = font.render("Your Score: " + str(points), True, FONT_COLOR)
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
            if get_highscore() < highscore:
                new_highscore = highscore
                write_highscore(new_highscore)

        hs_score_text = font.render("High Score : " + str(highscore), True, FONT_COLOR)  
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        hs_score_rect = hs_score_text.get_rect()
        hs_score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
        SCREEN.blit(hs_score_text, hs_score_rect)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                main()

def game_over_screen():
    SCREEN.blit(GAMEOVER, (SCREEN_WIDTH // 2 - GAMEOVER.get_width() // 2, SCREEN_HEIGHT // 2 - 70))
    pygame.display.update()
    pygame.time.delay(2000)

def get_highscore():
    try:
        with open('highscore.txt', mode='r') as file:
            return int(file.readlines()[0])
    except:
        return 0

def write_highscore(new_highscore):
    with open('highscore.txt', mode='w') as file:
        file.write(str(new_highscore))
    
if __name__ == '__main__':
    menu(death_count=0)
