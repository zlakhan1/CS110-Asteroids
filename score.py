import os 
import json 

class score():
	def __init__(self):
		'''Initalizes the players score to 0''' 
		self.score = 0 
	def points(self, amnt):
		'''Increases the score by some amount'''
		self.score += amnt 
	def player(self):
		'''Generates a dictonary with the high scores if a file is not found one is created'''
		data = {} 
		while True:
			name = input("What is your name") 
			score = self.score 
			if name.isdigit():
				print("numbers are not allowed") 
			else:
				break
		try:
			fptr = open("scores", "r")  
			a = fptr.read()
		except:
			fptr = open("scores" , 'w') 
		try:
			data = json.loads(a)
		except:
			fptr.close() 
			fptr = open("scores", "w") 
			data[name] = (score)  	 
			datastr = json.dumps(data) 
			fptr.write(datastr) 
 
		fptr.close() 
		fptr = open("scores", "w") 
		data[name] = (score)  	 
		datastr = json.dumps(data) 
		fptr.write(datastr) 
		highscore = max(data, key=data.get) 
		message = [highscore,data[name]] 
		fptr.close()
		return message 

