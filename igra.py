import pygame as p, random as r

play=True
dead = True

win=p.display.set_mode((288, 512))
bgimg = p.image.load('fon.png')

groundimg = p.image.load('zemlya.png')
truba = [p.image.load('truba1.png'),
		p.image.load('truba2.png')]
nums = [p.image.load('0.png'),
		p.image.load('1.png'),
		p.image.load('2.png'),
		p.image.load('3.png'),
		p.image.load('4.png'),
		p.image.load('5.png'),
		p.image.load('6.png'),
		p.image.load('7.png'),
		p.image.load('8.png'),
		p.image.load('9.png')]
		
birds = [p.image.load('birddown.png'),
		p.image.load('birdup.png')]


class tbird:
	def __init__(self):
		self.scores = 0
		self.x = 96
		self.y = 230
		self.fall_speed = 0
		self.img = birds[1]
		
	def draw(self):
		win.blit(self.img, (95, self.y))
	
	def jump(self):
		self.fall_speed = -5
		
	def gravity(self):
		self.fall_speed += 0.25
		self.y += self.fall_speed
		if self.fall_speed < 0:
			self.img = birds[0]
		else:
			self.img = birds[1]
			
		
class trub:
	def __init__(self):
		self.x = 288
		self.y = r.randint(180, 400)
		self.distance = r.randint(75,110)
		self.img1 = truba[0]
		self.img2 = truba[1]
		
	def draw(self):
		win.blit(self.img1, (self.x, self.y))
		win.blit(self.img2, (self.x, self.y-self.distance-320))
	
	def control(self):
		self.x = self.x - 0.75
		
	def vasya(self, base):
		if base.x == self.x:
			bird.scores = bird.scores+1
			print(bird.scores)
			
		if self.x+5 < base.x+base.img.get_rect().size[0] and self.y+7 < base.y+base.img.get_rect().size[1] and self.x+self.img1.get_rect().size[0]-5 > base.x:
			return True
			
		elif self.x+5 < base.x+base.img.get_rect().size[0] and self.y-self.distance-7 > base.y  and self.x+self.img2.get_rect().size[0]-5 > base.x:
			return True
			
		else:
			return False
			
class tbg:
	def __init__(self):
		self.x1 = 0
		self.x2 = 0
	def draw1(self):
		win.blit(bgimg, (self.x1, 0))	
		win.blit(bgimg, (self.x1+288, 0))
		
	def draw2(self):
		win.blit(groundimg, (self.x2, 436))
		win.blit(groundimg, (self.x2+288, 436))
		
	def control(self):
		self.x1 = self.x1-0.5
		if self.x1 == -288:
			self.x1 = 0
			
		self.x2 = self.x2-1
		if self.x2 == -288:
			self.x2 = 0
		
		
bird = tbird()
bird.jump()
trubs = []
back = tbg()
trubs.append(trub())

while play == True:
	for event in p.event.get():
		if event.type == p.QUIT:
			play = False
		
		if event.type == p.KEYDOWN:
			if dead == False:
				bird.jump()
			else:
				dead = False
				bird.jump()
				trubs = [trub()]
			
	back.draw1()
	back.control()
	if dead == False:	
		bird.gravity()
	
		for i in trubs:
			i.control()
			i.draw()
			if i.x == 165:
				trubs.append(trub())
		
		if i.x == 80:
			scores = scores+1

			
	for i in trubs:
		if i.x == -75:
			trubs.remove(i)

		if i.vasya(bird) == True:
			dead = True
			bird.scores = 0
			bird.x = 96
			bird.y = 230
			bird.fall_speed = 0

	if bird.y>420:
			dead = True
			bird.scores = 0
			bird.x = 96
			bird.y = 230
			bird.fall_speed = 0
		
	for i in range(len(str(bird.scores))):
		win.blit(nums[int(str(bird.scores)[i])], (10+20*i, 10))
	print(bird.scores)
	bird.draw()
	back.draw2()
	
	p.display.update()
	p.time.delay(7)
