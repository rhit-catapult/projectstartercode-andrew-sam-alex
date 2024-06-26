import pygame
import sys
import time
import math

class Earth:
    def __init__(self, screen):
        self.screen = screen
        self.phase = 0
        self.images = []
        for k in range(301):
            if k > 0:
                newimage = pygame.image.load("cutscenes/bad ending/end"+"0" * (4 - (math.floor(math.log(k, 10))+1)) + str(k) + ".png")
                self.images.append(newimage)
            else:
                newimage = pygame.image.load("cutscenes/bad ending/end0000.png")
                self.images.append(newimage)

    def play(self):
        if self.phase != 300:
            self.phase = self.phase + 1
        self.screen.blit(self.images[self.phase], (0,0))
        if self.phase == 300:
            sys.exit()




def main(screen):
    pygame.init()
    background = pygame.image.load("sprites/scene/test1.png")
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    earth = Earth(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        clock.tick(30)
        screen.fill("black")
        screen.blit(background, (0,0))
        earth.play()
        pygame.display.update()
if __name__  == "__main__":
    main()