import pygame

pygame.init()

# Set up the display
win = pygame.display.set_mode((500, 500))

# Set up the car
car = pygame.image.load('car.png')
car_x = 250
car_y = 400

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= 5
    elif keys[pygame.K_RIGHT]:
        car_x += 5

    # Update the display
    win.fill((255, 255, 255))
    win.blit(car, (car_x, car_y))
    pygame.display.update()

    # Set the frame rate
    pygame.time.Clock().tick(60)
