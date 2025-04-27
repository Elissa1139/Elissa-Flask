import pygame
import time
import random

WIDTH,HEIGHT=1000,800
WIN=pygame.display.set_mode ((WIDTH,HEIGHT))
pygame.display.set_caption("Baking adventure")

BG = pygame.image.load("static/images/Gamebackground.jpeg")
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

PLAYER_WIDTH= 40
PLAYER_HEIGHT = 60

def draw(Player):
    WIN.blit(BG, (0,0))
    pygame.display.update()

def main():
    player = pygame.Rect(200, HEIGHT-PLAYER_HEIGHT,PLAYER_WIDTH,PLAYER_HEIGHT )
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(player)  # <--- move this inside the loop

    pygame.quit()


    pygame.quit()

if __name__ == "__main__":
    main()
