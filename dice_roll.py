#this program will simulate  10 dice rolls
import random
def main():
	intro():
	roll():
def intro():
	print("this program")
	print("will generate")
	print("few")
	print("dice rolls")

def roll():
	for count in range(10):
		a = random.randint(1,6)
		print("first roll is", a)
		b = random.randint(1,6)
		print("second roll is", b)
		c = random.randint(1,6)
		print("third roll is", c)
		d = random.randint(1,6)
		print("fourth roll is", d)
		e = random.randint(1,6)
		print("fifth roll is", e)
		f = random.randint(1,6)
		print("sixth roll is", f)
		g = random.randint(1,6)
		print("seventh roll is", g)
		h = random.randint(1,6)
		print("eighth roll is", h)
		i = random.randint(1,6)
		print("ninth roll is", i)
		j = random.randint(1,6)
		print("tenth roll is", j)
		
main()		