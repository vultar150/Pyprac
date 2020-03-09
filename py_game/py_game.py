import pygame
from random import randint

def randcolor():
	return (randint(100,256), randint(100,256),randint(100,256))

pygame.init()
screen = pygame.display.set_mode((800, 600))
 
SZ = 100, 80

timeout = 500
pygame.time.set_timer(pygame.USEREVENT, timeout)
 
windows, nwin = [], 0
while True:
	e = pygame.event.wait()
	if e.type is pygame.QUIT:
		print("QUIT")
		break
	if e.type is pygame.MOUSEBUTTONDOWN:
		if e.button == 3:
			windows.append((nwin, randcolor(), pygame.Rect(e.pos, SZ)))
			nwin += 1
	else:
		for (i, color, rect) in reversed(windows):
			if hasattr(e, "pos") and rect.collidepoint(e.pos):
				print(f"{e} to {i}")
				break
		else:
			print(e)
	screen.fill(0)
	for i, color, rect in windows:
		screen.fill(color, rect)
	pygame.display.flip()
