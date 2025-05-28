import pygame
import time
import random


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
    
    pygame.draw.circle(screen, red, fruit_position, 7.5)

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

    if snake_position == fruit_position:

        fruit_position = [random.randrange(0, width, 10) +5, random.randrange(0, height, 10) +5]

    else:

        print(snake_position, ":", fruit_position)
        snake_body.pop()

    pygame.display.flip()

    #Create a clock
    clock = pygame.time.Clock()
    clock.tick(snake_speed)

    if snake_position[0] < 0 or snake_position[0] >= width:

        endgame()

    if snake_position[1] < 0 or snake_position[1] >= height:

        endgame()

    for block in snake_body[1:]:

        if snake_position[0] == block[0] and snake_position[1] == block[1]:

            endgame()

pygame.quit()