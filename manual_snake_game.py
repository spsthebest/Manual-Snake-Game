import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 400
dimen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SSSSSNAKE!!!")

# Define colors
snake_color = (0, 128, 0)  # Green
gameover_color = (255, 0, 0)  # Red
bgcolor = (147, 151, 153)  # Gray
food_color = (255, 121, 0)  # Orange

# Set up game variables
snake_block = 10
snake_speed = 15
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)

# Function to display messages on the screen
def message(msg, color):
    Mesg = font_style.render(msg, True, color)  # Render the message with the specified color
    dimen.blit(Mesg, [width / 6, height / 3])  # Blit the message to the screen

# Function to draw the snake on the screen
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dimen, snake_color, [x[0], x[1], snake_block, snake_block])  # Draw each block of the snake

# Main game loop
def gameloop():
    game_over = False
    game_close = False

    # Initialize the position of the snake
    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Randomly place the first food
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dimen.fill(bgcolor)  # Fill the screen with background color
            message("You lost! Press C to play again or Q to quit", gameover_color)  # Display game over message
            pygame.display.update()  # Update the screen

            for event in pygame.event.get():  # Check for key events
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Quit the game
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # Restart the game
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Close the window
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # Move left
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:  # Move right
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:  # Move up
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:  # Move down
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True  # End the game if the snake hits the wall

        x1 += x1_change  # Update snake's x position
        y1 += y1_change  # Update snake's y position
        dimen.fill(bgcolor)  # Fill the screen with background color
        pygame.draw.rect(dimen, food_color, [foodx, foody, snake_block, snake_block])  # Draw the food
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)  # Update snake's position

        if len(snake_List) > Length_of_snake:
            del snake_List[0]  # Remove the oldest block of the snake

        for x in snake_List[:-1]:  # Check if the snake collides with itself
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)  # Draw the snake
        pygame.display.update()  # Update the screen

        if x1 == foodx and y1 == foody:  # Check if the snake has eaten the food
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0  # Generate new food position
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1  # Increase the length of the snake

        clock.tick(snake_speed)  # Control the speed of the game

    pygame.quit()  # Quit Pygame
    quit()  # Exit the program

# Start the game loop
gameloop()
