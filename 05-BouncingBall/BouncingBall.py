import pygame
import sys
import random
import time
import math


# You will implement this module ENTIRELY ON YOUR OWN!

MAX_SPEED = 4
MIN_SIZE = 3
MAX_SIZE = 15
BALL_LIMIT = 100
BOUNCE_TIME_LIMIT = 1
BALL_OUTLINE = 1
SOUND = False

# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move
class Ball:
    def __init__(self, screen, color=None, x=None, y=None, radius=None, speed_x=None, speed_y=None, speed_adj = None,
                 shrink=False, grow=False, change_color=False, split=0, sound=None):
        self.screen = screen
        if (color == None):
            color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.color = color
        if(x == None):
            x = random.randint(0,screen.get_width())
        self.x = x
        if(y == None):
            y = random.randint(0,screen.get_height())
        self.y = y
        if(radius == None):
            radius = random.randint(MIN_SIZE, MAX_SIZE)
        self.radius = radius
        if(speed_x == None):
            speed_x = random.randint(-MAX_SPEED, MAX_SPEED)
        self.speed_x = speed_x
        if(speed_y == None):
            speed_y = random.randint(-MAX_SPEED, MAX_SPEED)
        self.speed_y = speed_y

        #weird ball mode settings
        #randomly shift the speed a little bit by this much after a bounce
        if(speed_adj == None):
            speed_adj = 0
        self.max_speed_adjustment = speed_adj
        self.shrink = shrink
        self.grow = grow
        self.last_grow_time = 0
        self.change_color = change_color
        self.split = split
        self.last_split_time = 0
        self.last_bounce_time = 0

        #for sound fin
        self.sound = sound

    def set_ball_modes(self, settings_array):
        self.shrink = settings_array[0]
        self.grow = settings_array[1]
        self.change_color = settings_array[2]
        self.split = settings_array[3]

    def randomize_ball_modes(self):
        settings = [random.choice([True, False]) for _ in range(3)]
        settings.append(random.randint(0,4))
        self.set_ball_modes(settings)

    def copy(self, other):
        self.screen = other.screen
        self.x = other.x
        self.y = other.y
        self.color = other.color
        self.radius = other.radius
        self.speed_x = other.speed_x
        self.speed_y = other.speed_y
        #copy the weird ball mode settings
        self.max_speed_adjustment = other.max_speed_adjustment
        self.shrink = other.shrink
        self.grow = other.grow
        self.change_color = other.change_color
        self.split = other.split


    def draw(self):
        pygame.draw.circle(self.screen, self.color,(self.x, self.y), self.radius)
        pygame.draw.circle(self.screen, (0,0,0),(self.x, self.y), self.radius+BALL_OUTLINE, BALL_OUTLINE)

    #returns a list of the balls remaining after this move
    def move(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y

        if (self.x < 0 or self.x+self.radius > self.screen.get_width()):
            balls = self.bounce()
            #scooch - keeps them from getting stuck along an edge
            if(self.x < 0):
                self.x += 1
            else:
                self.x -= 1
            self.speed_x = -self.speed_x
        elif (self.y < 0 or self.y+self.radius > self.screen.get_height()):
            balls = self.bounce()
            self.speed_y = -self.speed_y
            #scooch - keeps them from getting stuck along an edge
            if(self.y < 0):
                self.y += 1
            else:
                self.y -= 1
        else:
            balls = [self]

        return balls

    def modify_speed(self, max_change):
        x_change = random.randint(-max_change, max_change)
        y_change = random.randint(-max_change, max_change)
        #
        # if(self.speed_x > 0):
        #     self.speed_x += x_change
        # else:
        #     self.speed_x -= x_change
        #
        # if(self.speed_y > 0):
        #     self.speed_y += y_change
        # else:
        #     self.speed_y -= y_change
        self.speed_x += x_change
        self.speed_y += y_change


    #todo add sound effects here!
    def bounce(self):
        self.modify_speed(self.max_speed_adjustment)
        balls = []
        #shrink
        if(self.shrink):
            self.radius = self.radius - 3;

        #grow
        if(self.grow and time.time() - self.last_grow_time > BOUNCE_TIME_LIMIT):
            self.radius = self.radius + 3
            self.last_grow_time = time.time()

        if(self.radius < MIN_SIZE or self.radius > MAX_SIZE*2):
            #Pop!
            #don't return myself
            pass
        else:
            balls.append(self)
        #change color
        if(self.change_color):
            self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        #split
        if(self.split and time.time() - self.last_split_time > BOUNCE_TIME_LIMIT):
            self.split -= 1 #one lett time to split left
            new_ball = Ball(self.screen)
            new_ball.copy(self)
            new_ball.last_split_time = time.time() #dont immediately split the new ball yet
            new_ball.modify_speed(5)#make sure the new ball is moving a little different from me
            balls.append(new_ball)
            self.last_split_time = time.time()

        self.last_bounce_time = time.time()

        if(self.sound != None and SOUND == True):
            self.sound.play()

        return balls


def make_ball_at(screen, pos):
    new_ball = Ball(screen)
    new_ball.x = pos[0]
    new_ball.y = pos[1]
    return new_ball

def main():
    global SOUND #kinda sus - avoiding using globals like this, but this is just a setting, press M to toggle this
    pygame.init()
    screen = pygame.display.set_mode((1400, 800))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    bounce_sound = pygame.mixer.Sound("bounce.wav")

    # TODO: Create an instance of the Ball class called ball1
    ball1 = Ball(screen, (0, 255, 0), 50, 75, 10, 5, 5, sound=bounce_sound)
    balls = [ball1]
    NUM_BONUS_BALLS = 10
    for i in range(NUM_BONUS_BALLS):
        balls.append(Ball(screen))
        balls[-1].sound = bounce_sound
        balls[i+1].max_speed_adjustment = 1
        #balls[i].shrink = True
        #balls[i].grow = True #this causes weird behavior because we immediately bounce again since we're bigger, and infinitely get stuck on edge
        #balls[i].change_color = True
        #balls[i].split = 3

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                #add a new ball
                pos = event.pos
                balls.append(make_ball_at(screen, pos))
                balls[-1].sound = bounce_sound

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    SOUND = not SOUND


        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        next_balls = []
        ball_counter = 0
        for ball in balls:
            next_balls += ball.move()
            ball.draw()
            ball_counter += 1
            if(ball_counter > BALL_LIMIT):
                #skip the rest of the balls
                break

        balls = next_balls
        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
