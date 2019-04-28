#this program will simulate 10 coin tosses
import random
heads=1
tails=2
tosses=10

def main():
	for toss in range(10):
	if random.randint(1,2)==2:
		print("tails")
	else:
		print("heads")
		
main()