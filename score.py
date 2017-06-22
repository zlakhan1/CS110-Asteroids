import os 
import json 

class score():
	def __init__(self):
		self.score = 0 
	def points(self, amnt):
		self.score += amnt 
	def player(self):
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
		print("highscore is :", highscore,':',data[name]) 
		fptr.close()
def main():
	person = score() 
	person.points(200)
	person.player()
main() 
