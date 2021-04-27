class Hero(object):
	"""docstring for Hero"""
	def __init__(self):
		self.currentLocation = -1
		self.vision = 2
		self.info = "Себя"
		


	def Move(self, towards):
		move_dict = {'вверх':[-1,0],'вниз':[1,0],'влево':[0,-1],'вправо':[0,1]}
		try:
			cur = move_dict[towards]
		except KeyError as ex:
			cur = [0,0]
			towards = 'на месте'

		cur = [cur[0]+self.currentLocation.positionHero[0], cur[1]+self.currentLocation.positionHero[1]]

		if cur[0] <0 or cur[1]<0 or cur[0]>= len(self.currentLocation.field) or cur[1]>= len(self.currentLocation.field[0])-1:
			return "Вы не можете пройти "+towards

		if type(self.currentLocation.field[cur[0]][cur[1]]) == type(self.currentLocation):
			lastCurrentLocation = self.currentLocation
			self.currentLocation.field[self.currentLocation.positionHero[0]][self.currentLocation.positionHero[1]] = 0
			self.currentLocation.newHeroPosition = [] 
			self.currentLocation = self.currentLocation.field[cur[0]][cur[1]]
			a = FindeInMatrix(self.currentLocation.field, lastCurrentLocation)
			a[1]+=1
			self.currentLocation.positionHero = a
			self.currentLocation.field[self.currentLocation.positionHero[0]][self.currentLocation.positionHero[1]] = self
			return "Вы перешли в другую локацию"

		self.currentLocation.field[cur[0]][cur[1]] = self.currentLocation.field[self.currentLocation.positionHero[0]][self.currentLocation.positionHero[1]]
		self.currentLocation.field[self.currentLocation.positionHero[0]][self.currentLocation.positionHero[1]] = 0
		self.currentLocation.positionHero = [cur[0], cur[1]]
		
		if towards == 'на месте':
			return "Вы стоите " + towards
		else:
			return "Вы идёте "+ towards

	def WhatISee(self):
		curVisionLeft = self.vision
		curVisionRight = self.vision
		curVisionUp = self.vision
		curVisionDown = self.vision
		avalibalCell = []

		if curVisionLeft > self.currentLocation.positionHero[1]:
			curVisionLeft = self.currentLocation.positionHero[1]

		if curVisionUp > self.currentLocation.positionHero[0]:
			curVisionUp = self.currentLocation.positionHero[0]


		if curVisionRight >= len(self.currentLocation.field[0])-1 -self.currentLocation.positionHero[1]:
			curVisionRight = len(self.currentLocation.field[0])-1 -self.currentLocation.positionHero[1]

		if curVisionDown >len(self.currentLocation.field)-1 -self.currentLocation.positionHero[0]:
			curVisionDown = len(self.currentLocation.field)-1 -self.currentLocation.positionHero[0]


		for i in range(self.currentLocation.positionHero[0]-curVisionUp,self.currentLocation.positionHero[0]+curVisionDown+1):
			for j in range(self.currentLocation.positionHero[1]-curVisionLeft,self.currentLocation.positionHero[1]+curVisionRight+1):
				avalibalCell.append([i,j])


		result = []
		for i in range(len(self.currentLocation.field)):
			for j in range(len(self.currentLocation.field[i])):
				if ([i,j] in avalibalCell) and not(self.currentLocation.field[i][j] == 0):
					result.append([i,j,self.currentLocation.field[i][j].info ])

		inp = '''Вы видите:
		'''

		print(result)
		for x in result:
			if x[0] > self.currentLocation.positionHero[0]:
				if x[1]> self.currentLocation.positionHero[1]:
					inp +='снизу справа {'+x[2] +'} '+ '\n'
				elif x[1] == self.currentLocation.positionHero[1]:
					inp +='снизу {'+x[2]+'} '+ '\n'
				else:
					inp +='снизу слева {'+x[2]+'} '+ '\n'


			elif x[0] == self.currentLocation.positionHero[0]:
				if x[1]> self.currentLocation.positionHero[1]:
					inp +='справа {'+x[2]+'} '+ '\n'
				elif x[1] == self.currentLocation.positionHero[1]:
					inp +='{'+x[2]+'} '+ '\n'
				else:
					inp +='слева {'+x[2]+'} '+ '\n'
			else:
				if x[1]> self.currentLocation.positionHero[1]:
					inp +='сверху справа {'+x[2]+'} '+ '\n'
				elif x[1] == self.currentLocation.positionHero[1]:
					inp +='сверху {'+x[2]+'} '+ '\n'
				else:
					inp +='сверху слева {'+x[2]+'} '+ '\n'



		
		return inp




def FindeInMatrix(matrix,el):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] == el:
				return [i,j]