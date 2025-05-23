import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Geometry Dash")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
player_size = 75
player_x = 100
player_y = SCREEN_HEIGHT - player_size
player_y_velocity = 0
gravity = 1
jump_strength = -17
is_jumping = False
jump_increase = -5

# Load player image (dragon)
player_image = pygame.image.load('assets/dragon.png')
player_image = pygame.transform.scale(player_image, (player_size, player_size))

# Obstacle settings
obstacle_width = 50
obstacle_height = 25 
obstacle_x = SCREEN_WIDTH
obstacle_velocity = 10

obstacle_image = pygame.image.load('assets/brick_wall.png')
obstacle_image = pygame.transform.scale(obstacle_image, (obstacle_width, obstacle_height))

# Game settings
clock = pygame.time.Clock()
FPS = 30
running = True
score = 0

# Font settings for score display
font = pygame.font.Font(None, 36)

# Load and play background music
pygame.mixer.music.load('assets/KPOP5.0.wav')  # Replace with your music file
pygame.mixer.music.play(-1)  # Play the music in a loop

# Load background image
background_image = pygame.image.load('assets/forest_background.png')  # Replace with your image file
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Main game loop
while running:
    screen.blit(background_image, (0, 0))  # Draw the background image	
    #screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        player_y_velocity = jump_strength
        is_jumping = True

    # Update player position
    player_y_velocity += gravity
    player_y += player_y_velocity
    if player_y > SCREEN_HEIGHT - player_size:
        player_y = SCREEN_HEIGHT - player_size
        is_jumping = False

    # Draw player
    screen.blit(player_image, (player_x, player_y))
    #pygame.draw.rect(screen, BLACK, (player_x, player_y, player_size, player_size))

    # Update obstacle position
    obstacle_x -= obstacle_velocity
    if obstacle_x < -obstacle_width:
        obstacle_x = SCREEN_WIDTH
        obstacle_height = random.randint(25,100)
        obstacle_image = pygame.transform.scale(obstacle_image, (obstacle_width, obstacle_height))
        score += 1

    # Draw obstacle
    screen.blit(obstacle_image, (obstacle_x, SCREEN_HEIGHT - obstacle_height))
    #pygame.draw.rect(screen, RED, (obstacle_x, SCREEN_HEIGHT - obstacle_height, obstacle_width, obstacle_height))

    # Check for collision
    if player_x + player_size > obstacle_x and player_x < obstacle_x + obstacle_width:
        if player_y + player_size > SCREEN_HEIGHT - obstacle_height:
            print("Game Over")
            running = False

    #Display the score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (SCREEN_WIDTH - 150, 10))

    # Update the display
    pygame.display.update()
    clock.tick(FPS)

pygame.mixer.music.stop()
pygame.quit()

