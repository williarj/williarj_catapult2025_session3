import pygame, sys


class Missile:
    def __init__(self, screen, x):
        self.screen = screen
        self.x = x
        self.y = 591  # Hardcoded to keep it simple.
        self.has_exploded = False

    def move(self):
        self.y = self.y - 5

    def draw(self):
        pygame.draw.line(self.screen, (0, 255, 0), (self.x, self.y), (self.x, self.y + 8), 4)


class Fighter:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("images/fighter.png")
        self.image.set_colorkey((255, 255, 255))  # Make the white background transparent
        self.x = self.screen.get_width() / 2 - self.image.get_width() / 2
        self.y = self.screen.get_height() - self.image.get_height()
        self.missiles = []
        self.fire_sound = pygame.mixer.Sound("sounds/pew.wav")

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self, move_amount_x):
        self.x += move_amount_x
        left_bound = -self.image.get_width() / 2
        right_bound = self.screen.get_width() - self.image.get_width() / 2
        if self.x < left_bound:
            self.x = left_bound
        if self.x > right_bound:
            self.x = right_bound

    def fire(self):
        self.missiles.append(Missile(self.screen, self.x + self.image.get_width() / 2))
        self.fire_sound.play()

    def remove_exploded_missiles(self):
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
