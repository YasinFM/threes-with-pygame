'''
MohammadYasin Farshad
Des 2022
'''
import pygame
import sys
import random

pygame.init()
White = (6, 23, 21)
Black = (13,47,44)
Yellow = (249,99,44)
Orange = (228,174,0)
screen = pygame.display.set_mode((800,920))
pygame.display.set_caption("Threes!")
font = pygame.font.SysFont("Times new Roman",75)
screen.fill('White')
Snn = pygame.Rect(30,30,740,740)
pygame.draw.rect(screen,Orange,Snn,0,30)

### Defining Each Row
Snn = pygame.Rect(60,60,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(235,60,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(410,60,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(585,60,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(60,235,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(235,235,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(410,235,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(585,235,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(60,410,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(235,410,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(410,410,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(585,410,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(60,585,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(235,585,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(410,585,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(585,585,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
pygame.display.flip( )

### Defining Functions
def R(y):
    x = y[:]
    for i in range(len(x)):
        for j in range(len(x)-2,-1,-1):
            if x[i][j] == 0 or x[i][j+1]== x[i][j] == 2 or x[i][j+1] == x[i][j] == 1 :
                continue
            if x[i][j+1] == 0:
                x[i][j+1] = x[i][j]
                x[i][j] = 0
            elif x[i][j+1] == x[i][j] or x[i][j] + x[i][j+1] == 3:
                x[i][j+1] = x[i][j] + x[i][j+1]
                x[i][j] = 0
    return x
def L(y):
    x = y[:]
    for i in range(len(x)):
        x[i] = x[i][::-1]
    x = R(x)
    for i in range(len(x)):
        x[i] = x[i][::-1]
    return x
def U(y):
    x = y[:]
    for i in range(len(x)):
        for j in range(1,len(x)):
            if x[j][i] == 0 or x[j-1][i] == x[j][i] == 2 or x[j-1][i] == x[j][i] == 1:
                continue
            if x[j-1][i] == 0:
                x[j-1][i] = x[j][i]
                x[j][i] = 0
            elif x[j-1][i] == x[j][i] or x[j-1][i]+x[j][i] == 3:
                x[j-1][i] += x[j][i]
                x[j][i] = 0
    return x
def D(y):
    x = y[:]
    x = x[::-1]
    x = U(x)
    x = x[::-1]
    return x
def mr(x):
    m = 0
    for i in range(len(x)):
        if x[i][0] == '0' :
            m += 1
    return m

def ml(x):
    m = 0
    for i in range(len(x)):
        if x[i][(len(x)-1)] == '0' :
            m += 1
    return m

def md(x):
    m = 0
    for i in range(len(x)):
        if x[0][i] == '0' :
            m += 1
    return m

def mu(x):
    m = 0
    for i in range(len(x)):
        if x[(len(x)-1)][i] == '0' :
            m += 1
    return m

def shift(x,k):
    z = x[k::]
    p = x[:k+1:]
    x = p + z
    return x


def checknot(z,x):
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i][j] != z[i][j] :
                return True
    return False

def t2(x):
    if x == 1:
        return 0
    return t2(x//2)+1

def namomken0(x):
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i][j] == '0':
                return False
    return True

def namomkenr(x):
    for i in range(len(x)-1):
        if x[i] != '1' and x[i] != '2':
            if x[i] == x[i+1]:
                return False
        elif x[i] == '1' :
            if x[i+1] == '2':
                return False
        elif x[i] == '2' :
            if x[i+1] == '1':
                return False
    return True

def namomkenc(x):
    b = []
    for i in range(len(x)):
        c = []
        for j in range(len(x)):
            c += [x[j][i]]
        b += [c]
    x = b
    if namomkenr(x):
        return True
    return False

def namomken(x):
    if namomken0(x):
        if namomkenr(x):
            if namomkenc(x):
                return True
    return False


def TC(x):
    tc = []
    for i in range(len(x)):
        for j in range(len(x)):
            tc += [x[i][j]]
    return tc
def check(x,tc):
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i][j] != tc[(i*4)+j]:
                return True
    return False
def NewNumber(x,d,k,tt):
    m = 0
    Z = -1
    if tt == 'D':
        for i in range(len(x)):
             if x[0][i] == 0:
                 m +=1
        for j in range(len(x)):
                if x[0][j] == 0:
                    Z += 1
                    if Z == k%m:
                        x[0][j] = d
                        return x
    elif tt == 'U':
        for i in range(len(x)):
             if x[len(x)-1][i] == 0:
                 m +=1
        for j in range(len(x)):
            if x[len(x)-1][j] == 0:
                Z += 1
                if Z == k%m:
                    x[len(x)-1][j] = d
                    return x
    elif tt == 'R':
        for i in range(len(x)):
            if x[i][0] == 0:
                m += 1
        for j in range(len(x)):
            if x[j][0] == 0:
                Z += 1
                if Z == k%m:
                    x[j][0] = d
                    return x
    elif tt == 'L':
        for i in range(len(x)):
            if x[i][len(x)-1] == 0:
                m += 1
        for j in range(len(x)):
            if x[j][len(x)-1] == 0:
                Z += 1
                if Z == k%m:
                    x[j][len(x)-1] = d
                    return(x)
    return x

def t2(x):
    if x == 1:
        return 0
    return t2(x//2)+1

def point(x):
    score = 0
    for i in range(len(x)):
        for j in range(len(x)):
            n = int(x[i][j])
            if n != 0 and n != 1 and n != 2:
                n = n//3
                n = t2(n)
                score += (3**(n+1))
    return score

### Main Body of Code
nn = [[0]*4 for i in range(4)]
for i in range(9):
    r,c = random.randint(0,3), random.randint(0,3)
    while nn[r][c]!=0:
        r,c = random.randint(0,3), random.randint(0,3)
    nn[r][c] = random.randint(1,3)

nn_chek = TC(nn)
TT = ''
flag = False
d = random.randint(1,3)
while True:
    Check = check(nn,nn_chek)
    if Check:
        nn = NewNumber(nn,d,random.randint(1,4),TT)
        nn_chek = TC(nn)
        d = random.randint(1,3)
        #row 1
        Snn = pygame.Rect(60,60,150,150)
        pygame.draw.rect(screen,Yellow,Snn,0,30)
        Snn = pygame.Rect(235,60,150,150)
        pygame.draw.rect(screen,Yellow,Snn,0,30)
        Snn = pygame.Rect(410,60,150,150)
        pygame.draw.rect(screen,Yellow,Snn,0,30)
        Snn = pygame.Rect(585,60,150,150)
        pygame.draw.rect(screen,Yellow,Snn,0,30)
        #row 2
        Snn = pygame.Rect(60,235,150,150)
        pygame.draw.rect(screen,Yellow,Snn,0,30)
        Snn = pygame.Rect(235,235,150,150)
        pygame.draw.rect(screen,Yellow,Snn,0,30)
        Snn = pygame.Rect(410,235,150,150)
        pygame.draw.rect(screen,Yellow,Snn,0,30)
        Snn = pygame.Rect(585,235,150,150)
        pygame.draw.rect(screen,Yellow,Snn,0,30)
        #row 3
        Snn = pygame.Rect(60,410,150,150)
        pygame.draw.rect(screen,Yellow,Snn,0,30)
        Snn = pygame.Rect(235,410,150,150)
        pygame.draw.rect(screen,Yellow,Snn,0,30)
        Snn = pygame.Rect(410,410,150,150)
        pygame.draw.rect(screen,Yellow,Snn,0,30)
        Snn = pygame.Rect(585,410,150,150)
        pygame.draw.rect(screen,Yellow,Snn,0,30)
        #row 4
        Snn = pygame.Rect(60,585,150,150)
        pygame.draw.rect(screen,Yellow,Snn,0,30)
        Snn = pygame.Rect(235,585,150,150)
        pygame.draw.rect(screen,Yellow,Snn,0,30)
        Snn = pygame.Rect(410,585,150,150)
        pygame.draw.rect(screen,Yellow,Snn,0,30)
        Snn = pygame.Rect(585,585,150,150)
        pygame.draw.rect(screen,Yellow,Snn,0,30)
        pygame.display.flip( )
    else:
        checking = []
        for W in range(4):
            A = []
            for Q in range(4):
                    A += [nn_chek[Q*4:(Q+1)*4]]
            if W == 0:
                checking += [(L(A))]
            elif W == 1:
                checking += [(D(A))]
            elif W == 2:
                checking += [(R(A))]
            elif W == 3:
                checking += [(U(A))]
        if checking[0]==checking[1]==checking[2]==checking[3]==nn:
            flag = True
            break
    if flag:
        break
    for i in range(4):
        XY = 115
        for j in range(4):
            ttext = str(nn[i][j])
            font_name , font_size = "Arial" , 80
            color = (0,0,0)
            if nn[i][j] == 1:
                color = (20,190,88)
            if nn[i][j] == 2:
                color = (22,101,190)
            if nn[i][j] == 0:
                ttext = ''
            text = font.render(ttext,True,color)
            XY = 115
            if int(nn[i][j]) > 10:
                XY = 95
            elif int(nn[i][j]) > 100:
                XY = 75
            screen.blit(text,(XY + j*(175),95+i*(175)))
    Snn = pygame.Rect(0,800,800,120)
    pygame.draw.rect(screen,White,Snn)
    Snn = pygame.Rect(205,780,125,125)
    pygame.draw.rect(screen,Yellow,Snn,0,30)
    color = (0,0,0)
    if d == 1:
        color = (20,190,88)
    if d == 2:
        color = (22,101,190)
    text = font.render(str(d),True,color)
    screen.blit(text,(250,800))
    SCORE = point(nn)
    text = font.render("score : "+str(SCORE),True,Yellow)
    screen.blit(text,(400,800))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if  event.key== pygame.K_UP :
                TT = 'U'
                nn = U(nn)
                break
            elif  event.key== pygame.K_RIGHT :
                TT = 'R'
                nn = R(nn)
                break
            elif event.key== pygame.K_LEFT :
                TT = 'L'
                nn = L(nn)
                break
            elif  event.key == pygame.K_DOWN :
                TT = 'D'
                nn = D(nn)
                break
            elif event.key == pygame.K_ESCAPE:
                flag = True
                break
    if flag:
        break
nn = NewNumber(nn,random.randint(1,3),random.randint(1,4),TT)
##print nn and score
#row 1
Snn = pygame.Rect(60,60,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(235,60,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(410,60,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(585,60,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
#row 2
Snn = pygame.Rect(60,235,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(235,235,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(410,235,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(585,235,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
#row 3
Snn = pygame.Rect(60,410,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(235,410,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(410,410,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(585,410,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
#row 4
Snn = pygame.Rect(60,585,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(235,585,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(410,585,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
Snn = pygame.Rect(585,585,150,150)
pygame.draw.rect(screen,Yellow,Snn,0,30)
pygame.display.flip( )
for i in range(4):
    XY = 115
    for j in range(4):
        ttext = str(nn[i][j])
        font_name , font_size = "Arial" , 80
        color = (0,0,0)
        if nn[i][j] == 1:
            color = (20,190,88)
        if nn[i][j] == 2:
            color = (22,101,190)
        if nn[i][j] == 0:
            ttext = ''
        text = font.render(ttext,True,color)
        XY = 115
        if nn[i][j] > 10:
            XY = 95
        elif nn[i][j] > 100:
            XY = 75
        screen.blit(text,(XY + j*(175),95+i*(175)))
        pygame.display.flip()
score = 0
for i in nn:
    for j in range(4):
        temp_score = 0
        if i[j]%3 == 0 and i[j] != 0:
            temp_score += 1
            TI = i[j]//3
            TS = 1
            while TI != 1:
                TI = TI//2
                TS += 1
            for k in range(TS):
                temp_score = temp_score*3
        score += temp_score
if TC(R(nn[:]))==TC(nn) and TC(L(nn[:]))==TC(nn) and TC(D(nn[:]))==TC(nn) and TC(U(nn[:]))==TC(nn):
    Snn = pygame.Rect(50,770,700,150)
    pygame.draw.rect(screen,White,Snn)
    Snn = pygame.Rect(50,800,700,100)
    pygame.draw.rect(screen,Black,Snn,0,40)
    text = font.render('The final score is '+str(score)+'.',True,Yellow)
    screen.blit(text,(60,810))
    pygame.display.flip()
else:
    Snn = pygame.Rect(50,770,700,150)
    pygame.draw.rect(screen,White,Snn)
    Snn = pygame.Rect(50,800,700,100)
    pygame.draw.rect(screen,Black,Snn,0,40)
    text = font.render('The partial score is '+str(score)+'.',True,Yellow)
    screen.blit(text,(60,810))
    pygame.display.flip()
while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key== pygame.K_ESCAPE):
            exit(0)