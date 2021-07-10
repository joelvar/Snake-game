import pygame
import time
import random

pygame.init()
run = True

exist = [0,0]
size= (20,20)

speed = 15
width = 1500
height = 800

colour = (0,0,0)

food_width = width//2
food_height=height//2

food_colour = (255,255,255)
food_size = (25,25)
char_colour = (255,0,255)

snake = 1 #set length of snake to be atleast >=1
queue=[]

screen = pygame.display.set_mode((width,height))
screen.fill(colour)
pygame.display.set_caption("Joel's Snake Gaame")

font_size = 32
font = pygame.font.SysFont("calibri.ttf",font_size)
text = font.render("SCORE : 0", True, (255,255,255),colour)
text_rect = text.get_rect()
text_rect.center = (width//2,font_size)
pygame.display.update()

def drawfood(pos,size,colour):
    coordinates = pygame.Rect((pos[0],pos[1]),(size[0],size[1]))
    pygame.draw.rect(screen,colour,coordinates)
    pygame.display.update()

def placefood(pos,size,colour):
    coordinates = pygame.Rect((pos[0], pos[1]), (size[0], size[1]))
    pygame.draw.rect(screen,colour,coordinates)

def erase(pos, size, colour):
    coordinates = pygame.Rect(pos[0],pos[1],size[0],size[1])
    screen.fill(colour,coordinates)

def up():
    if exist[1] - speed < font_size:
        exist[1] = height
    exist[1]-=speed
    queue.append(exist[:])
    drawRect(exist,size,char_colour)

def down():
    if exist[1] + speed > height:
        exist[1] = 0
    exist[1] += speed
    queue.append(exist[:])
    drawRect(exist, size, char_colour)

def left():
    if exist[0] - speed < 0:
        exist[0] = width 
    exist[0] -= speed
    queue.append(exist[:])
    drawRect(exist, size, char_colour)

def right():
    if exist[0] + speed > width:
        exist[0] = 0 
    exist[0] += speed
    queue.append(exist[:])
    drawRect(exist, size, char_colour)

mouse_is_pressed = False
move_right = True
move_left = False
move_down = False
move_up = False

def eatFood():
    global limit
    global food_width
    global food_height
    global food_colour
    global char_colour

    char_colour = food_colour[:]

    limit += 1
    food_width = randint(speed,width - speed)
    food_height = randint(speed + font_size, height - speed)
    food_colour = (randint(10, 255), randint(10, 255), randint(10, 255))


def reset():
    global queue
    global limit
    print("collide!")
    for _ in range(len(queue)):
        erase(queue.pop(0), size, colour)
    limit = 1
    erase([width // 4, 0], [width // 2, font_size*2], colour)

    
