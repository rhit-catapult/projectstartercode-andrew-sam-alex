import pygame
import sys
import time


class Gun:
    def __init__(self, screen, x, lmb):
        self.screen = screen
        self.x = x
        self.lmb = 0
        self.angle = 0
        self.shooting = False
        # self.image = pygame.image.load("sprites/gun/aim/aim (1).png")
        self.images = []
        self.start = 20
        self.click = False
        for k in range(6):
            newimage = pygame.image.load(f"sprites/gun/aim/aim ({k+1}).png")
            self.images.append(newimage)

    def shoot(self):
        if self.start < 5:
            self.lmb = 1
        if self.start > 5:
            self.lmb = 0
        self.start = self.start + 1

    def location(self):
       if pygame.mouse.get_pos()[0] < 200:
           self.angle = 1
       elif pygame.mouse.get_pos()[0] > 600:
           self.angle = 2
       else:
           self.angle = 0
    def draw(self):
        if self.lmb == 1:
            fire = 3
        else:
            fire = 0
        image_index = self.angle + fire
        self.screen.blit(self.images[image_index], (self.x, 0))
        print(self.start)
def main():
    pygame.init()
    pygame.display.set_caption("gun test")
    screen = pygame.display.set_mode((800, 800))
    gun = Gun(screen, 0, lmb=0)
    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                gun.lmb = 1
                gun.start = 0

        gun.shoot()
        screen.fill((255, 255, 255))
        gun.location()
        gun.draw()
        pygame.display.update()


if __name__  == "__main__":
    main()