#test how dinosaur works
import modules
while True:
	change_hat(Hats.Dinosaur_Hat)
	while True:
		next_x, next_y = measure()
		quick_print(next_x, next_y)
		if modules.position(next_x, next_y) == False:
			break
	change_hat(Hats.Brown_Hat)
