
def SetBridges(locations):
	for i in range(len(locations)):
		if i == len(locations)-1:
			locations[i].next = locations[0]
			locations[i].previous = locations[i-1]
		elif i == 0:
			locations[i].next = locations[i+1]
			locations[i].previous = locations[len(locations)-1]
		else:
			locations[i].next = locations[i+1]
			locations[i].previous = locations[i-1]






class Location(object):
	"""docstring for Location"""
	def __init__(self, name,countItem, countEnemy, lenght,weight):
		self.name = name
		self.countEnemy = countEnemy
		self.countItem = countItem
		self.lenght = lenght
		self.weight = weight
		self.field = []
		self.next = None
		self.previous = None
		self.positionHero = []
		self.info = 'Проход на локацию '+ str(self.name)

	def CreateField(self):
		self.field = [[0 for i in range(self.weight)]for i in range(self.lenght)]

		self.field[0][int(self.weight/2)] = self.next
		self.field[self.lenght-1][int(self.weight/2)] = self.previous


	def UpdatePositionhero(self, newHeroPosition):
		pass
