import pygame
import sys
import time

class Earth:
    def __init__(self, screen):
        self.screen = screen
        self.phase = 0
        self.images = []
        for k in range(301):
            newimage = pygame.image.load(f"cutscenes/bad ending/end ({k + 1}).jpg")
            self.images.append(newimage)

    def play(self):
        if self.phase != 300:
            self.phase = self.phase + 1
        self.screen.blit(self.images[self.phase], (0,0))
        if self.phase == 300:
            sys.exit()




def main():
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