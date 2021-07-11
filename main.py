
import pygame
import time
import random

pygame.init() # initialize game

run = True
exist = [0, 0]
size = (20, 20)
speed = 20
width = 1500
height = 800
colour = (0, 0, 0)
foodX = width // 2 
foodY = height // 2 
food_colour = (255, 255, 255) 
food_size = (25, 25)
char_colour = (0, 255, 255)


length = 3 #set length of snake to be atleast >=3

queue = [] # the length of the snake

# initialize screen
screen = pygame.display.set_mode((width, height)) 
screen.fill(colour)
pygame.display.set_caption("Joel's Snake Game")


font_size = 32
font = pygame.font.SysFont("calibri.ttf",font_size) # font type of the score displayed
text = font.render('YOUR SCORE: 0', True, (255, 255, 255), colour) 
TEXT_RECT = text.get_rect()
TEXT_RECT.center = (width // 2, font_size) # centers the score at the top
pygame.display.update()

 
def drawRect(pos, size, colour):
    coordinates = pygame.Rect((pos[0], pos[1]), (size[0], size[1])) # size[0] and size[1] being the width and height
    pygame.draw.rect(screen, colour, coordinates)
    pygame.display.update()

def placefood(pos, size, colour):
    coordinates = pygame.Rect((pos[0], pos[1]), (size[0], size[1]))
    pygame.draw.rect(screen, colour, coordinates)

def remove(pos, size, colour):
    coordinates = pygame.Rect(pos[0], pos[1], size[0], size[1])
    screen.fill(colour, coordinates)

def up():
    if exist[1] - speed < font_size: exist[1] = height
    exist[1] = exist[1]-speed
    queue.append(exist[:])
    drawRect(exist, size, char_colour) 

def left():
    if exist[0] - speed < 0: exist[0] = width 
    exist[0] = exist[0]-speed
    queue.append(exist[:])
    drawRect(exist, size, char_colour)

def down():
    if exist[1] + speed > height: exist[1] = 0
    exist[1] =exist[1] + speed
    queue.append(exist[:])
    drawRect(exist, size, char_colour)


def right():
    if exist[0] + speed > width: exist[0] = 0 
    exist[0] = exist[0] +speed
    queue.append(exist[:])
    drawRect(exist, size, char_colour)

move_right = True
move_left = False
move_down = False
move_up = False

def eatfood():
    global length
    global foodX
    global foodY
    global food_colour
    global char_colour

    char_colour = food_colour[:]

    length += 1
    foodX = random.randint(speed, width - speed)
    foodY = random.randint(speed + font_size, height - speed)
    food_colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def reset():
    global queue
    global length
    for i in range(len(queue)):
        remove(queue.pop(0), size, colour)
    length = 1
    remove([width // 4, 0], [width // 2, font_size*2], colour)


error = 25 # margin of error
frame_freq = 0.05

while run:

    placefood([foodX, foodY], food_size, food_colour) # randomly places food 
    time.sleep(frame_freq)
    
    visited = queue[:]
    if len(visited) >= 1:
        visited.pop()
    atefood = (foodX - error <= exist[0] <= foodX + error) and (foodY - error <= exist[1] <= foodY + error)

    if len(queue) > length:
        remove(queue.pop(0), size, colour) # maintains size of snake

    if move_up:
        if exist in visited: # will reset if there is a collision
            reset()

        if atefood:
            remove([foodX, foodY], food_size, colour) # removes the food as the snake goes over it
            eatfood()
        up()

    elif move_down:
        if exist in visited: # will reset if there is a collision
            reset()

        if atefood:
            remove([foodX, foodY], food_size, colour)
            eatfood()
        down()

    elif move_right:
        if exist in visited: # will reset if there is a collision
            reset()

        if atefood:
            remove([foodX, foodY], food_size, colour)
            eatfood()
        right()

    elif move_left:
        if exist in visited: # will reset if there is a collision
            reset()
            length = 1

        if atefood:
            remove([foodX, foodY], food_size, colour)
            eatfood()

        left()
   
    
    score = "YOUR SCORE: " + str(length * 10-10) 
    text = font.render(score, True, (255, 255, 255), colour)
    screen.blit(text, TEXT_RECT)

    for event in pygame.event.get():
        action = event.type
        if action == pygame.QUIT:
            run = False

        elif action == pygame.KEYDOWN:
            
            if event.key == pygame.K_SPACE: # if a key other that w,a,s,d,up,down,left,right  is pressed
                pass

            if event.key == pygame.K_w or event.key == pygame.K_UP: #if up arrow key or w is pressed
                move_up = True
                move_down = False
                move_right = False
                move_left = False
                
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT: #if left arrow key or a is pressed
                move_up = False
                move_down = False
                move_right = False
                move_left = True

            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:#if down arrow key or s is pressed
                move_up = False
                move_down = True
                move_right = False
                move_left = False
                
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:#if right arrow key or d is pressed
                move_up = False
                move_down = False
                move_right = True
                move_left = False
