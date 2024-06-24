import pygame
import sys
import time


class Gun:
    def __init__(self, screen, x, lmb,):
        self.screen = screen
        self.x = x
        self.lmb = 0
        self.xnew = 0
        self.angle = 0
        self.shooting = False
        self.recoil = 0
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
        if self.start < 5 and self.recoil < 30:
            self.recoil = self.recoil + 10
        if self.start > 2:
            self.lmb = 0
        self.start = self.start + 1
        if self.recoil > 0 and self.start > 5:
            self.recoil = self.recoil - 10


    def location(self):

       if pygame.mouse.get_pos()[0] < 300:
           self.angle = 1
       elif pygame.mouse.get_pos()[0] > 500:
           self.angle = 2
       else:
           self.angle = 0

       self.xnew = (pygame.mouse.get_pos()[0] - 400) / 20

    def draw(self):
        if self.lmb == 1:
            fire = 3
        else:
            fire = 0
        image_index = self.angle + fire
        self.screen.blit(self.images[image_index], (self.xnew, self.recoil))

class Reticle:
    def __init__(self, screen, lmb):
        self.screen = screen
        self.lmb = 0
        self.loop = 1
        self.images = []
        self.x = 0
        self.y = 0
        self.phase = 0
        for k in range(11):
            newimage = pygame.image.load(f"sprites/gun/ret/ret ({k+1}).png")
            self.images.append(newimage)

    def animate(self):
        if self.phase >= 1:
            self.phase = self.phase + 1
        if self.lmb == 1:
            self.phase = 1
            self.lmb = 0
        if self.phase == 11:
            self.phase = 0

    def draw(self):
        self.screen.blit(self.images[self.phase], (self.x,self.y))
    def move(self):
        self.x = pygame.mouse.get_pos()[0] - 400
        self.y = pygame.mouse.get_pos()[1] - 400

class Particle:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.phase = 0
        self.lmb = 0
        self.particleimages = []
        for k in range(8):
            newimage = pygame.image.load(f"sprites/gun/hit/hit ({k + 1}).png")
            self.particleimages.append(newimage)


    def animate(self):
        if self.lmb == 1:
            self.phase = self.phase + 1
            self.lmb = 0
        if self.phase == 7:
            self.phase = 0
        if self.phase > 0:
            self.screen.blit(self.particleimages[self.phase], (self.x, self.y))
            self.phase = self.phase + 1


def main(screen):
    gun = Gun(screen, 0, lmb=0)
    reticle = Reticle(screen, 1)
    particle = Particle(screen, 0, 0)
    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                gun.lmb = 1
                reticle.lmb = 1
                gun.start = 0
                particle.x = pygame.mouse.get_pos()[0] - 400
                particle.y = pygame.mouse.get_pos()[1] - 400
                particle.phase = 1
                particle.lmb = 1

        gun.shoot()
        gun.location()
        reticle.animate()
        reticle.move()
        particle.animate()
        gun.draw()
        reticle.draw()
        pygame.display.update()


if __name__  == "__main__":
    main()
