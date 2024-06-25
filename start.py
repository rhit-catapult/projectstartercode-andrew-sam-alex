import pygame
import sys
import time
import gun
import goodending
import badending
class Twirl:
    def __init__ (self, screen, lmb):
        self.screen = screen
        self.lmb = 0
        self.phase = 0
        self.images = []
        self.prevent = 0
        for k in range(50):
            newimage = pygame.image.load(f"sprites/gun/twirl/twirl ({k + 1}).png")
            self.images.append(newimage)

    def spin(self):
        if self.lmb == 1 and self.prevent != 1:
            self.phase = 1
            self.prevent = 1
        if self.phase > 0 and self.phase != 49:
            self.phase = self.phase + 1
            self.lmb = 1
            self.screen.blit(self.images[self.phase], (0,0))
        if self.phase == 49:
            gun.main(self.screen)

class Wall:
    def __init__(self, screen, lmb):
        self.screen = screen
        self.lmb = 0
        self.phase = 0
        self.images = []
        self.prevent = 0
        for k in range(41):
            newimage = pygame.image.load(f"sprites/wall/curtan ({k + 1}).png")
            self.images.append(newimage)

    def shatter(self):
        if self.phase != 40:
            if self.phase > 0:
                self.phase = self.phase + 1
            if self.lmb == 1 and self.prevent == 0:
                self.phase = 1
                self.prevent = 1
        self.screen.blit(self.images[self.phase], (0, 0))
pygame.display.set_caption("Loading ...")
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    screen.fill("white")
    twirl = Twirl(screen, 0)
    wall = Wall(screen, 0)
    clock = pygame.time.Clock()
    cutscene = 0
    outoftime = 120
    while True:
        pygame.display.set_caption("Target Shooter, Quest for the Onion Ring")
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                twirl.lmb = 1
                wall.lmb = 1
        if outoftime != 0:
            screen.fill((0, 0, 0))
            wall.shatter()
            twirl.spin()
        if outoftime == 0:
            if cutscene == 1:
                goodending.main(screen)
            if cutscene == 0:
                badending.main(screen)
        pygame.display.update()



if __name__  == "__main__":
    main()