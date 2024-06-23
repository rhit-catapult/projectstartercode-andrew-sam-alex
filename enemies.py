import pygame
import sys
import random
import time

class enemy:
    def __init__(self, screen, x, y, w, h, hp, max_hp):
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = hp
        self.max_hp = max_hp

    def render(self):
        pygame.draw.rect(self.screen, "blue", (self.x, self.y, self.w, self.h))


    def hit_by(self):
        if pygame.mouse.get_pressed()[0]:
            if pygame.mouse.get_pos()[0] > self.x and pygame.mouse.get_pos()[0] < self.x + self.w and pygame.mouse.get_pos()[1] > self.y and pygame.mouse.get_pos()[0] < self.y + self.h:
                self.hp -= 1
                print(f"{self.hp}/{self.max_hp}")
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 700))
    clock = pygame.time.Clock()
    fleet = []
    test_enemy = enemy(screen, 200, 200, 100, 200, 200, 200)
    fleet.append(test_enemy)
    while 1:
        clock.tick(30)
        screen.fill(pygame.Color("Black"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        for e in fleet:
            e.hit_by()
            e.render()
            if e.hp <= 0:
                fleet.remove(e)
        pygame.display.update()
if __name__ == "__main__":
    main()