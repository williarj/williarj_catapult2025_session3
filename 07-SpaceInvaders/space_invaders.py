import pygame
import sys

# TODO: when need import the fighter_missile_module
# TODO: when need import the enemy_fleet_module


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("SPACE INVADERS!")
    screen = pygame.display.set_mode((640, 650))

    # TODO 9: Set    enemy_rows    to an initial value of 3.
    # TODO 10: Create an EnemyFleet object (called enemy_fleet) with the screen and enemy_rows
    # TODO 1: Create a Fighter (called fighter)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            # TODO 5: If the event type is KEYDOWN and pressed_keys[pygame.K_SPACE] is True, then fire a missile
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))
        # TODO 3: If pygame.K_LEFT is pressed and move the fighter left 5 (i.e. -5)
        # TODO 4: If pygame.K_RIGHT is pressed and move the fighter right 5
        # TODO 2: Draw the fighter

        # TODO 11: Move the enemy_fleet
        # TODO 12: Draw the enemy_fleet

        # TODO 6: For each missile in the fighter missiles
        #   TODO 7: Move the missile
        #   TODO 8: Draw the missile

        # TODO 12: For each badguy in the enemy_fleet.badguys list
        #     TODO 13: For each missile in the fighter missiles
        #         TODO 14: If the badguy is hit by the missile
        #             TODO 15: Mark the badguy is_dead = True
        #             TODO 16: Mark the missile has_exploded = True

        # Optional TODOs (technically this is already done within fighter.remove_exploded_missiles)
        # TODO 16.5: For each missile in the fighter missiles
        #     TODO 16.5: If the missle is off the screen
        #         TODO 16.5: Mark the missile has_exploded = True (cleaning up off screen stuff)

        # TODO 17: Use the fighter to remove exploded missiles
        # TODO 18: Use the enemy_fleet to remove dead badguys

        # TODO 19: If the enemy is_defeated
        #     TODO 20: Increment the enemy_rows
        #     TODO 21: Create a new enemy_fleet with the screen and enemy_rows

        # TODO 22: Check for your death.  Figure out what needs to happen.
        # Hints: Check if a Badguy gets a y value greater than 545
        #    Note: 545 is screen.get_height() -
        #    If that happens set a variable (game_over) as appropriate
        #    If the game is over, show the gameover.png image at (170, 200)

        # TODO 23: Create a Scoreboard class (from scratch)
        # Hints: Instance variables: screen, score, and font (size 30)
        #    Methods: draw (and __init__)
        # Create a scoreboard and draw it at location 5, 5
        # When a Badguy is killed add 100 points to the scoreboard.score

        # TODO 24: Optional extra - Add sound effects!

        pygame.display.update()


main()
