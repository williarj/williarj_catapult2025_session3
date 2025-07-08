import pygame
import sys

class Missile:
    def __init__(self, screen, x):
        # Store the data.  Initialize:   y to 591   and   has_exploded to False.
        # Note: the 591 comes from the screen height (650) minus the ship image height (59).  Best practice would be to
        #   pass in that value in case the ship image or screen height changes, but simplified here to always be 591.
        pass

    def move(self):
        # Make self.y 5 smaller than it was (which will cause the Missile to move UP).
        # Note: you could've instead passed in a speed when you made a Missle, but all missles in the game are the same
        #   speed, so just using a hardcoded 5 is fine.
        pass

    def draw(self):
        # Draw a vertical red (or green) line on the screen for the missile, 8 pixels long,  4 pixels thick
        #   where the line starts at the current position of this Missile.
        pass

    def is_off_screen(self):
        # Return true if the y value of the missle is less than 0 (or -8 depending how how you draw) i.e. off the screen
        pass


class Fighter:
    def __init__(self, screen):
        # Store the screen to an instance variable.
        # Load the file  "fighter.png"  as the image
        # Set the x instance variable as the screen width / 2 - image width / 2
        # Set the y instance variable as the screen height - image height
        # Already done   self.missiles   to the empty list. 
        # Set the colorkey to white (it has a white background that needs removed) using the method set_colorkey
        self.missiles = []

    def move(self, move_amount_x):
        # Move this Fighter by the move_amount_x
        #   Limit the range from -self.image.get_width() / 2 to
        #                        self.screen.get_width() - self.image.get_width() / 2
        pass

    def draw(self):
        # Draw this Fighter, using its image at its current (x, y) position.
        pass

    def fire(self):
        # Construct a new Missile self.image.get_width() / 2 pixels to the right of this Fighter's x position.
        # Append that Missile to this Fighter's list of Missile objects.
        pass

    def remove_exploded_missiles(self):
        # Already complete
        for k in range(len(self.missiles) - 1, -1, -1):
            if self.missiles[k].has_exploded or self.missiles[k].y < -8:
                del self.missiles[k]


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Testing the Fighter and Missiles only")
    screen = pygame.display.set_mode((640, 650))

    fighter = Fighter(screen)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            # Doing something once when a key is PRESSED
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_SPACE]:
                    fighter.fire()
            if event.type == pygame.QUIT:
                sys.exit()

        # Doing something continually when a key is HELD DOWN
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            fighter.move(-5)
        if pressed_keys[pygame.K_RIGHT]:
            fighter.move(5)

        screen.fill((0, 0, 0))
        fighter.draw()
        for missile in fighter.missiles:
            missile.move()
            missile.draw()
        fighter.remove_exploded_missiles()
        pygame.display.update()


# Testing the classes
if __name__ == "__main__":
    main()
