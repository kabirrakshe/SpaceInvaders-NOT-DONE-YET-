import pygame
import time


pygame.init()
pygame.display.init()
ship1 = pygame.image.load('starship1.png')
ship2 = pygame.image.load('starship2.png')
ship3 = pygame.image.load('starship3.png')
ship4 = pygame.image.load('starship4.png')
ship5 = pygame.image.load('starship5.png')
ship6 = pygame.image.load('starship6.png')
ship7 = pygame.image.load('starship7.png')
ship8 = pygame.image.load('starship8.png')

font = pygame.font.SysFont('comicsans', 80, True)
font2 = pygame.font.SysFont('comicsans', 20)

color = {
    'red': (255,0,0),
    'green': (0,255,0),
    'blue': (0,0,255),
    'white': (255,255,255),
    'black': (0,0,0),
    'yellow': (255,255,0)
}

canvas = pygame.display.set_mode((1080, 720))

speed = 10
rect = pygame.draw.rect
circ = pygame.draw.circle

class character():
    '''Controls functions of main character'''
    def __init__(self, x, y, chosenstarship):
        self.x = x
        self.y = y
        self.chosenstarship = chosenstarship
    def moveRight(self):
        self.x += speed
    def moveLeft(self):
        self.x -= speed
    def moveUp(self):
        self.y -= speed
    def moveDown(self):
        self.y += speed
    def draw(self):
        canvas.blit(self.chosenstarship, (self.x, self.y, 50, 50))
    def gun(self, x, y):
        rect(canvas, color['yellow'], (x, y, 5, 15))
    def special(self):
        circ(canvas, color['blue'], (self.x+27, self.y-65), 30)

def introduction():
    notClicked = True
    tempcolor = 'white'
    poslst = [(50, 240), (320, 240), (590, 240), (860, 240), (50, 480), (320, 480), (590, 480),(860, 480)]
    shiplst = [ship1,ship2,ship3,ship4,ship5,ship6,ship7,ship8]
    current = 0
    count = 0
    text = font.render(str('CHOOSE YOUR VESSEL'), 2, color['white'])
    text4 = font2.render(str('Sidewinder'), 2, color['white'])
    text7 = font2.render(str('Twilight'), 2, color['white'])
    text5 = font2.render(str('Scythe'), 2, color['white'])
    text2 = font2.render(str('Hurricane'), 2, color['white'])
    text3 = font2.render(str('Nightingale'), 2, color['white'])
    text8 = font2.render(str('Viper'), 2, color['white'])
    text1 = font2.render(str('Marauder'), 2, color['white'])
    text6 = font2.render(str('Titan'), 2, color['white'])

    while (notClicked):
        canvas.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: quit()
        keys = pygame.key.get_pressed()


        if keys[pygame.K_RETURN]:
            notClicked = False
            tempcolor = 'green'
            chosen = shiplst[current]

        elif keys[pygame.K_RIGHT] and current %4 != 3 and count % 6 == 0:
            current += 1
        elif keys[pygame.K_LEFT] and current % 4 != 0 and count % 6 == 0:
            current -= 1
        elif keys[pygame.K_DOWN] and current < 4 and count %6 == 0:
            current += 4
        elif keys[pygame.K_UP] and current > 3 and count % 6 == 0:
            current -= 4



        canvas.blit(text, (125, 75))

        canvas.blit(text1, (85, 220))
        canvas.blit(text2, (355, 220))
        canvas.blit(text3, (620, 220))
        canvas.blit(text4, (885, 220))
        canvas.blit(text5, (85, 460))
        canvas.blit(text6, (365, 460))
        canvas.blit(text7, (625, 460))
        canvas.blit(text8, (905, 460))

        canvas.blit(pygame.transform.scale2x(ship1), (55, 240))
        canvas.blit(pygame.transform.scale2x(ship2), (325, 240))
        canvas.blit(pygame.transform.scale2x(ship3), (595, 240))
        canvas.blit(pygame.transform.scale2x(ship4), (865, 240))
        canvas.blit(pygame.transform.scale2x(ship5), (55, 480))
        canvas.blit(pygame.transform.scale2x(ship6), (325, 480))
        canvas.blit(pygame.transform.scale2x(ship7), (595, 480))
        canvas.blit(pygame.transform.scale2x(ship8), (865, 480))

        rect(canvas, color[tempcolor], (poslst[current][0], poslst[current][1], 130, 130), 1)

        pygame.display.update()
        count += 1
    time.sleep(2)
    return chosen


def main():
    cooldown = 0
    hero = character(235,235,introduction())
    bullet_indices = []
    while True:
        canvas.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and hero.y <= 690:
            hero.moveDown()
        if keys[pygame.K_UP] and hero.y >= 0:
            hero.moveUp()
        if keys[pygame.K_RIGHT] and hero.x <= 1050:
            hero.moveRight()
        if keys[pygame.K_LEFT] and hero.x >= 0:
            hero.moveLeft()

        if keys[pygame.K_SPACE] and cooldown == 10:
            cooldown = 0
            hero.gun(hero.x+30, hero.y-18)
            bullet_indices.append([hero.x+30, hero.y-18])



        for i in range(len(bullet_indices)):
            bullet_indices[i][1] -= 5
            hero.gun(bullet_indices[i][0], bullet_indices[i][1])
            if bullet_indices[i][0] < 0:
                bullet_indices.pop(i)

        if cooldown != 10:
            cooldown += 1





        hero.draw()


        pygame.display.update()

    pygame.quit()

main()
