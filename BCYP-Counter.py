'''	This program is a counter in days, hours, minutes, and econds
	until the the first day of the 89th session of the British Columbia Youth Parliament on December 27th 2017
	
	Date Set on line 51
	
	Author: Rebecca Louie
	Date  : December 13th 2017
'''
from datetime import datetime, time
import pygame

def dDS(date1, date2):
	'''Date difference in seconds'''
	timedelta = date2 - date1
	return timedelta.days * 24 * 3600 + timedelta.seconds

def TIME(seconds):
	'''daysHoursMinutesSecondsFromSeconds'''
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)

def frame():
	'''Draws a frame'''
	pygame.draw.line(screen,BLACK,(0,0),(0,700),50)
	pygame.draw.line(screen,BLACK,(0,0),(700,0),50)
	pygame.draw.line(screen,BLACK,(700,0),(700,700),50)
	pygame.draw.line(screen,BLACK,(0,700),(700,700),50)
	pygame.draw.line(screen,WHITE,(10,10),(10,690),4)
	pygame.draw.line(screen,WHITE,(10,10),(690,10),4)
	pygame.draw.line(screen,WHITE,(690,10),(690,690),4)
	pygame.draw.line(screen,WHITE,(10,690),(690,690),4)

class Background(pygame.sprite.Sprite):
	def __init__(self, image_file, location):
		pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
		self.image = pygame.image.load('BCYP-Logo.jpg')
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location

pygame.init()
done=False
# Set the height and width of the screen
size = [700, 700]
screen = pygame.display.set_mode(size)

#Colours
WHITE=(255,255,255)
BLACK=(0,0,0)
pygame.display.set_caption("89th BCYP Countdown")
font = pygame.font.Font(None, 35)

BackGround = Background('background_image.png', [0,0]) #Calls background

DATE='2017-12-27 01:00:00'
leaving_date = datetime.strptime(DATE, '%Y-%m-%d %H:%M:%S')
now = datetime.now()

while not done:
	for event in pygame.event.get():  		# User did something
		if event.type == pygame.QUIT:  		# If user clicked close
			done = True  # Flag that we are done so we exit this loop
	screen.fill(WHITE) #Sets screen background
	screen.blit(BackGround.image, BackGround.rect) #Call background image
	frame() #Draws frame with the func. frame
	#clock.tick(frame_rate)
	now = datetime.now()
	output_string=("%d days, %d hours, %d minutes, %d seconds" % TIME(dDS(now, leaving_date)))
	text = font.render(output_string, True, BLACK)
	screen.blit(text, [110,625])
	pygame.display.flip()
