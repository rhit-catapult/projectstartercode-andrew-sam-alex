#pygame.init()
#pygame.display.update()
#screen = screen = pygame.display.set_mode((width, height))
#img = pygame.image.load("imagefile")
#sound = pygame.mixer.Sound("soundfile")
#pygame.mixer.music.load("soundfile")
#font = pygame.font.Font(fontname, size)
#textimage = font.render(textvariable, antialiasing?, color)
'''        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()'''
#if event.type == pygame.EVENT
#do stuff
#pygame.image.load(filename)
#pygame.mouse.get_pos() returns mouse position
#pygame.mixer.music.play(-1) play music infinitely
#screen.fill(pygame.Color("Black"))
#!!!!!!!IMPORTANT screen.blit(img, (x,y))
'''class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        self.screen = screen
        self.x = x
        self.y = y
        # TODO 16: Initialize this Hero, as follows:
        self.image_umbrella = pygame.image.load(with_umbrella_filename)
        self.image_wo_umbrella = pygame.image.load(without_umbrella_filename)
        # TODO 16: Initialize this Hero, as follows:
        #     - Store the screen.
        #     - Set the initial position of this Hero to x and y.
        #     - Create an image of this Hero WITH    an umbrella to the given with_umbrella_filename.
        #     - Create an image of this Hero WITHOUT an umbrella to the given without_umbrella_filename.
        #     - Set the "last hit time" to 0.
        #   Use instance variables:
        #      screen  x  y  image_umbrella   image_no_umbrella  last_hit_time.
        self.last_hit_time = 0
    def draw(self):
        self.screen.blit(self.image_wo_umbrella, (self.x, self.y))
        """ Draws this sprite onto the screen. """
        # TODO 17: Draw (blit) this Hero, at this Hero's position, WITHOUT an umbrella:
        # TODO 21: Instead draw (blit) this Hero, at this Hero's position, as follows:
        #     If the current time is greater than this Hero's last_hit_time + 1,
        #       draw this Hero WITHOUT an umbrella,
        #       otherwise draw this Hero WITH an umbrella.
        pass
''' #OOP sample