import pygame
pygame.init()

BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
LIGHT_BLUE = (200,255,255)
GREEN = (0,255,0)

window_width = 1200
window_height = 750
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Лабіринт')

background = pygame.transform.scale(pygame.image.load('bottom_of_sea_background2.jpeg'), (1200, 750))

clock = pygame.time.Clock()
FPS = 60

pygame.mixer.music.load('Pirates of the Caribbean - Hes a Pirate.mp3')
pygame.mixer_music.play()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_size_x, player_size_y, player_speed):
        super().__init__()

        self.size_x = player_size_x
        self.size_y = player_size_y

        self.image = pygame.transform.scale(pygame.image.load(player_image), (self.size_x, self.size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > -10:
            self.rect.x -= self.speed
        if keys[pygame.K_LEFT] and self.rect.x > -10:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x < 1155:
            self.rect.x += self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < 1155:
            self.rect.x += self.speed
        if keys[pygame.K_w] and self.rect.y > -5:
            self.rect.y -= self.speed
        if keys[pygame.K_UP] and self.rect.y > -5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < 700:
            self.rect.y += self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 700:
            self.rect.y += self.speed
class Wall(pygame.sprite.Sprite):
    def __init__(self, color1, color2, color3, width, height, wall_x, wall_y):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = width
        self.height = height

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((self.color1, self.color2, self.color3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Enemy(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_size_x, player_size_y, player_speed, way):
        super().__init__()

        self.size_x = player_size_x
        self.size_y = player_size_y

        self.image = pygame.transform.scale(pygame.image.load(player_image), (self.size_x, self.size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

        self.way = way
    def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))
    def move(self):
        if pygame.sprite.collide_rect(monster, wall_v1):
            self.way = 'right'
        if pygame.sprite.collide_rect(monster, wall_main_right):
            self.way = 'left'

        if self.way == 'right':
            self.rect.x += player.speed
        if self.way == 'left':
            self.rect.x -= player.speed

player = Player('gleb.png', 415, 190, 50, 50, 1)
monster = Enemy('enemy.png', 465, 410, 100, 83, 2, 'right')
chest = GameSprite('treasure_chest.png', 480, 510, 50, 50, 0)

wall_main_left = Wall(255,0,0,10,400,385,175)
wall_main_up = Wall(255,0,0,410,10,395,175)
wall_main_right = Wall(255,0,0,10,400,805,175)
wall_main_down = Wall(255,0,0,410,10,395,565)
wall_h1 = Wall(255,0,0,100,10,395,245)
wall_h2 = Wall(255,0,0,100,10,565,245)
wall_h3 = Wall(255,0,0,200,10,395,315)
wall_h4 = Wall(255,0,0,200,10,465,385)
wall_v1 = Wall(255,0,0,10,180,465,395)
wall_v2 = Wall(255,0,0,10,150,665,245)
wall_v3 = Wall(255,0,0,10,220,735,175)

def win():
    win = pygame.font.Font(None,70).render('You won!', True, (0,255,0))
    window.blit(win, (500,375))

game = True
updating = True
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False


    window.blit(background, (0, 0))

    pygame.draw.rect(window, (100,0,255), (415,190,50,50))

    wall_main_left.draw()
    wall_main_up.draw()
    wall_main_right.draw()
    wall_main_down.draw()
    wall_h1.draw()
    wall_h2.draw()
    wall_h3.draw()
    wall_h4.draw()
    wall_v1.draw()
    wall_v2.draw()
    wall_v3.draw()

    player.reset()
    chest.reset()

    if pygame.sprite.collide_rect(player, chest):
        win()
        updating = False

    if updating:
        player.move()
        monster.reset()
        monster.move()

        if pygame.sprite.collide_rect(player, wall_main_left) or pygame.sprite.collide_rect(player, wall_main_up) or pygame.sprite.collide_rect(player, wall_main_right) or pygame.sprite.collide_rect(player, wall_main_down) or pygame.sprite.collide_rect(player, wall_h1) or pygame.sprite.collide_rect(player, wall_h2) or pygame.sprite.collide_rect(player, wall_h3) or pygame.sprite.collide_rect(player, wall_h4) or pygame.sprite.collide_rect(player, wall_v1) or pygame.sprite.collide_rect(player, wall_v2) or pygame.sprite.collide_rect(player, wall_v3) or pygame.sprite.collide_rect(player, monster):                                                            
            player.rect.x = 415
            player.rect.y = 190

    pygame.display.update()
    clock.tick(FPS)