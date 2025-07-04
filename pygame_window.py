
import pygame

WINDOW_SIZE = (500, 500)
BG_COLOR     = (58, 58, 58)        
IMAGE_SIZE   = (300, 300)          
IMAGE_FILE   = "C:/Users/aayus/OneDrive/Desktop/Coding with Codlingal/.idea/Pygame/enemy.jpg"    
CAPTION      = "My first game screen"


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(CAPTION)

    
    image = pygame.image.load(IMAGE_FILE).convert_alpha()
    image = pygame.transform.smoothscale(image, IMAGE_SIZE)
    image_rect = image.get_rect(center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)         
        screen.blit(image, image_rect)  
        pygame.display.flip()         
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
