import pygame
import sys
import fighter_missile_module
import enemy_fleet_module
import game_over_module


class Scoreboard:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        as_image = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(as_image, (5, 5))


def main():
    pygame.init()
    pygame.display.set_caption("Space Invaders")
    screen = pygame.display.set_mode((640, 650))
    main_game_loop(screen)


def main_game_loop(screen):
    allow_supergun = False

    INITIAL_NUM_ROWS = 4
    enemy_rows = INITIAL_NUM_ROWS
    enemy_fleet = enemy_fleet_module.EnemyFleet(screen, enemy_rows)
    fighter = fighter_missile_module.Fighter(screen)

    # DONE: Create a Scoreboard, called scoreboard, using the screen at location 5, 5
    scoreboard = Scoreboard(screen)
    win_sound = pygame.mixer.Sound("sounds/win.wav")

    clock = pygame.time.Clock()
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

        # Optional
        if allow_supergun and pressed_keys[pygame.K_SPACE]:
            fighter.fire()

        screen.fill((0, 0, 0))

        scoreboard.draw()

        enemy_fleet.move()
        enemy_fleet.draw()

        fighter.draw()
        for missile in fighter.missiles:
            missile.move()
            missile.draw()

        for badguy in enemy_fleet.badguys:
            for missile in fighter.missiles:
                if badguy.hit_by(missile):
                    # DONE: Increment the score of the scoreboard by 100
                    scoreboard.score = scoreboard.score + 100
                    badguy.is_dead = True
                    missile.has_exploded = True

        fighter.remove_exploded_missiles()
        enemy_fleet.remove_dead_badguys()

        if enemy_fleet.is_defeated:
            win_sound.play()
            enemy_rows = enemy_rows + 1
            enemy_fleet = enemy_fleet_module.EnemyFleet(screen, enemy_rows)

        # Check for your death!
        for badguy in enemy_fleet.badguys:
            if badguy.y + badguy.image.get_height() >= fighter.y:
                game_over_module.run_game_over_loop(screen)
                # Note: that function is a new screen.  Code here runs when that screen closes.
                # Reset necessary variables to play again.
                scoreboard.score = 0
                fighter.missiles.clear()
                enemy_fleet.badguys.clear()
                enemy_rows = INITIAL_NUM_ROWS
                enemy_fleet = enemy_fleet_module.EnemyFleet(screen, enemy_rows)

        pygame.display.update()


if __name__ == "__main__":
    main()
