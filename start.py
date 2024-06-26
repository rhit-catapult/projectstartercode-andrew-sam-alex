import pygame
import sys
import time
import gun
import goodending
import badending
import enemies
import random
class Twirl:
    def __init__ (self, screen, lmb):
        self.screen = screen
        self.lmb = 0
        self.phase = 0
        self.images = []
        self.prevent = 0
        for k in range(50):
            newimage = pygame.image.load(f"sprites/gun/twirl/twirl ({k + 1}).png").convert_alpha()
            self.images.append(newimage)

    def spin(self):
        if self.lmb == 1 and self.prevent != 1:
            self.phase = 1
            self.prevent = 1
        if self.phase > 0 and self.phase != 49:
            self.phase = self.phase + 1
            self.lmb = 1
            self.screen.blit(self.images[self.phase], (0,0))

class Wall:
    def __init__(self, screen, lmb):
        self.screen = screen
        self.lmb = 0
        self.phase = 0
        self.images = []
        self.prevent = 0
        for k in range(41):
            newimage = pygame.image.load(f"sprites/wall/curtan ({k + 1}).png").convert_alpha()
            self.images.append(newimage)

    def shatter(self):
        if self.phase != 40:
            if self.phase > 0:
                self.phase = self.phase + 1
            if self.lmb == 1 and self.prevent == 0:
                self.phase = 1
                self.prevent = 1
        self.screen.blit(self.images[self.phase], (0, 0))

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    load1 = pygame.image.load("loading screens/load.png")
    screen.blit(load1, (0, 0))
    pygame.display.set_caption("Loading ...")
    pygame.display.update()
    impact = pygame.mixer.Sound("sounds/bullet_impact.mp3")
    shoot = pygame.mixer.Sound("sounds/gunshot.mp3")
    shoot.set_volume(.3)
    reload = pygame.mixer.Sound("sounds/reload-123781.mp3")
    buzzer = pygame.mixer.Sound("sounds/startend_buzzer.mp3")
    pygame.mixer_music.load("sounds/Tough Guy Alert! - Mario & Luigi_ Bowser's Inside Story OST.mp3")
    screen.fill("white")
    twirl = Twirl(screen, 0)
    wall = Wall(screen, 0)
    clock = pygame.time.Clock()
    cutscene = 1
    outoftime = 1
    tar_1 = enemies.enemy(screen, 150, 385, 50, 1, 1, "sprites/target/close/appear/spawn (44).png", 1,
                  "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -25, 8, 1, 100)
    tar_2 = enemies.enemy(screen, 335, 385, 50, 1, 1, "sprites/target/close/appear/spawn (44).png", 1,
                  "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -25, 8, 2, 100)
    tar_3 = enemies.enemy(screen, 520, 385, 50, 1, 1, "sprites/target/close/appear/spawn (44).png", 1,
                  "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -25, 8, 3, 100)
    tar_4 = enemies.enemy(screen, 705, 385, 50, 1, 1, "sprites/target/close/appear/spawn (44).png", 1,
                  "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -25, 8, 4, 100)
    tar_5 = enemies.enemy(screen, 237, 455, 25, 1, 1, "sprites/target/close/appear/spawn (44).png", 1,
                  "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -12, 3, 5, 200)
    tar_6 = enemies.enemy(screen, 412, 455, 25, 1, 1, "sprites/target/close/appear/spawn (44).png", 1,
                  "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -12, 3, 6, 200)
    tar_7 = enemies.enemy(screen, 585, 455, 25, 1, 1, "sprites/target/close/appear/spawn (44).png", 1,
                  "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -12, 3, 7, 200)
    tar_8 = enemies.enemy(screen, 237, 190, 25, 1, 1, "sprites/target/close/appear/spawn (44).png", 1,
                  "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -12, 3, 8, 300)
    tar_9 = enemies.enemy(screen, 412, 190, 25, 1, 1, "sprites/target/close/appear/spawn (44).png", 1,
                  "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -12, 3, 9, 300)
    tar_10 = enemies.enemy(screen, 585, 190, 25, 1, 1, "sprites/target/close/appear/spawn (44).png", 1,
                   "sprites/target/close/shot/despawn", 19, "sprites/target/close/appear/spawn", 44, 19, -12, 3, 10,
                   300)
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
    timeleft = 69
    game = False
    the_gun = gun.Gun(screen, 0, lmb=0)
    reticle = gun.Reticle(screen, 1)
    particle = gun.Particle(screen, 0, 0)
    clock = pygame.time.Clock()
    while True:
        pygame.display.set_caption("Target Shooter, Quest for the Onion Ring")
        clock.tick(30)
        screen.fill((0, 0, 0))
        if not game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game = True
                    pygame.mixer_music.play()
                    init_tick = pygame.time.get_ticks()
                    reload.play()
        if game:
            twirl.lmb = 1
            wall.lmb = 1
            seconds = (pygame.time.get_ticks() - init_tick) / 1000
            clicking = False
            storeprevscore = score
            animate += 1
            if animate > cycle:
                animate = 0
            screen.blit(bg, (0, 0))
            if score < 20000: textimage = font.render(str(score)+"/20000", True, "white")
            else: textimage = font.render(str(score)+"/20000", True, "green")
            screen.blit(textimage, (300, 50))
            if timeleft > 0: timeleft = int(120 - seconds)
            if timeleft > 10:
                timeimage = font.render(str(timeleft), True, "white")
            else:
                timeimage = font.render(str(timeleft), True, "red")
            screen.blit(timeimage, (725, 50))
            for e in non_moving:
                if e.initialized:
                    if e.hp <= 0:
                        if states[e.id - 1] == 1:
                            score += e.score
                        states[e.id - 1] = 0

                        e.del_enemy()
                    else:
                        # e.hit_by(10)
                        #e.render()
                        # e.render_hp()
                        e.render_obj()
                else:
                    if random.randint(1, 100) == e.id:
                        e.initializing = True
                    if e.initializing:
                        states[e.id - 1] = 1
                        e.initialize()
                if e.id == 1:
                    if animate <= cycle / 2:
                        screen.blit(f1, (0, 0))
                    else:
                        screen.blit(f2, (0, 0))
                if e.id == 5:
                    screen.blit(m, (0, 0))
                if e.id == 8:
                    if animate <= cycle / 2:
                        screen.blit(t1, (0, 0))
                    else:
                        screen.blit(t2, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    shoot.play()

                    punish = True
                    the_gun.lmb = 1
                    reticle.lmb = 1
                    the_gun.start = 0
                    particle.x = pygame.mouse.get_pos()[0] - 400
                    particle.y = pygame.mouse.get_pos()[1] - 400
                    particle.phase = 1
                    particle.lmb = 1
                    for e in non_moving:
                        if not e.initialized:
                            continue
                        state1 = e.hp
                        e.hit_by(10)
                        state2 = e.hp
                        if state1 > state2:
                            punish = False
                            impact.play()
                    if punish and score > 0:
                        score -= 50
            the_gun.shoot()
            the_gun.location()
            reticle.animate()
            reticle.move()
            particle.animate()
            the_gun.draw()
            reticle.draw()
            if timeleft == 0:
                outoftime = 0
                if score >= 20000: cutscene = 1
                else: cutscene = 0
        if outoftime != 0:
            wall.shatter()
        if outoftime == 0:
            pygame.mixer_music.stop()
            buzzer.play()
            if cutscene == 1:
                goodending.main(screen)
            if cutscene == 0:
                badending.main(screen)
        pygame.display.update()



if __name__  == "__main__":
    main()