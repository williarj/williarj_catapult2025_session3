import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        # TODO 8: Initialize this Raindrop, as follows:
        #     - Store the screen.
        #     - Set the initial position of the Raindrop to x and y.
        #     - Set the initial speed to a random integer between 5 and 15.
        #   Use instance variables:   screen  x  y  speed.
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(3, 15)


    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        # TODO 11: Change the  y  position of this Raindrop by its speed.
        self.y = self.y + self.speed


    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        # Note: this will be used for testing, but not used in the final version of the code for the sake of simplicity.
        # TODO 13: Return  True  if the  y  position of this Raindrop is greater than 800.
        if self.y > self.screen.get_height():
            return True
        return False

    def draw(self):
        """ Draws this sprite onto the screen. """
        # TODO 9: Draw a vertical line that is 5 pixels long, 2 pixels thick,
        #      from the current position of this Raindrop (use either a black or blue color).
        pygame.draw.line(self.screen, (0, 0, 150),
                         (self.x, self.y),
                         (self.x, self.y + 5), 2)


class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        # TODO 16: Initialize this Hero, as follows:
        #     - Store the screen.
        #     - Set the initial position of this Hero to x and y.
        #     - Create an image of this Hero WITH    an umbrella to the given with_umbrella_filename.
        #     - Create an image of this Hero WITHOUT an umbrella to the given without_umbrella_filename.
        #     - Set the "last hit time" to 0.
        #   Use instance variables:
        #      screen  x  y  image_umbrella   image_no_umbrella  last_hit_time.
        self.screen = screen
        self.x = x
        self.y = y
        self.image_with_umbrella = pygame.image.load(with_umbrella_filename)
        self.image_without_umbrella = pygame.image.load(without_umbrella_filename)
        self.last_hit_time = 0


    def draw(self):
        """ Draws this sprite onto the screen. """
        # TODO 17: Draw (blit) this Hero, at this Hero's position, WITHOUT an umbrella:
        # TODO 21: Instead draw (blit) this Hero, at this Hero's position, as follows:
        #     If the current time is greater than this Hero's last_hit_time + 1,
        #       draw this Hero WITHOUT an umbrella,
        #       otherwise draw this Hero WITH an umbrella.
        current_image = self.image_without_umbrella

        if time.time() - self.last_hit_time < 1.0:
            current_image = self.image_with_umbrella

        self.screen.blit(current_image, (self.x, self.y))


        pass

    def hit_by(self, raindrop):
        """ Returns true if the given raindrop is hitting this Hero, otherwise false. """
        # TODO 19: Return True if this Hero is currently colliding with the given Raindrop.
        hero_hit_box = pygame.Rect(self.x, self.y, 170, 192)
        return hero_hit_box.collidepoint((raindrop.x, raindrop.y))


class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        # TODO 24: Initialize this Cloud, as follows:
        #     - Store the screen.
        #     - Set the initial position of this Cloud to x and y.
        #     - Set the image of this Cloud to the given image filename.
        #     - Create a list for Raindrop objects as an empty list called raindrops.
        #   Use instance variables:
        #      screen  x  y  image   raindrops.
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)
        self.raindrops = []

    def draw(self):
        """ Draws this sprite onto the screen. """
        # TODO 25: Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """
        # TODO 28: Append a new Raindrop to this Cloud's list of raindrops,
        #     where the new Raindrop starts at:
        #       - x is a random integer between this Cloud's x and this Cloud's x + 300.
        #       - y is this Cloud's y + 100.

        new_raindrop = Raindrop(self.screen,
                                random.randint(self.x, self.x + self.image.get_width()),
                                self.y + self.image.get_height() - 8)
        self.raindrops.append(new_raindrop)
        print(len(self.raindrops))


def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    # TODO 1: Initialize the game, display a caption, and set   screen   to a 1000x600 Screen.
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Mike's Rainy Day")
    # TODO 2: Make a Clock
    clock = pygame.time.Clock()
    # TODO 7: As a temporary test, make a new Raindrop called test_drop at x=320 y=10
    # test_raindrop = Raindrop(screen, 720, 10)
    # TODO 15: Make a Hero, named mike, with appropriate images, starting at position x=200 y=400.
    mike = Hero(screen, 300, 400, "Mike_umbrella.png", "Mike.png")
    # TODO 15: Make a Hero, named alyssa, with appropriate images, starting at position x=700 y=400.
    alyssa = Hero(screen, 700, 400, "Alyssa_umbrella.png", "Alyssa.png")
    # TODO 23: Make a Cloud, named cloud, with appropriate images, starting at position x=300 y=50.
    cloud = Cloud(screen, 300, 50, "cloud.png")

    # TODO 3: Enter the game loop, with a clock tick of 60 (or so) at each iteration.
    while True:
        clock.tick(60)
        # TODO 4:   Make the pygame.QUIT event stop the game.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            cloud.x = cloud.x - 5
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x = cloud.x + 5
        if pressed_keys[pygame.K_UP]:
            cloud.y = cloud.y - 5
        if pressed_keys[pygame.K_DOWN]:
            cloud.y = cloud.y + 5

        # TODO 27: Inside the game loop (AFTER the events loop above), get the list of keys that are currently pressed.
        #     Arrange so that the Cloud moves:
        #       5 pixels (or 10 pixels) to the right if the Right Arrow key (pygame.K_RIGHT) is pressed.
        #       5 pixels (or 10 pixels) to the left  if the Left  Arrow key (pygame.K_LEFT)  is pressed.
        #       5 pixels (or 10 pixels) up           if the Up    Arrow key (pygame.K_UP)    is pressed.
        #       5 pixels (or 10 pixels) down         if the Down  Arrow key (pygame.K_DOWN)  is pressed.
        # DISCUSS: If you want something to happen once per key press, put it in the events loop above
        #          If you want something to continually happen while holding the key, put it after the events loop.



        # TODO 5: Inside the game loop, draw the screen (fill with white)
        screen.fill((255, 255, 255))

        # --- begin area of test_drop code that will be removed later
        # TODO 12: As a temporary test, move test_drop
        # test_raindrop.move()
        # # TODO 14: As a temporary test, check if test_drop is off screen, if so reset the y position to 10
        # if test_raindrop.off_screen():
        #     test_raindrop.y = 10
        #
        # # TODO 10: As a temporary test, draw test_drop
        # test_raindrop.draw()

        # TODO 20: As a temporary test, check if test_drop is hitting Mike (or Alyssa), if so set their last_hit_time


        # TODO 22: Remove the code that reset the y of the test_drop when off_screen()
        #          Instead reset the test_drop y to 10 when mike is hit, additionally set the x to 750
        #          Then add similar code to alyssa that sets her last_hit_time and moves the test_drop to 10 320
        # --- end area of test_drop code that will be removed later

        # TODO 26: Draw the Cloud.
        cloud.draw()
        # TODO 29: Remove the temporary testdrop code from this function and refactor it as follows:
        cloud.rain()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)

            if alyssa.hit_by(raindrop):
                alyssa.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)

            if raindrop.off_screen():
                cloud.raindrops.remove(raindrop)

        # TODO: Make the Cloud "rain", then:
        # TODO    For each Raindrop in the Cloud's list of raindrops:
            #       - move the Raindrop.
            #       - draw the Raindrop.
            # TODO  30: if the Hero (Mike or Alyssa) is hit by a Raindrop, set the Hero's last_time_hit to the current time.
            # Optional  - if the Raindrop is off the screen or hitting a Hero, remove it from the Cloud's list of raindrops.

        # TODO 18: Draw the Heroes (Mike and Alyssa)
        mike.draw()
        alyssa.draw()

        # TODO 6: Update the display and remove the pass statement below
        pygame.display.update()



# TODO 0: Call main.
main()