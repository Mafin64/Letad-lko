import pygame
import random

# Připravíme PyGame
pygame.init()
pygame.display.set_caption("   Letadýlková Game")
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# Připravíme si obrázek
background = (200, 200, 200)
auto = pygame.image.load("auto.png")
auto = pygame.transform.scale(auto, (40, 40))
df = pygame.image.load("df.png")
df = pygame.transform.scale(df, (40, 40))

WIDTH = 8
HEIGHT = 6

auto_x = 2
auto_y = 1

def game_to_screen(x, y):
    return (x * 45 + 10, y * 45 + 10)

def move_auto(nx, ny):
    global auto_x, auto_y

    duration = 2000
    t = 0
    # Obrazovkove souradnice
    sx, sy = game_to_screen(auto_x, auto_y)
    ex, ey = game_to_screen(nx, ny)
    while t < duration:
        new = t / duration  # 0...1
        old = 1 - new
        x = old * sx + new * ex
        y = old * sy + new * ey
        draw_scene()
        screen.blit(rotated_auto, (x, y))
        pygame.display.update()
        t = t + clock.tick()

    auto_x = nx
    auto_y = ny
    check_dfs()

    

pa_x = 0
pa_y = 0
dfs = [(0, 0), (5, 1), (0, 2)]
score = 0

def draw_scene():
    screen.fill(background)
    for x in range(WIDTH):
        for y in range(HEIGHT):                    
            color = (255, 255, 255)
            rect = (game_to_screen(x, y), (40, 40))
            pygame.draw.rect(screen, color, rect)
    for pa in dfs:
        pa_x, pa_y = pa
        screen.blit(df, game_to_screen(pa_x, pa_y))
    font = pygame.font.Font(None, 42)
    text = font.render(f"Score: {score}", True, (0, 0, 0), (255, 255, 0))
    screen.blit(text, (20, 300))

def check_dfs():
    global dfs
    global score
    new = []
    for pa in dfs:
        if pa == (auto_x, auto_y):
            score = score + 1
        else:
            new.append(pa)
    dfs = new

countdown = 5
rotated_auto = pygame.transform.rotate(auto, 0)
while True:
    # Vykreslíme
    draw_scene()
    screen.blit(rotated_auto, game_to_screen(auto_x, auto_y))
    pygame.display.update()

    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
            rotated_auto = pygame.transform.rotate(auto, 270)
            if auto_x < WIDTH - 1:
                move_auto(auto_x + 1, auto_y)
        elif event.key == pygame.K_w:
            rotated_auto = pygame.transform.rotate(auto, 0)
            if auto_y > 0:
                move_auto(auto_x, auto_y - 1)
        elif event.key == pygame.K_a:
            rotated_auto = pygame.transform.rotate(auto, 90)
            if auto_x > 0:
                move_auto(auto_x - 1, auto_y)
        elif event.key == pygame.K_s:
            rotated_auto = pygame.transform.rotate(auto, 180)
            if auto_y < HEIGHT - 1:
                move_auto(auto_x, auto_y + 1)

    if (auto_x, auto_y) == (pa_x, pa_y):
        pa_x = random.randrange(0, WIDTH)
        pa_y = random.randrange(0, HEIGHT)