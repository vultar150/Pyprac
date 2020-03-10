import sys, pygame
pygame.init()

DX, DY = 0.1, 0.1
size = width, height = 4000, 4000
screen_size = int(width*DX)+1, int(height*DY)+1
speed = [8, 8]

black = 0, 0, 0

screen = pygame.display.set_mode(screen_size)

ball = pygame.image.load("intro_ball.gif")
x, y = width/2, height/2
ballrect = ball.get_rect()
w, h = ballrect.w/DX, ballrect.h/DY
pygame.time.set_timer(pygame.USEREVENT, 50)
pull = False

while 1:
    event = pygame.event.wait()
    if event.type == pygame.QUIT: sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN and ballrect.collidepoint(event.pos):
        pull = ballrect.centerx - event.pos[0], ballrect.centery - event.pos[1]
    elif pull and event.type == pygame.MOUSEMOTION:
        x, y = event.pos[0]/DX + pull[0], event.pos[1]/DY + pull[1]
    elif event.type == pygame.MOUSEBUTTONUP:
        pull = False
    
        
        
    elif event.type == pygame.USEREVENT:
        if not pull:
            if x-w/2 < 0 or x+w/2 > width:
                speed[0] = -speed[0]
            if y-h/2 < 0 or y+h/2 > width:
                speed[1] = -speed[1]
            x += speed[0]
            y += speed[1]
    screen.fill(black)
    ballrect.center = int(x*DX), int(y*DY)
    screen.blit(ball, ballrect)
    pygame.display.flip()
