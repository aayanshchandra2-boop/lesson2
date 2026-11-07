import math
import random
import pygame

screen_width = 800
screen_height = 600
player_start_x = 370
player_start_y = 480
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 2
enemy_speed_y = 30
bullet_speed_y = 10
collision_distance = 27

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invader")

background = pygame.Surface((screen_width, screen_height))
background.fill((10, 20, 40))
for y in range(0, screen_height, 40):
    pygame.draw.rect(background, (18, 28, 52), (0, y, screen_width, 20))

# Simple generated game art so the window works without external files.
def make_player_surface():
    surf = pygame.Surface((52, 28), pygame.SRCALPHA)
    pygame.draw.polygon(surf, (65, 200, 255), [(26, 0), (52, 24), (38, 24), (38, 28), (14, 28), (14, 24), (0, 24)])
    pygame.draw.rect(surf, (255, 255, 255), (20, 10, 12, 8))
    return surf


def make_enemy_surface():
    surf = pygame.Surface((40, 28), pygame.SRCALPHA)
    pygame.draw.ellipse(surf, (255, 90, 90), (4, 6, 32, 18))
    pygame.draw.rect(surf, (220, 220, 220), (14, 0, 12, 8))
    pygame.draw.polygon(surf, (255, 255, 255), [(8, 20), (12, 24), (28, 24), (32, 20)])
    return surf


def make_bullet_surface():
    surf = pygame.Surface((8, 18), pygame.SRCALPHA)
    pygame.draw.rect(surf, (255, 255, 100), (2, 0, 4, 18))
    return surf


player_img = make_player_surface()
icon = pygame.transform.smoothscale(player_img, (32, 32))
pygame.display.set_icon(icon)

enemy_img = make_enemy_surface()
bullet_img = make_bullet_surface()

player_x = player_start_x
player_y = player_start_y
player_x_change = 0

enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6
for _ in range(num_of_enemies):
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(enemy_start_y_min, enemy_start_y_max))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)

bullet_x = 0
bullet_y = player_y
bullet_state = "ready"

score_value = 0
font = pygame.font.Font(None, 32)
over_font = pygame.font.Font(None, 64)
text_x = 10
text_y = 10


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def draw_player(x, y):
    screen.blit(player_img, (x, y))


def draw_enemy(x, y, index):
    screen.blit(enemy_img, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


def is_collision(enemy_x_pos, enemy_y_pos, bullet_x_pos, bullet_y_pos):
    distance = math.sqrt(
        (math.pow(enemy_x_pos - bullet_x_pos, 2)) + (math.pow(enemy_y_pos - bullet_y_pos, 2))
    )
    return distance < collision_distance


running = True
game_over = False
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            elif event.key == pygame.K_RIGHT:
                player_x_change = 5
            elif event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x
                bullet_y = player_y
                bullet_state = "fire"
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_x_change = 0

    if not game_over:
        player_x += player_x_change
        if player_x <= 0:
            player_x = 0
        elif player_x >= 736:
            player_x = 736

        if bullet_state == "fire":
            bullet_y -= bullet_speed_y
            if bullet_y <= 0:
                bullet_y = player_y
                bullet_state = "ready"

        for i in range(num_of_enemies):
            enemy_x[i] += enemy_x_change[i]
            if enemy_x[i] <= 0:
                enemy_x_change[i] = enemy_speed_x
                enemy_y[i] += enemy_y_change[i]
            elif enemy_x[i] >= 736:
                enemy_x_change[i] = -enemy_speed_x
                enemy_y[i] += enemy_y_change[i]

            if enemy_y[i] > 440:
                game_over = True
                break

            if bullet_state == "fire" and is_collision(enemy_x[i], enemy_y[i], bullet_x + 16, bullet_y + 10):
                bullet_state = "ready"
                bullet_y = player_y
                score_value += 1
                enemy_x[i] = random.randint(0, 736)
                enemy_y[i] = random.randint(enemy_start_y_min, enemy_start_y_max)

            draw_enemy(enemy_x[i], enemy_y[i], i)

        if bullet_state == "fire":
            screen.blit(bullet_img, (bullet_x + 16, bullet_y + 10))

    draw_player(player_x, player_y)
    show_score(text_x, text_y)
    if game_over:
        game_over_text()
    pygame.display.update()
    pygame.time.delay(20)

pygame.quit()
