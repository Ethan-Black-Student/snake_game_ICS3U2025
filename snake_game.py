import pygame
import time
import random
<<<<<<< HEAD

=======
>>>>>>> a1d68ee08b2cfa0558d1dff58a57b8d3dba7f517

#Define colours
black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0
red = 255, 0, 0
yellow = 255, 255, 0
blue = 0, 0, 255
purple = 255, 0, 255

#Initial screen stuff
pygame.init()
width, height = 720, 480
pygame.display.set_caption('ICS3U/C1 Snake Game')
screen = pygame.display.set_mode((width, height))

#Snake Information
snake_position = [360, 240]
snake_speed = 10
direction = 'RIGHT'
snake_body = [[360,240],[350,240],[340,240],[330,240]]

<<<<<<< HEAD
fruit_position = [random.randrange(0, (width//10))*10 +5, random.randrange(0, (height//10))*10 +5]

def endgame():

    my_font = pygame.font.SysFont('comicsansms', 50)

    game_over_surface = my_font.render('GAME OVER', True, white)

    game_over_rect = game_over_surface.get_rect()

    game_over_rect.center = [(width/2), (height/2)]

    screen.blit(game_over_surface, game_over_rect)

    pygame.display.flip()

    time.sleep(2)

    pygame.quit()

=======
#FRUIT!
fruit_position = [random.randrange(0, (width//10))*10,
                  random.randrange(0, (height//10))*10]

def endgame():
    #Create a font object
    my_font = pygame.font.SysFont('comicsansms', 50)

    #Create text surface
    game_over_surface = my_font.render('GAME OVER', True, red)

    #Create a rectangle object for the surface
    game_over_rect = game_over_surface.get_rect()

    #Position our game over object
    game_over_rect.center = [(width/2), (height/2)]

    #blit = draw the surface onto the rectangle
    screen.blit(game_over_surface, game_over_rect)

    pygame.display.flip() #Update the screen

    time.sleep(2)

    #Deactivate the quit
    pygame.quit()
>>>>>>> a1d68ee08b2cfa0558d1dff58a57b8d3dba7f517
    quit()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction != 'DOWN':
                direction = 'UP'
            if event.key == pygame.K_s and direction != 'UP':
                direction = 'DOWN'
            if event.key == pygame.K_a and direction != 'RIGHT':
                direction = 'LEFT'
            if event.key == pygame.K_d and direction != 'LEFT':
                direction = 'RIGHT'

    screen.fill(black) #Fill in the screen

    #Set the snake on the screen
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
    
<<<<<<< HEAD
    pygame.draw.circle(screen, red, fruit_position, 7.5)
=======
    #Draw my fruit
    pygame.draw.circle(screen, red, (fruit_position[0]+5,fruit_position[1]+5),5)
>>>>>>> a1d68ee08b2cfa0558d1dff58a57b8d3dba7f517

    #Moving the snake
    if direction == 'RIGHT':
        snake_position[0] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10

    snake_body.insert(0, list(snake_position))

<<<<<<< HEAD
    if snake_position == fruit_position:

        fruit_position = [random.randrange(0, width, 10) +5, random.randrange(0, height, 10) +5]

    else:

        print(snake_position, ":", fruit_position)
=======
    #Eat the fruit
    if snake_position==fruit_position:
        fruit_position = [random.randrange(0, (width//10))*10,
                        random.randrange(0, (height//10))*10]
    else:
>>>>>>> a1d68ee08b2cfa0558d1dff58a57b8d3dba7f517
        snake_body.pop()

    pygame.display.flip()

    #Create a clock
    clock = pygame.time.Clock()
    clock.tick(snake_speed)

<<<<<<< HEAD
    if snake_position[0] < 0 or snake_position[0] >= width:

        endgame()

    if snake_position[1] < 0 or snake_position[1] >= height:

        endgame()

    for block in snake_body[1:]:

        if snake_position[0] == block[0] and snake_position[1] == block[1]:

=======
    #Endgame conditions
    if snake_position[0] < 0 or snake_position[0] >= width:
        endgame()
    if snake_position[1] < 0 or snake_position[1] >= height:
        endgame()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
>>>>>>> a1d68ee08b2cfa0558d1dff58a57b8d3dba7f517
            endgame()

pygame.quit()