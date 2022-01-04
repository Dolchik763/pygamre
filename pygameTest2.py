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

s_x = 100
s_y = 100
end_x = 200
end_y = 200
x = Whidth / 2
y = height / 2

isJump = False
JumpCount = 10


WalkRight =[pygame.image.load("pygame_left_1.png"),
            pygame.image.load("pygame_left_2.png"),
            pygame.image.load("pygame_left_3.png"),
            pygame.image.load("pygame_left_4.png"),
            pygame.image.load("pygame_left_5.png"),
            pygame.image.load("pygame_left_6.png")]

WalkLeft = [pygame.image.load("pygame_right_1.png"),
            pygame.image.load("pygame_right_2.png"),
            pygame.image.load("pygame_right_3.png"),
            pygame.image.load("pygame_right_4.png"),
            pygame.image.load("pygame_right_5.png"),
            pygame.image.load("pygame_right_6.png"),]


left = False
right = False
animCount = 0
PlayerStand = [pygame.image.load("pygame_idle.png")]
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

def DarwWindow():
    global animCount
    screen.fill(BLACK)
    if animCount + 1 > 30:
        animCount = 0
    if left :
        screen.blit(WalkLeft[animCount // 5], (x,y))
        animCount += 1
    elif right:
        screen.blit(WalkRight[animCount // 5], (x,y))
        animCount += 1
    else:
        screen.blit(PlayerStand,(x,y))
    pygame.display.flip()


running = True
while running:
    Clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 1:
        x -= 5
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 619 - 50 - 1:
        x += 5
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    if not (isJump):
        # if keys[pygame.K_UP] and y > 1:
        #     y -= 5
        # if keys[pygame.K_DOWN] and y < 479  -50 - 1 :
        #     y += 5
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if JumpCount >= -10:
            if JumpCount < 0:
                y += (JumpCount ** 2) / 2
            else:
                y -= (JumpCount ** 2) / 2
            JumpCount -= 1
        else :
            isJump = False
            JumpCount = 10
    if keys[pygame.K_a]:
        s_x -= 10
        # s_y += 10
        end_x += 10
        # end_y -= 10

    pygame.display.update()
    DarwWindow()
    # all_sprite.draw(screen)
    # pygame.draw.line(screen, (RED), (s_x,s_y), (end_x,end_y))

    # x += 5
    # y += 5
pygame.quit()
