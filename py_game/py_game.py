import pygame
from random import randint

def randcolor():
	return (randint(100,255), randint(100,255),randint(100,255))

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
	if e.type is pygame.MOUSEBUTTONDOWN and e.button == 3:
		windows.append([nwin, randcolor(), pygame.Rect(e.pos, SZ), False])
		nwin += 1
	else:
		for (i, color, rect, flag) in reversed(windows):
			if e.type == pygame.MOUSEBUTTONUP and e.button == 1 and rect.collidepoint(e.pos):
				windows[i][3] = True
				print(f"{e} to {i}")
				break
			elif hasattr(e, "pos") and rect.collidepoint(e.pos):
				print(f"{e} to {i}")
				break
		else:
			print(e)
	screen.fill(0)
	for i, color, rect, flag in windows:
		screen.fill(color, rect)
		if flag:
			pygame.draw.line(screen, (255,0,0), rect[:2], (rect[0]+100, rect[1]+80), 4)

		
	pygame.display.flip()
