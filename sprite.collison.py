from pathlib import Path
import random

import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVE_SPEED = 5
FONT_SIZE = 72


class Sprite(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(colour)
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(0, min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height))


def create_background():
    background_path = Path(__file__).resolve().parent / "background.jpg"
    if background_path.exists():
        return pygame.transform.scale(
            pygame.image.load(str(background_path)).convert(),
            (SCREEN_WIDTH, SCREEN_HEIGHT),
        )

    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background.fill(pygame.Color("skyblue"))
    pygame.draw.rect(
        background,
        pygame.Color("lightgreen"),
        (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50),
    )
    return background


def game_loop():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sprite Collision Example")
    background_image = create_background()
    font = pygame.font.SysFont("times new roman", FONT_SIZE)

    all_sprites = pygame.sprite.Group()
    sprite1 = Sprite(pygame.Color("dodgerblue"), 30, 30)
    sprite2 = Sprite(pygame.Color("red"), 30, 30)

    for sprite in (sprite1, sprite2):
        sprite.rect.x = random.randint(0, SCREEN_WIDTH - sprite.rect.width)
        sprite.rect.y = random.randint(0, SCREEN_HEIGHT - sprite.rect.height)
        all_sprites.add(sprite)

    running, won = True, False
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_x
            ):
                running = False

        if not won:
            keys = pygame.key.get_pressed()
            x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVE_SPEED
            y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVE_SPEED
            sprite1.move(x_change, y_change)

            if sprite1.rect.colliderect(sprite2.rect):
                all_sprites.remove(sprite2)
                won = True

        screen.blit(background_image, (0, 0))
        all_sprites.draw(screen)
        if won:
            win_text = font.render("You Win!", True, pygame.Color("black"))
            text_rect = win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(win_text, text_rect)

        pygame.display.flip()
        clock.tick(90)

    pygame.quit()


if __name__ == "__main__":
    game_loop()
