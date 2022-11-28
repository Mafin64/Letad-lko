import pygame

# Připravíme PyGame
pygame.init()
pygame.display.set_caption("..Letadýlko")
size = (300, 200)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Připravíme si obrázek
background = (150, 150, 150)
auto = pygame.image.load("auto.png")
auto = pygame.transform.scale(auto, (40, 40))
rotated_auto = pygame.transform.rotate(auto, 0)

WIDTH = 6
HEIGHT = 4

zx = 0
zy = 0


def game_to_screen(x, y):
    return (x * 51, y * 51)


def animate(nx, ny):
    global zx, zy

    duration = 2000

    t = 0
    #Obrázkové souradnice
    sx, sy = game_to_screen(zx, zy)
    ex, ey = game_to_screen(nx, ny)
    while t < duration:
        new = t / duration  #0...1
        old = 1 - new
        x = old * sx + new * ex
        y = old * sy + new * ey
        screen.fill(background)
        draw_grid()
        screen.blit(rotated_auto, (x, y))
        pygame.display.update()
        t = t + clock.tick()

    zx = nx
    zy = ny


def draw_grid():
    for x in range(WIDTH):
        for y in range(HEIGHT):
            color = (255, 255, 255)
            rect = (game_to_screen(x, y), (40, 40))
            pygame.draw.rect(screen, color, rect)


while True:
    # Vykreslíme
    screen.fill(background)
    draw_grid()
    screen.blit(rotated_auto, game_to_screen(zx, zy))

    pygame.display.update()

    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
            rotated_auto = pygame.transform.rotate(auto, 270)
            if zx < WIDTH - 1:
                animate(zx + 1, zy)
        elif event.key == pygame.K_w:
            rotated_auto = pygame.transform.rotate(auto, 0)
            if zy > 0:
                animate(zx, zy - 1)
        elif event.key == pygame.K_s:
            rotated_auto = pygame.transform.rotate(auto, 180)
            if zy < HEIGHT - 1:
                animate(zx, zy + 1)
        elif event.key == pygame.K_a:
            rotated_auto = pygame.transform.rotate(auto, 90)
            if zx > 0:
                animate(zx - 1, zy)
