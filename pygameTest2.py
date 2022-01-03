import  pygame
import  random
Whidth = 620
height = 480

FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

x = Whidth / 2
y = height / 2

isJump = False
JumpCount = 8


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
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 1:
        x -= 5
    if keys[pygame.K_RIGHT] and x < 619 - 50 - 1:
        x += 5
    if not (isJump):
        if keys[pygame.K_UP] and y > 1:
            y -= 5
        if keys[pygame.K_DOWN] and y < 479  -50 - 1 :
            y += 5
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if JumpCount >= -8:
            if JumpCount < 0:
                y += (JumpCount ** 2) / 2
            else:
                y -= (JumpCount ** 2) / 2
            JumpCount -= 1
        else :
            isJump = False
            JumpCount = 8

    screen.fill(BLACK)
    pygame.display.update()
    pygame.draw.rect(screen,(GREEN),(x,y,50,50))
    # all_sprite.draw(screen)
    pygame.display.flip()
    # x += 5
    # y += 5

pygame.quit()
