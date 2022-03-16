import pygame
import random
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

width = 800
height = 500
fps = 30
x = 400 #兔子初始位置
speed = 0
rock_stary = 0 #石頭初始位置
rock_starx = random.randint(0,724)
time = 0 #躲過石頭的次數
rock_speed = 1 #石頭的加速度
sc = 0 #得分

correct_stary = 0#蘿蔔初始位置
correct_starx = random.randint(0,724)

screen = pygame.display.set_mode((width, height)) #畫面的長寬 
pygame.display.set_caption("Rabbit running") #遊戲名
clock = pygame.time.Clock() #一秒鐘跑幾次loop

#載入圖片
rabbit = pygame.image.load('rabbit.jpg')  #引入兔子圖片  76 * 57
correct = pygame.image.load('correct.jpg')  #引入蘿蔔圖片  76 * 57
rock = pygame.image.load('rock.jpg')  #引入石頭圖片  76 * 57


running = True
def gameloop():
	# keep loop running at t he right speed 維持均速
	global x, speed, rock_stary, correct_stary, rock_speed, sc

	clock.tick(fps)

	
	screen.fill(white) #背景底色
	screen.blit(rabbit,(x, 400))
	screen.blit(rock,(rock_starx,rock_stary))
	screen.blit(correct,(correct_starx,correct_stary))

	pygame.display.flip()

	#判斷按鍵有沒有按下
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				speed = -7
			elif event.key == pygame.K_RIGHT:
				speed = 7
		elif event.type == pygame.KEYUP:
			speed = 0

	#判斷兔子的移動
	if x + 76 < 0:
		x = width
	elif x > width:
		x = 0 - 76
	x = x + speed
	screen.blit(rabbit,(x, 400))
	# 判斷石頭跟蘿蔔的下落
	rock_stary += rock_speed
	correct_stary +=1

	#判斷碰撞
	if 	correct_stary + 57 >= 400 and correct_stary + 57 <= 457 and correct_starx >= x and correct_starx <= x+75 and correct_starx + 75 <= x + 75 and correct_starx + 75 > x:
		sc = sc + 1
		correct_stary = height + 1
		print(sc)
	if 	rock_stary + 57 >= 400 and rock_stary + 57 <= 457 and rock_starx >= x and rock_starx <= x+75 and rock_starx + 75 <= x + 75 and rock_starx + 75 > x:
		#gameover
		pass

	screen.blit(rock,(rock_starx,rock_stary))	
	screen.blit(correct,(correct_starx,correct_stary))

def pygamequit():
	quit()

while running:
	if rock_stary > height:
		rock_starx = random.randint(0,800)
		rock_stary = 0
		time += 1
		if rock_speed <= 13:
			rock_speed += 1
		else:
			rock_speed = 13
	if correct_stary > height:
		correct_starx = random.randint(0,800)
		correct_stary = 0
	gameloop()