import pygame
import sys
import space_invaders
import button_module

def main():
    pygame.init()
    pygame.display.set_caption("Space Invaders")
    screen = pygame.display.set_mode((640, 650))

    pygame.mixer.Sound("sounds/win.wav").play()

    fighter_image = pygame.image.load("images/fighter.png").convert()
    fighter_image.set_colorkey((255, 255, 255))

    badguy_image = pygame.image.load("images/badguy.png")

    play_button = button_module.TextButton(screen, screen.get_width() / 2, 250, "Click here to play")

    instructions_font = pygame.font.Font("fonts/COMIC.TTF", 24)
    instruction_caption1 = instructions_font.render("Use the left and right arrows to move", True,
                                                    pygame.Color("White"))
    instruction_caption2 = instructions_font.render("and the spacebar to fire.  Good luck!", True, pygame.Color("White"))


    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if play_button.is_clicked_by(event.pos):
                    print("You clicked the play button.")
                    space_invaders.main_game_loop(screen)
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((0, 0, 0))

        x = None  # Just a trick so that x exists after the loop.
        for k in range(5):
            x = screen.get_width() / 2 + k * 5
            y = screen.get_height() - 300 + k * 50
            pygame.draw.line(screen, (0, 255, 0), (x, y), (x, y + 8), 4)
        screen.blit(fighter_image, (x - fighter_image.get_width() / 2 + 5, screen.get_height() - fighter_image.get_height()))

        screen.blit(badguy_image, (screen.get_width() / 2 - 100, 100))
        play_button.draw()

        screen.blit(instruction_caption1, (30, 12))
        screen.blit(instruction_caption2, (30, 40))

        pygame.display.update()


main()
