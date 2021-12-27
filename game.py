import pygame

pygame.init()

screen_width= 1100
screen_length = 600

window = pygame.display.set_mode((screen_width,screen_length))

clock = pygame.time.Clock()

pygame.display.set_caption("Go-Go Ultra Fight Frenzy")

background = pygame.image.load('Graphics/battleback1.png')

character_width = 36
character_height = 48


walkRight = [pygame.transform.scale(pygame.image.load('Graphics/right4.png'), (character_width, character_height)),
             pygame.transform.scale(pygame.image.load('Graphics/right5.png'), (character_width, character_height)),
             pygame.transform.scale(pygame.image.load('Graphics/right6.png'), (character_width, character_height))]

walkLeft  = [pygame.transform.scale(pygame.image.load('Graphics/left4.png'), (character_width, character_height)),
             pygame.transform.scale(pygame.image.load('Graphics/left5.png'), (character_width, character_height)),
             pygame.transform.scale(pygame.image.load('Graphics/left6.png'), (character_width, character_height))]

walkUp =  [pygame.transform.scale(pygame.image.load('Graphics/up1.png'), (character_width, character_height)),
           pygame.transform.scale(pygame.image.load('Graphics/up2.png'), (character_width, character_height)),
           pygame.transform.scale(pygame.image.load('Graphics/up3.png'), (character_width, character_height))]

walkDown = [pygame.transform.scale(pygame.image.load('Graphics/down1.png'), (character_width, character_height)),
            pygame.transform.scale(pygame.image.load('Graphics/down2.png'), (character_width, character_height)),
            pygame.transform.scale(pygame.image.load('Graphics/down3.png'), (character_width, character_height))]

standing = pygame.transform.scale(pygame.image.load('Graphics/Standing.png'), (character_width, character_height))

x = 350 #
y = screen_length - (screen_length/2.5) # default position we want our object to start at

walkUpEnemy =  [pygame.transform.scale(pygame.image.load('Graphics/GoblinDown1.png'), (1.8 * character_width, 1.2 * character_height)),
                pygame.transform.scale(pygame.image.load('Graphics/GoblinDown2.png'), (1.8 * character_width, 1.2 * character_height)),
                pygame.transform.scale(pygame.image.load('Graphics/GoblinDown3.png'), (1.8 * character_width, 1.2 * character_height)),
                pygame.transform.scale(pygame.image.load('Graphics/GoblinDown4.png'), (1.8 * character_width, 1.2 * character_height)),
                pygame.transform.scale(pygame.image.load('Graphics/GoblinDown5.png'), (1.8 * character_width, 1.2 * character_height)),
                pygame.transform.scale(pygame.image.load('Graphics/GoblinDown6.png'), (1.8 * character_width, 1.2 * character_height))]

walkLeftEnemy= [pygame.transform.scale(pygame.image.load('Graphics/tile033.png'), (1.8 * character_width, 1.2 * character_height)),
                pygame.transform.scale(pygame.image.load('Graphics/tile034.png'), (1.8 * character_width, 1.2 * character_height)),
                pygame.transform.scale(pygame.image.load('Graphics/tile035.png'), (1.8 * character_width, 1.2 * character_height)),
                pygame.transform.scale(pygame.image.load('Graphics/tile036.png'), (1.8 * character_width, 1.2 * character_height)),
                pygame.transform.scale(pygame.image.load('Graphics/tile037.png'), (1.8 * character_width, 1.2 * character_height)),
                pygame.transform.scale(pygame.image.load('Graphics/tile038.png'), (1.8 * character_width, 1.2 * character_height))]

walkDownEnemy = [pygame.transform.scale(pygame.image.load('Graphics/Goblinup1.png'), (1.8 * character_width, 1.2 * character_height)),
                 pygame.transform.scale(pygame.image.load('Graphics/Goblinup2.png'), (1.8 * character_width, 1.2 * character_height)),
                 pygame.transform.scale(pygame.image.load('Graphics/Goblinup3.png'), (1.8 * character_width, 1.2 * character_height)),
                 pygame.transform.scale(pygame.image.load('Graphics/Goblinup4.png'), (1.8 * character_width, 1.2 * character_height)),
                 pygame.transform.scale(pygame.image.load('Graphics/Goblinup5.png'), (1.8 * character_width, 1.2 * character_height)),
                 pygame.transform.scale(pygame.image.load('Graphics/Goblinup6.png'), (1.8 * character_width, 1.2 * character_height))]

walkRightEnemy= [pygame.transform.scale(pygame.image.load('Graphics/Goblinright1.png'), (1.8 * character_width, 1.2 * character_height)),
                 pygame.transform.scale(pygame.image.load('Graphics/Goblinright2.png'), (1.8 * character_width, 1.2 * character_height)),
                 pygame.transform.scale(pygame.image.load('Graphics/Goblinright3.png'), (1.8 * character_width, 1.2 * character_height)),
                 pygame.transform.scale(pygame.image.load('Graphics/Goblinright4.png'), (1.8 * character_width, 1.2 * character_height)),
                 pygame.transform.scale(pygame.image.load('Graphics/Goblinright5.png'), (1.8 * character_width, 1.2 * character_height)),
                 pygame.transform.scale(pygame.image.load('Graphics/Goblinright6.png'), (1.8 * character_width, 1.2 * character_height))]

width = character_width
height = character_height # size of object

class user():
    def __init__(self, x,y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.isJump = False
        self.jumpDistance = 7 #
        self.jumpCount = 7 # THESE TWO NUMBERS MUST MATCH UP
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0


    def updateChar(self,window): # Animation

        if(self.walkCount +1 >= 21):
            self.walkCount = 0
        if(self.left):
            window.blit(walkLeft[self.walkCount//7], (self.x,self.y))
            self.walkCount += 1
        elif(self.right):
            window.blit(walkRight[player.walkCount//7], (self.x,self.y))
            self.walkCount += 1
        elif(self.down):
            window.blit(walkDown[self.walkCount//7], (self.x,self.y))
            self.walkCount += 1

        elif(self.up):
            window.blit(walkUp[self.walkCount//7], (self.x,self.y))
            self.walkCount += 1
        else:
            window.blit(standing, (self.x,self.y))


class Enemy:
    def __init__(self, x,y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.maxDistance = 85
        self.directionCount = 0
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.velocity = 1
        self.walkCount = 0

    def updateMonster(self, window):


        if(self.walkCount +1 >= 72):
            self.walkCount = 0

        if(self.left):

            window.blit(walkLeftEnemy[self.walkCount//12], (self.x,self.y))
            self.walkCount += 1
        elif(self.right):

            window.blit(walkRightEnemy[self.walkCount//12], (self.x,self.y))
            self.walkCount += 1

        elif(self.down):
            window.blit(walkDownEnemy[self.walkCount//12], (self.x,self.y))
            self.walkCount += 1

        elif(self.up):
            window.blit(walkUpEnemy[self.walkCount//12], (self.x,self.y))
            self.walkCount += 1


run = True

player = user(x,y,character_width, character_height)

Goblin = []

Goblin.append(Enemy(900, 350, 1.8*character_width, 1.2*character_height))
Goblin[0].left = True
Goblin[0].maxDistance += 20

Goblin.append(Enemy(200, 320, 1.8*character_width, 1.2*character_height))
Goblin[1].right = True
Goblin[0].maxDistance -= 20



def updateScreen():
    window.blit(background, (0,0))
    player.updateChar(window)
    for i in range(len(Goblin)):
        Goblin[i].updateMonster(window)

    pygame.display.update()


#GAME LOOP:
while run:

    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # allows you to exit
            run = False

    keys = pygame.key.get_pressed() # gather user key info

    for i in range(len(Goblin)):
        if(Goblin[i].left == True): # Goblin Loop

            if(Goblin[i].directionCount == Goblin[i].maxDistance):
                Goblin[i].left = False
                Goblin[i].up = True
                Goblin[i].directionCount = 0
            else:
                Goblin[i].x -= Goblin[i].velocity
                Goblin[i].directionCount += 1

        elif(Goblin[i].up == True):

            if(Goblin[i].directionCount == Goblin[i].maxDistance):
                Goblin[i].up = False
                Goblin[i].right = True
                Goblin[i].directionCount = 0
            else:
                Goblin[i].y -= Goblin[i].velocity
                Goblin[i].directionCount += 1

        elif(Goblin[i].right == True):

            if(Goblin[i].directionCount == Goblin[i].maxDistance):
                Goblin[i].right = False
                Goblin[i].down = True
                Goblin[i].directionCount = 0
            else:
                Goblin[i].x += Goblin[i].velocity
                Goblin[i].directionCount += 1
        else:

            if(Goblin[i].directionCount == Goblin[i].maxDistance):
                Goblin[i].down = False
                Goblin[i].left = True
                Goblin[i].directionCount = 0
            else:
                Goblin[i].y += Goblin[i].velocity
                Goblin[i].directionCount += 1


    if(keys[pygame.K_LEFT] and player.x > player.velocity + 40):
        player.x -= player.velocity
        player.left = True
        player.right = False
        player.up = False
        player.down = False

    elif(keys[pygame.K_RIGHT] and player.x < screen_width - player.width - player.velocity - 40):
        player.x += player.velocity
        player.right = True # for animation
        player.left = False #
        player.up = False
        player.down = False

    elif(keys[pygame.K_UP] and player.y > player.velocity + 200):
        player.y -= player.velocity
        player.right = False # for animation
        player.left = False #
        player.up = True
        player.down = False

    elif(keys[pygame.K_DOWN] and player.y < screen_length - player.height - player.velocity - 140):
        if(player.isJump == False):
            player.y += player.velocity
            player.right = False # for animation
            player.left = False #
            player.up = False
            player.down = True
    else:
        if(player.isJump == False):
            player.right = False #
            player.left = False # for animation
            player.up = False
            player.down = False
            player.walkCount = 0  #

    if(player.isJump == False): # if not(isJump)
        if(keys[pygame.K_SPACE]):
            player.isJump = True
            player.walkCount = 0

    else: # so we cannot jump twice in mid-air

        if(player.jumpCount >= -player.jumpDistance):

            if(player.jumpCount < 0):
                player.y += (player.jumpCount ** 2) / 2

            else:
                player.y -= (player.jumpCount ** 2) / 2

            player.jumpCount -= 1

        else: # restore default values
            player.isJump = False
            player.jumpCount = player.jumpDistance

    updateScreen()


pygame.quit()