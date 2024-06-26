import pygame
import sys
import time

class Onion:
    def __init__(self, screen):
        self.screen = screen
        self.phase = 0
        self.images = []
        for k in range(301):
            newimage = pygame.image.load(f"cutscenes/good ending/loot ({k + 1}).png")
            self.images.append(newimage)
        self.onionring = pygame.mixer.Sound("sounds/Jerma985 - ONION RING POG!!!.mp3")
        self.congrat = pygame.mixer.Sound("sounds/congratulations-deep-voice-172193.mp3")
        self.good = pygame.mixer.Sound("sounds/goodresult-82807.mp3")

    def play(self):
        if self.phase == 1:
            self.onionring.play()
        if self.phase == 209:
            self.congrat.play()
        if self.phase == 1:
            self.good.play()
        if self.phase != 300:
            self.phase = self.phase + 1
        self.screen.blit(self.images[self.phase], (0,0))
        if self.phase == 300:
            sys.exit()




def main(screen):
    pygame.init()
    background = pygame.image.load("sprites/scene/test1.png")
    screen = pygame.display.set_mode((800, 800))
    load1 = pygame.image.load("loading screens/results.png")
    screen.blit(load1, (0, 0))
    pygame.display.update()
    clock = pygame.time.Clock()
    onion = Onion(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        clock.tick(30)
        screen.fill("black")
        screen.blit(background, (0,0))
        onion.play()
        pygame.display.update()
if __name__  == "__main__":
    main()