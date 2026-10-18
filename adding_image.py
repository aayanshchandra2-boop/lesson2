from pathlib import Path

import pygame

pygame.init()
SCREEN_WIDTH ,SCREEN_HEIGHT = 500,500
display_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Adding Image and background image")
asset_dir = Path(__file__).resolve().parent
background_path = asset_dir / "background.png"
penguin_path = asset_dir / "penguin.png"

if background_path.exists():
    background_image = pygame.transform.scale(
        pygame.image.load(str(background_path)).convert(),
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )
else:
    background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image.fill((112, 190, 220))
    pygame.draw.rect(background_image, (235, 245, 248), (0, 390, SCREEN_WIDTH, 110))

if penguin_path.exists():
    penguin_image = pygame.transform.scale(
        pygame.image.load(str(penguin_path)).convert_alpha(),
        (200, 200)
    )
else:
    penguin_image = pygame.Surface((200, 200), pygame.SRCALPHA)
    pygame.draw.ellipse(penguin_image, (35, 43, 52), (45, 18, 110, 165))
    pygame.draw.ellipse(penguin_image, (245, 245, 238), (67, 65, 66, 105))
    pygame.draw.ellipse(penguin_image, (35, 43, 52), (37, 82, 35, 86))
    pygame.draw.ellipse(penguin_image, (35, 43, 52), (128, 82, 35, 86))
    pygame.draw.circle(penguin_image, (255, 255, 255), (83, 57), 7)
    pygame.draw.circle(penguin_image, (255, 255, 255), (117, 57), 7)
    pygame.draw.circle(penguin_image, (25, 25, 25), (84, 57), 3)
    pygame.draw.circle(penguin_image, (25, 25, 25), (116, 57), 3)
    pygame.draw.polygon(penguin_image, (245, 155, 48), [(92, 69), (108, 69), (100, 82)])
    pygame.draw.ellipse(penguin_image, (245, 155, 48), (58, 168, 42, 18))
    pygame.draw.ellipse(penguin_image, (245, 155, 48), (100, 168, 42, 18))

penguin_rect = penguin_image.get_rect()
penguin_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30)

text = pygame.font.Font(None, 36).render("Penguin", True, (255, 255, 255))
text_rect = text.get_rect()
text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)

def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)

        pygame.display.update()

    pygame.quit()

     
if __name__ == "__main__":
    game_loop()
    
