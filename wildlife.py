
import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wildlife Information Display")

background = pygame.image.load(r"C:\Users\Eh.iits.just.Meh\Downloads\LESSON3\background.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

tiger = pygame.image.load(r"C:\Users\Eh.iits.just.Meh\Downloads\LESSON3\tiger.jpg")
tiger = pygame.transform.scale(tiger, (250, 200))

tiger_rect = tiger.get_rect(center=(250, 270))

heading_font = pygame.font.Font(None, 36)
fact_font = pygame.font.Font(None, 24)

heading = heading_font.render("WILDLIFE INFORMATION", True, (255, 255, 255))
fact = fact_font.render("Tigers are excellent swimmers!", True, (255, 255, 255))

heading_rect = heading.get_rect(center=(250, 40))
fact_rect = fact.get_rect(center=(250, 465))

clock = pygame.time.Clock()


def game_loop():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))
        screen.blit(tiger, tiger_rect)
        screen.blit(heading, heading_rect)
        screen.blit(fact, fact_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


game_loop()
