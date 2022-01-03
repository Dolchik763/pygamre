import  pygame
import  random
Whidth = 640
height = 420

FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (Whidth / 2 , height / 2)

pygame.init()
screen = pygame.display.set_mode((Whidth,height))
pygame.display.set_caption("Test")
Clock = pygame.time.Clock()
all_sprite = pygame.sprite.Group
player = Player()
all_sprite.add(player)



running = True
while running:
    Clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprite.update()



    screen.fill(BLACK)
    all_sprite.draw(screen)

    pygame.display.flip()


pygame.quit()
