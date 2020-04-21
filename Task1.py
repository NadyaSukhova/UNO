# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

list = ['red_0','blue_0','yellow_0','green_0']
for i in range(1,10):
    list += ['red_' + str(i)] * 2
    list += ['blue_' + str(i)] * 2
    list += ['yellow_' + str(i)] * 2
    list += ['green_' + str(i)] * 2
list += ['red_reverse', 'red_+2', 'red_skip'] * 2 + ['green_reverse', 'green_+2', 'green_skip'] * 2 \
        + ['yellow_reverse', 'yellow_+2', 'yellow_skip'] * 2 + ['blue_reverse', 'blue_+2', 'blue_skip'] * 2
list += ['black_wildcard', 'black_+4'] * 4


colors = ['red', 'black', 'blue', 'green', 'yellow']
s = 'C:\\Users\\Надежда\\Desktop\\pict\\'

pic = pygame.image.load( s + 'pic.png')
pic = pygame.transform.scale(pic, (50,50))

gam = []
def choose():
    s1 = random.randint(0, len(list) - 1)
    s = list[s1]
    del list[s1]
    return s

def mark(numb):
    if numb == 0:
        screen.blit(pic, (575, 600 - 210))
    elif k == 2:
        if numb == 1:
            screen.blit(pic, (575, 190))
    elif k == 3:
        if numb == 1:
            screen.blit(pic, (575, 190))
        if numb == 2:
            screen.blit(pic, (200, 300 - 35))
    elif k == 4:
        if numb == 2:
            screen.blit(pic, (575, 190))
        if numb == 3:
            screen.blit(pic, (200, 300 - 35))
        if numb == 1:
            screen.blit(pic, (1200 - 220, 300 - 35))

def prov1(gam, num, car,):
    f = False
    for i in range(len(gam[num])):
        s = str(gam[num][i])
        s1 = str(car)
        if (s[0] == s1[0] and s[2] == s1[2]) \
                or (s[len(s) - 1] == s1[len(s1) - 1] and s[len(s) - 2] == s1[len(s1) - 2]):
            f = True
            break
    for i in range(len(gam[num])):
        s = str(gam[num][i])
        if (s.find('black') != -1):
            f = True
            break
    return f


def prov2(gam, num, car,):
    f = False
    for i in range(len(gam[num])):
        s = str(gam[num][i])
        s1 = str(car)
        if (s[0] == s1[0] and s[2] == s1[2]) \
                or (s[len(s) - 1] == s1[len(s1) - 1] and s[len(s) - 2] == s1[len(s1) - 2]):
            f = True
            break
    return f

def print():
    screen.fill(GREEN)
    if k == 2:
        x = 160
        y1 = 470
        y2 = 30
        for i in range(len(gam[0])):
            c = pygame.image.load(s + str(gam[0][i]) + '.png')
            screen.blit(c, (x + i * int((1200 - 160 - 70) / (len(gam[0]))), y1))

        for i in range(len(gam[1])):
            c = pygame.image.load(s + str(gam[1][i]) + '.png')
            screen.blit(c, (x + i * int((1200 - 160 - 70) / (len(gam[1]))), y2))
    elif k == 3:
        x = 160
        y1 = 470
        y2 = 30
        for i in range(len(gam[0])):
            c = pygame.image.load(s + str(gam[0][i]) + '.png')
            screen.blit(c, (x + i * int((1200 - 160 - 70) / (len(gam[0]))), y1))

        for i in range(len(gam[1])):
            c = pygame.image.load(s + str(gam[1][i]) + '.png')
            screen.blit(c, (x + i * int((1200 - 160 - 70) / (len(gam[1]))), y2))
        x1 = 30
        y1 = 30 + 100
        for i in range(len(gam[2])):
            c = pygame.transform.rotate(pygame.image.load(s + str(gam[2][i]) + '.png'), -90)
            screen.blit(c, (x1, y1 + i * ((600 - 100 - 100 - 30) / ((len(gam[2])) + 1))))

    elif k == 4:
        x = 160
        y1 = 470
        y2 = 30
        for i in range(len(gam[0])):
            c = pygame.image.load(s + str(gam[0][i]) + '.png')
            screen.blit(c, (x + i * int((1200 - 160 - 70) / (len(gam[0]))), y1))
        for i in range(len(gam[2])):
            c = pygame.image.load(s + str(gam[2][i]) + '.png')
            screen.blit(c, (x + i * int((1200 - 160 - 70) / (len(gam[2]))), y2))
        x1 = 1200 - 30 - 100
        y1 = 30 + 100
        for i in range(len(gam[1])):
            c = pygame.transform.rotate(pygame.image.load(s + str(gam[1][i]) + '.png'), 90)
            screen.blit(c, (x1, y1 + i * ((600 - 100 - 100 - 30) / ((len(gam[1])) + 1))))
        x1 = 30
        y1 = 30 + 100
        for i in range(len(gam[3])):
            c = pygame.transform.rotate(pygame.image.load(s + str(gam[3][i]) + '.png'), -90)
            screen.blit(c, (x1, y1 + i * ((600 - 100 - 100 - 30) / ((len(gam[3])) + 1))))



WIDTH = 1200
HEIGHT = 600
FPS = 30

# Задаем цвета
GREEN = (50, 100, 50)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("UNO")
ic = pygame.image.load(s + 'cat.png')
pygame.display.set_icon(ic)
clock = pygame.time.Clock()

# Цикл игры
running = True

x = 470
y = 150

screen.fill(GREEN)
col = (255, 255, 255)


card = pygame.image.load(s+ 'cat.png')

screen.blit(card, (x, y))

fond = pygame.font.SysFont('kokila', 32)
words = fond.render("Wanna play UNO?", 1, (0, 0, 0), (255, 255, 255))
screen.blit(words, (700, 150))
w = 150
h = 100
x = 525
y = 310
k = 0
pygame.draw.rect(screen, (255,255,255), (x, y, w, h))
words = fond.render("Sure", 1, (0, 0, 0), (255, 255, 255))
screen.blit(words, (x + 45, y + 30))
f = False
while running:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        x_m, y_m = pygame.mouse.get_pos()
        if (x_m >= x and x_m <= x + w and y_m >= y and y_m <= y + h):
            screen.fill(GREEN)
            f = True
            break
    elif event.type == pygame.QUIT:
        running = False
    pygame.display.update()
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
if running == False:
    pygame.quit()
while running:
    if (f):
        x1 = x - w - 10
        x2 = x
        x3 = x + w + 10
        screen.blit(card, (460, 90))
        words = fond.render("How many players are there?", 1, (0, 0, 0), (255, 255, 255))
        screen.blit(words, (460, 250))
        pygame.draw.rect(screen, (255, 255, 255), (x1, y, w, h))
        pygame.draw.rect(screen, (255, 255, 255), (x2, y, w, h))
        pygame.draw.rect(screen, (255, 255, 255), (x3, y, w, h))
        words = fond.render("3", 1, (0, 0, 0), (255, 255, 255))
        screen.blit(words, (x + w / 2 - 10, y + h / 2 - 10))
        words = fond.render("2", 1, (0, 0, 0), (255, 255, 255))
        screen.blit(words, (x - w + w / 2 - 20, y + h / 2 - 10))
        words = fond.render("4", 1, (0, 0, 0), (255, 255, 255))
        screen.blit(words, (x + w / 2 + w, y + h / 2 - 10))
        pygame.display.update()
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONDOWN:
            m1, m2 = pygame.mouse.get_pos()
            if (m1 >= x1 and m1 <= x1 + w and m2 >= y and m2 <= y + h):
                k = 2
                screen.fill(GREEN)
                break
            elif (m1 >= x2 and m1 <= x2 + w and m2 >= y and m2 <= y + h):
                k = 3
                screen.fill(GREEN)
                break
            elif (m1 >= x3 and m1 <= x3 + w and m2 >= y and m2 <= y + h):
                k = 4
                screen.fill(GREEN)
                break

        elif event.type == pygame.QUIT:
                running = False
        pygame.display.update()
            # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

if running == False:
    pygame.quit()


kol = 7
mas = []
for i in range(kol):
        s1 = choose()
        mas.append(s1)
gam.append(mas)
mas = []
for i in range(kol):
        s1 = choose()
        mas.append(s1)
gam.append(mas)
mas = []
if k >= 3:
        x1 = 30
        y1 = 30 + 100
        for i in range(kol):
            s1 = choose()
            mas.append(s1)
        gam.append(mas)
        mas = []
if k == 4:
        x1 = 1200 - 30 - 100
        y1 = 30 + 100
        for i in range(kol):
            s1 = choose()
            mas.append(s1)
        gam.append(mas)
if running == True:
        print()
        pygame.display.update()



while running:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        numb = random.randint(0, (k - 1))
        car = random.choice(gam[numb])
        while (car.find('black') != -1 and car.find('+4') != -1):
            car = random.choice(gam[numb])
        card = pygame.image.load(s + car + '.png')
        gam[numb].remove(car)
        print()
        mark(numb)
        if (car.find('wild') != -1):
            numb -= 1
            car = random.choice(colors)
            while not prov2(gam, numb, car):
                car = random.choice(colors)
        if (numb == -1):
            numb = 0
        screen.blit(card, (565, 250))
        pygame.display.update()
        break
    elif event.type == pygame.QUIT:
        running = False
if running == False:
    pygame.quit()

A = 1
B = 0
C = k
if car.find('skip') != -1:
    numb += A
    if numb == C:
        numb = B
if car.find('reverse') != -1:
    A = -A
    if B == 0:
        B = k - 1
    else:
        B = 0
    if C == k:
        C = -1
    else:
        C = k

if car.find('+2') != -1:
    numb = (numb + A) % k
    s1 = choose()
    gam[numb].append(s1)
    s1 = choose()
    gam[numb].append(s1)
verh = car
while running:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        numb += A
        if numb == C:
            numb = B
        if prov1(gam, numb, car) == False or car.find('black') != -1:
            s1 = choose()
            gam[numb].append(s1)
            numb -= A
            print()
            mark((numb + A) % k)
            card = pygame.image.load(s + verh + '.png')
            screen.blit(card, (565, 250))

            pygame.display.update()
        else:
            car1 = random.choice(gam[numb])
            while not ((car[0] == car1[0] and car[2] == car1[2])
                       or (car[len(car) - 1] == car1[len(car1) - 1] and car[len(car) - 2] == car1[len(car1) - 2]) or (car1.find('black') != -1)):
                car1 = random.choice(gam[numb])
            gam[numb].remove(car1)
            print()
            mark(numb)
            if car1.find('skip') != -1:
                numb += A
                if numb == C:
                    numb = B
                car = car1
                verh = car
            elif car1.find('reverse') != -1:
                A = -A
                if B == 0:
                    B = k - 1
                else:
                    B = 0
                if C == k:
                    C = -1
                else:
                    C = k
                car = car1
                verh = car
            elif car1.find('+2') != -1:
                numb = (numb + A) % k
                s1 = choose()
                gam[numb].append(s1)
                s1 = choose()
                gam[numb].append(s1)
                car = car1
                verh = car
            elif car1.find('+4') != -1:
                numb = (numb + A) % k
                s1 = choose()
                gam[numb].append(s1)
                s1 = choose()
                gam[numb].append(s1)
                s1 = choose()
                gam[numb].append(s1)
                s1 = choose()
                gam[numb].append(s1)
                verh = car1
                car = car.split('_')[0]
            elif car1.find('wild') != -1:
                car = 'black'
                while not prov2(gam, numb, car):
                  car = random.choice(colors)
                numb -= A
                verh = car1
            else:
                car = car1
                verh = car
        card = pygame.image.load(s + verh + '.png')
        screen.blit(card, (565, 250))
        #pygame.time.wait(50)
        pygame.display.update()
        f = True
        number = - 1
        for i in range(k):
            if (len(gam[i]) == 0 or len(list) == 0):
                f = False
                if (len(gam[i]) == 0):
                    number = i
        if (f == False):
            break
    elif event.type == pygame.QUIT:
        running = False
if running == False:
    pygame.quit()


x = 470
y = 150
screen.fill(GREEN)
col = (255, 255, 255)
card = pygame.image.load(s + 'cat.png')
screen.blit(card, (x, y))
fond = pygame.font.SysFont('kokila', 32)
if (number != -1):
    if (number != 0):
        words = fond.render("Player " + str(number + 1) + " won!", 1, (0, 0, 0), (255, 255, 255))
    else:
        words = fond.render("You won!", 1, (0, 0, 0), (255, 255, 255))
else:
    words = fond.render("Noone won!", 1, (0, 0, 0), (255, 255, 255))
screen.blit(words, (700, 150))
pygame.display.update()
while running:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        running = False
    elif event.type == pygame.QUIT:
        running = False
pygame.quit()