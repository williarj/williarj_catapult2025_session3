import pygame
import sys


class Badguy:
    def __init__(self, screen, x, y, speed):
        self.is_dead = False
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = speed * 1.5
        self.image = pygame.image.load("images/badguy.png")
        self.original_x = x

    def move(self):
        self.x = self.x + self.speed
        if abs(self.x - self.original_x) > 100:
            self.speed = -self.speed
            self.y = self.y + 4 * abs(self.speed)

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, missile):
        badguy_hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        return badguy_hitbox.collidepoint(missile.x, missile.y)


class EnemyFleet:
    def __init__(self, screen, enemy_rows):
        self.badguys = []
        self.explosion_sound = pygame.mixer.Sound("sounds/explosion.wav")
        for j in range(enemy_rows):
            for k in range(8):
                self.badguys.append(Badguy(screen, 80 * k, 50 * j + 20, enemy_rows))

    @property
    def is_defeated(self):
        return len(self.badguys) == 0

    def move(self):
        for badguy in self.badguys:
            badguy.move()

    def draw(self):
        for badguy in self.badguys:
            badguy.draw()

    def remove_dead_badguys(self):
        for k in range(len(self.badguys) - 1, -1, -1):
            if self.badguys[k].is_dead:
                del self.badguys[k]
                self.explosion_sound.play()


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Testing the Enemy Fleet and Badguys only")
    screen = pygame.display.set_mode((640, 650))

    enemy_rows = 4
    enemy_fleet = EnemyFleet(screen, enemy_rows)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))
        enemy_fleet.draw()
        enemy_fleet.move()

        enemy_fleet.remove_dead_badguys()
        pygame.display.update()


# Testing the classes
if __name__ == "__main__":
    main()
