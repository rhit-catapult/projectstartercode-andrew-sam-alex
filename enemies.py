import pygame
import sys
import random
import time

class enemy:
    def __init__(self, screen, x, y, r, hp, max_hp, main_img, main_frames, del_img, del_frames, start_img, start_frames, img_scale, img_offset_x, img_offset_y, id):
        self.screen = screen
        self.x = x - r/2
        self.y = y - r/2
        self.r = r
        self.hp = hp
        self.max_hp = max_hp
        self.main_frames = main_frames
        self.del_img = del_img
        self.main_img = main_img
        self.start_img = start_img
        self.del_frames = del_frames
        self.del_frame = 0
        self.main_frame = 0
        self.start_frame = 0
        self.initialized = 0
        self.on_screen = 1
        self.img_scale = img_scale
        self.img_offset_x = img_offset_x
        self.img_offset_y = img_offset_y
        self.id = id
        if start_img != 0:
            self.start_img = start_img
            self.start_frames = start_frames

    def render(self):
        pygame.draw.circle(self.screen, "blue", (self.x, self.y), self.r)

    def del_enemy(self, img_frames):
        cur_img = img_frames[self.del_frame]
        cur_img = pygame.transform.scale(cur_img, (self.r * self.img_scale, self.r * self.img_scale))
        self.screen.blit(cur_img, (self.x + self.r / 2 - self.r * self.img_scale / 2 + self.img_offset_x,
                                   self.y + self.r / 2 - self.r * self.img_scale / 2 + self.img_offset_y))
        self.del_frame += 1
        if self.del_frame == self.del_frames - 1: self.on_screen = 0

    def render_obj(self, img):
        cur_img = img
        cur_img = pygame.transform.scale(cur_img, (self.r * self.img_scale, self.r * self.img_scale))
        self.screen.blit(cur_img, (self.x + self.r/2 - self.r * self.img_scale/2 + self.img_offset_x, self.y + self.r/2 - self.r * self.img_scale/2 + self.img_offset_y))

    def initialize(self, img_array):
        cur_img = pygame.transform.scale(img_array[self.start_frame], (self.r * self.img_scale, self.r * self.img_scale))
        self.screen.blit(cur_img, (self.x + self.r/2 - self.r * self.img_scale/2 + self.img_offset_x, self.y + self.r/2 - self.r * self.img_scale/2 + self.img_offset_y))
        self.start_frame += 1
        if self.start_frame == self.start_frames - 1: self.initialized = 1

    def hit_by(self, dmg):
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] - self.x) ** 2 + (pygame.mouse.get_pos()[1] - self.y) ** 2 < self.r ** 2:
                self.hp -= dmg

                #print(f"{self.hp}/{self.max_hp}")

    def render_hp(self):
        pygame.draw.rect(self.screen, "red", (self.x, self.y - 50, self.r, 10))
        pygame.draw.rect(self.screen, "green", (self.x, self.y - 50, self.r * self.rp / self.max_hp, 10))

class moving_enemy(enemy):
    def __init__(self, screen,  start_x, start_y, end_x, end_y, w, h, hp, max_hp, speed, start_size, end_size):
        self.screen = screen
        self.x = start_x - w/2
        self.y = start_y - h/2
        self.w = w
        self.h = h
        self.hp = hp
        self.max_hp = max_hp
        self.start_x = start_x - w/2 * start_size
        self.start_y = start_y - h/2 * start_size
        self.end_x = end_x - w/2 * end_size
        self.end_y = end_y - h/2 * end_size
        self.speed = speed
        self.size = start_size
        self.start_size = start_size
        self.end_size = end_size
        if self.hp: self.hostile = 0
        else: self.hostile = 1
    def move_to_tar(self):
        if abs(self.x - self.end_x) > self.speed and abs(self.x - self.end_x) > self.speed:
            self.x += (self.end_x - self.start_x) / 300 * self.speed
            self.y += (self.end_y - self.start_y) / 300 * self.speed
            self.size += (self.end_size - self.size) / 300 * self.speed
        else:
            self.x = self.end_x
            self.y = self.end_y

    def render(self):
        pygame.draw.rect(self.screen, "blue", (self.x, self.y, self.w * self.size, self.h * self.size))

    def render_hp(self):
        pygame.draw.rect(self.screen, "red", (self.x, self.y - 50 * self.size, self.w * self.size, 10))
        pygame.draw.rect(self.screen, "green", (self.x, self.y - 50 * self.size, self.w * self.size * self.hp / self.max_hp, 10))
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    #test_enemy = enemy(screen, 500, 500, 50, 1, 1, "sprites/target/close/appear/spawn (44).png", 1, "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -25, 8, 0)
    non_moving = []
    states = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    start_frames = []
    del_frames = []
    main_img = pygame.image.load("sprites/target/close/appear/spawn (44).png")
    for i in range(1,44):
        start_frames.append(pygame.image.load(f"sprites/target/close/appear/spawn ({i}).png"))
    for i in range(1,19):
        del_frames.append(pygame.image.load(f"sprites/target/close/shot/despawn ({i}).png"))
    while 1:
        clock.tick(30)
        screen.fill(pygame.Color("white"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        for e in non_moving:
            states[e.id] = 1
            if e.initialized:
                if not e.on_screen:
                    non_moving.remove(e)
                    states[e.id] = 0
                elif e.hp <= 0:
                    e.del_enemy(del_frames)
                else:
                    e.hit_by(10)
                    e.render()
                    #e.render_hp()
                    e.render_obj(main_img)
            else:
                e.initialize(start_frames)

        for i in range(0,9):
            if states[i] == 0:
                if random.randint(1,200) == 49:
                    new_enemy = enemy(screen, i*50, 500, 50, 1, 1, "sprites/target/close/appear/spawn (44).png", 1, "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 1, -25, 8, i)
                    non_moving.append(new_enemy)
        pygame.display.update()
if __name__ == "__main__":
    main()