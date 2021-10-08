# This is a python game program built with the pygame library and its modules
# It contains one player object and three enemy objects. If there's a 
# Collision between the player and any enemy object the player loses
# Else the player wins.

import pygame
import random

#Initialise screen w
pygame.init()
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))

#======================================================================#

# Create a player image and three enemy images

player = pygame.image.load("image.png")
enemy1 = pygame.image.load("enemy.png")
enemy2 = pygame.image.load("monster.jpg")
enemy3 = pygame.image.load("player.jpg")

#======================================================================#

# Get the width and height of the images
image_height = player.get_height()
image_width = player.get_width()

enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

#======================================================================#

# Store the player's inital position in a variable
playerXPosition = 100
playerYPosition = (screen_height/2) - image_height

# Store the enemies' positions
enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0,screen_height - enemy1_height)

enemy2XPosition =  random.randint(0, screen_width - enemy2_width)
enemy2YPosition =  0 - enemy2_height

enemy3XPosition =  screen_width
enemy3YPosition =  random.randint(0, screen_height - enemy3_height)

#======================================================================#

# Create boolean values for the up,down,left,right arrows keys
keyUp= False
keyDown = False
keyLeft =False
keyRight =False

#======================================================================#

# Event Loop
while 1:
    # Clear screen, render player and enemy objects and update screen
    screen.fill(0) 
    
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    
    pygame.display.flip()

    # This loops through events in the game
   
   #======================================================================#
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        
        # This event checks if the key is  presserd and if the keys pressed are the up,down,left or right arrow key.
       
        if event.type == pygame.KEYDOWN:
           
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        # This event checks if the key is not pressed and if the keys pressed are the up,down,left or right arrow key.
        
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False  
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
        
    #======================================================================#

    # Player is moved according to the key pressed making sure the player does not move past the window

    if keyUp == True:
        if playerYPosition > 0 : 
            playerYPosition -= 1
    
    if keyDown == True:
        if playerYPosition < screen_height - image_height:
            playerYPosition += 1
      
    if keyLeft == True:
        if playerXPosition > 0 : 
            playerXPosition -= 1
    
    if keyRight == True:
        if playerXPosition < screen_width - image_width:
            playerXPosition += 1
    
    #======================================================================#

    # Create Bounding box for the player and enemies and update Box position :

    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    #======================================================================#
    
    # If player and enemy collide, display losing status and quit game
    
    if playerBox.colliderect(enemy1Box):
        print("You lose!")
        pygame.quit()
        exit(0)

    elif playerBox.colliderect(enemy2Box):
        print("You lose!")
        pygame.quit()
        exit(0)

    elif playerBox.colliderect(enemy3Box):      
        print("You lose!")       
        pygame.quit()
        exit(0)

    #======================================================================#

    # If enemies are off the screen the user wins the game
    
    if (enemy1XPosition < 0 - enemy1_width) and (enemy2YPosition > screen_height) and (enemy3XPosition < 0 - enemy3_width):
       
        print("You win!")
        pygame.quit()
        exit(0)
    
    #======================================================================#
    
    # Make enemies approach the player.
    enemy1XPosition -= 0.15
    enemy2YPosition += 0.2
    enemy3XPosition -= 0.25
   

