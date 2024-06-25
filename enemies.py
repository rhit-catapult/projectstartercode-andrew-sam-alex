import pygame
import sys
import random
import time
class enemy:
    def __init__(self, screen, x, y, r, hp, max_hp, main_img, main_frames, del_img, del_frames, start_img, start_frames, img_scale, img_offset_x, img_offset_y, id, score):
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
        self.initializing = True
        self.on_screen = 1
        self.img_scale = img_scale
        self.img_offset_x = img_offset_x
        self.img_offset_y = img_offset_y
        self.id = id
        self.start_array = []
        self.del_array = []
        self.main_img = main_img
        self.score = score
        for i in range(1, start_frames + 1):
            cur_img = pygame.image.load(start_img + f" ({i}).png").convert_alpha()
            cur_img = pygame.transform.scale(cur_img, (self.r * self.img_scale, self.r * self.img_scale))
            self.start_array.append(cur_img)
        for i in range(1, del_frames + 1):
            cur_img = pygame.image.load(del_img + f" ({i}).png").convert_alpha()
            cur_img = pygame.transform.scale(cur_img, (self.r * self.img_scale, self.r * self.img_scale))
            self.del_array.append(cur_img)
        cur_img = pygame.image.load(main_img).convert_alpha()
        self.main_img = pygame.transform.scale(cur_img, (self.r * self.img_scale, self.r * self.img_scale))
        if start_img != 0:
            self.start_img = start_img
            self.start_frames = start_frames

    def render(self):
        pygame.draw.circle(self.screen, "blue", (self.x, self.y), self.r)

    def del_enemy(self):
        cur_img = self.del_array[self.del_frame]
        self.screen.blit(cur_img, (self.x + self.r / 2 - self.r * self.img_scale / 2 + self.img_offset_x,
                                   self.y + self.r / 2 - self.r * self.img_scale / 2 + self.img_offset_y))
        self.del_frame += 1
        if self.del_frame == self.del_frames:
            self.initialized = 0
            self.on_screen = 0
            self.del_frame = 0

    def render_obj(self):
        cur_img = self.main_img
        self.screen.blit(cur_img, (self.x + self.r/2 - self.r * self.img_scale/2 + self.img_offset_x, self.y + self.r/2 - self.r * self.img_scale/2 + self.img_offset_y))

    def initialize(self):
        self.hp = 1
        self.on_screen = 1
        cur_img = self.start_array[self.start_frame]
        self.screen.blit(cur_img, (self.x + self.r/2 - self.r * self.img_scale/2 + self.img_offset_x, self.y + self.r/2 - self.r * self.img_scale/2 + self.img_offset_y))
        self.start_frame += 1
        self.initializing = True
        if self.start_frame == self.start_frames:
            self.initialized = 1
            self.start_frame = 0
            self.initializing = False

    def hit_by(self, dmg):
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
    tar_1 = enemy(screen, 150, 385, 50, 1, 1, "sprites/target/close/appear/spawn (44).png", 1,
                  "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -25, 8, 1, 100)
    tar_2 = enemy(screen, 335, 385, 50, 1, 1, "sprites/target/close/appear/spawn (44).png", 1,
                  "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -25, 8, 2, 100)
    tar_3 = enemy(screen, 520, 385, 50, 1, 1, "sprites/target/close/appear/spawn (44).png", 1,
                  "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -25, 8, 3, 100)
    tar_4 = enemy(screen, 705, 385, 50, 1, 1, "sprites/target/close/appear/spawn (44).png", 1,
                  "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -25, 8, 4, 100)
    tar_5 = enemy(screen, 237, 455, 25, 1, 1, "sprites/target/close/appear/spawn (44).png", 1,
                  "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -12, 3, 5, 200)
    tar_6 = enemy(screen, 412, 455, 25, 1, 1, "sprites/target/close/appear/spawn (44).png", 1,
                  "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -12, 3, 6, 200)
    tar_7 = enemy(screen, 585, 455, 25, 1, 1, "sprites/target/close/appear/spawn (44).png", 1,
                  "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -12, 3, 7, 200)
    tar_8 = enemy(screen, 237, 190, 25, 1, 1, "sprites/target/close/appear/spawn (44).png", 1,
                  "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -12, 3, 8, 300)
    tar_9 = enemy(screen, 412, 190, 25, 1, 1, "sprites/target/close/appear/spawn (44).png", 1,
                  "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -12, 3, 9, 300)
    tar_10 = enemy(screen, 585, 190, 25, 1, 1, "sprites/target/close/appear/spawn (44).png", 1,
                   "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -12, 3, 10, 300)
    non_moving = [tar_10, tar_9, tar_8, tar_7, tar_6, tar_5, tar_4, tar_3, tar_2, tar_1]
    states = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    bg = pygame.image.load("sprites/scene/background.png").convert_alpha()
    f1 = pygame.image.load("sprites/scene/front1.png").convert_alpha()
    f2 = pygame.image.load("sprites/scene/front2.png").convert_alpha()
    m = pygame.image.load("sprites/scene/mid.png").convert_alpha()
    t1 = pygame.image.load("sprites/scene/top1.png").convert_alpha()
    t2 = pygame.image.load("sprites/scene/top2.png").convert_alpha()
    score = 0
    font = pygame.font.SysFont("impact", 50)
    animate = 0
    cycle = 30
    init_tick = pygame.time.get_ticks()
    timeleft = 69
    while 1:
        clock.tick(30)
        seconds = (pygame.time.get_ticks() - init_tick) / 1000
        clicking = False
        storeprevscore = score
        animate += 1
        if animate > cycle:
            animate = 0
        screen.fill(pygame.Color("white"))
        screen.blit(bg, (0, 0))
        textimage = font.render(str(score), True, "white")
        screen.blit(textimage, (350, 50))
        if timeleft > 0: timeleft = int(125 - seconds)
        if timeleft > 10: timeimage = font.render(str(timeleft), True, "white")
        else: timeimage = font.render(str(timeleft), True, "red")
        screen.blit(timeimage, (725, 50))
        for e in non_moving:
            if e.initialized:
                if e.hp <= 0:
                    if states[e.id - 1] == 1:
                        score += e.score
                    states[e.id - 1] = 0
                    e.del_enemy()
                else:
                    #e.hit_by(10)
                    e.render()
                    #e.render_hp()
                    e.render_obj()
            else:
                if random.randint(1, 100) == e.id:
                    e.initializing = True
                if e.initializing:
                    states[e.id - 1] = 1
                    e.initialize()
            if e.id == 1:
                if animate <= cycle/2: screen.blit(f1, (0,0))
                else: screen.blit(f2, (0,0))
            if e.id == 5:
                screen.blit(m, (0,0))
            if e.id == 8:
                if animate <= cycle/2:
                    screen.blit(t1, (0, 0))
                else:
                    screen.blit(t2, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                punish = True
                for e in non_moving:
                    if not e.initialized:
                        continue
                    state1 = e.hp
                    e.hit_by(10)
                    state2 = e.hp
                    if state1 > state2:
                        punish = False
                        break
                if punish and score > 0:
                    score -=50
        pygame.display.update()
if __name__ == "__main__":
    main()