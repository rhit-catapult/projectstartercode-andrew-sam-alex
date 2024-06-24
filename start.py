import pygame
import sys
import time
import gun
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




def main():
    pygame.init()
    pygame.display.set_caption("gun test")
    screen = pygame.display.set_mode((800, 800))
    twirl = Twirl(screen, 0)
    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                twirl.lmb = 1
        screen.fill((0, 0, 0))
        twirl.spin()
        pygame.display.update()


if __name__  == "__main__":
    main()