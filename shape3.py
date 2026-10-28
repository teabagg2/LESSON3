import pygame


def main():
    pygame.init()

    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Moving Sprite with Color Change on Wall Collision")

    colors = {
        'white': pygame.Color('white'),
        'blue': pygame.Color('blue'),
        'yellow': pygame.Color('yellow'),
        'red': pygame.Color('red'),
        'green': pygame.Color('green')
    }

    current_color = colors['white']
    x, y = 30, 30
    sprite_width, sprite_height = 60, 60

    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= 5
        if keys[pygame.K_RIGHT]:
            x += 5
        if keys[pygame.K_UP]:
            y -= 5
        if keys[pygame.K_DOWN]:
            y += 5

        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)

        if x == 0:
            current_color = colors['blue']
        elif x == screen_width - sprite_width:
            current_color = colors['yellow']
        elif y == 0:
            current_color = colors['red']
        elif y == screen_height - sprite_height:
            current_color = colors['green']
        else:
            current_color = colors['white']

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color, (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(90)

    pygame.quit()


if __name__ == "__main__":
    main()