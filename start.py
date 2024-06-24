import pygame
import sys
import time

def main():
    pygame.init()

    pygame.display.set_caption("gun test")
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
    pygame.display.update()


if __name__  == "__main__":
    main()