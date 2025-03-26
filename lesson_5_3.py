# import pygame
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# t = 0
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if pygame.time.get_ticks() - t > 2000:
#             print("Час іде...")
#             t = pygame.time.get_ticks() 

import pygame
import random
pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BG_1 = (79,159,135)
BG_2 = (224,182,100)
BG_3 = (141,137,62)

x,y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
RADIUS = 30
RADIUS_M = 20
RADIUS_S = 10
font = pygame.font.SysFont("Arial", 30)
start_time = pygame.time.get_ticks()
last_move_time = 0
MOVE_INTERVAL = 1000
score = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance = ((mouse_x -x)**2 + (mouse_y -y)**2)**0.5
            if distance <= RADIUS:
                score+=1
                print("Є влучання!")
    current_time = pygame.time.get_ticks()
    if current_time - last_move_time >= MOVE_INTERVAL:
        x,y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
        last_move_time = current_time
    screen.fill(WHITE)
    if score == 5:
        screen.fill(BG_1)
    elif score == 10:
        screen.fill(BG_2)
    elif score == 15:
        screen.fill(BG_3)
    pygame.draw.circle(screen, RED, (x,y), RADIUS)
    pygame.draw.circle(screen,  WHITE, (x,y), RADIUS_M)
    pygame.draw.circle(screen,  RED, (x,y), RADIUS_S)
    score_text =  font.render(f"Влучань: {score}", True, (0,0,0))
    screen.blit(score_text, (10,10))
    elapsed_time = (current_time - start_time)//1000
    time_text = font.render(f"Час: {elapsed_time} c", True, (0,0,0))
    screen.blit(time_text, (10,40))
    pygame.draw.rect(screen, (0, 255, 0), (0,0,500,500), 10)
    pygame.display.flip()
pygame.quit()