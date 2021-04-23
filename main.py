import random
# Guessing Game
# Rock Paper Scissors
# Dice Roll
# Fortune Teller

def guessingGame():
	# print("This is going to be a Guessing Game")
	# cpu will choose a randon number from 1-10
	cpu = random.randint(1,10)
	# user guesses until they are correct
	user = int(input("Guess what number I am thinking of: "))

	while(cpu != user):
		user = int(input("Try again: "))

	print("You guessed it! Yayyy")


def rockPaperScissors():
	#print("This is going to be a game of Rock Paper Scissors ")

	# cpu and player
	# cpu chooses a random number between 1-3
	# get player choice 
	print("1. Rock")
	print("2. Paper")
	print("3. Scissors")
	cpu = random.randint(1,3)
	user = int(input("Choose your weapon please: "))
	# use nested conditionals
	if(cpu == user): 
		print("Tie game")
	elif(cpu == 1): 
		if(user == 2): 
			print("You won! I chose Rock")
		elif(user == 3): 
			print("You lose! I chose Rock")
	elif(cpu == 2): 
		if(user == 1): 
			print("You lose! I chose Paper")
		elif(user == 3): 
			print("You won! I chose Paper")
	elif(cpu == 3): 
		if(user == 1): 
			print("You won! I chose Scissors")
		elif(user == 2): 
			print("You lose! I chose Scissors")

def diceRoll():
	# print("This is going to be a Dice Roll game")
	print(random.randint(1,6))

def fortuneTeller():
	# print("This is going to be a Fortune Telling game")
	# using a list, add 5 fortunes and randomly choose one to output
	fortuneList = ["You look great today", "You won the lottery", "You will pass your next test", "You are the smartest person ever", "You will survive today"]

	print(fortuneList[random.randint(0, len(fortuneList)-1)])

# 'main' function
# this is where we define how we want our program to run

def main():
	#print("This is the Main Function")

	# Tell the user their game options
	# Ask the user to choose one
	# Call the correct function based on user input
	print("1. Guessing Game")
	print("2. Rock Paper Scissors")
	print("3. Dice Roll")
	print("4. Fortune Teller")
	userInput = int(input("Which game would you like to play - please answer with a number?: "))

	if(userInput == 1):
		guessingGame()
	elif(userInput == 2):
		rockPaperScissors()
	elif(userInput == 3):
		diceRoll()
	elif(userInput == 4):
		fortuneTeller()
	else: # Catch Exceptions
		print("Sorry, Invalid Input")
		main()

guessingGame()
rockPaperScissors()
diceRoll()
fortuneTeller()

# this controls the execution of our code
if __name__ == "__main__":
	main()
