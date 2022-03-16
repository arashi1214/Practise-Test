#太空戰機
#引入pygame 跟亂數
import pygame
import random

width = 360
height = 480
fps = 30

#define colers 定義顏色之後就可以直接呼叫
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height)) #畫面的長寬 
pygame.display.set_caption("My Game") #遊戲名
clock = pygame.time.Clock() #遊戲時間

#game loop
running = True
while running:
	# keep loop running at the right speed 維持均速
	clock.tick(fps)
	#Process input(events)
	for event in pygame.event.get():
		# check for closing window 檢查有沒有關掉遊戲
		if event.type == pygame.QUIT:
			running = False

	#Update

	#Draw / render
	screen.fill(black) #背景底色
	# after drawing eyething, flip the display 在畫出任何東西之後，跳出這個顯示
	pygame.display.flip()

pygame.quit()