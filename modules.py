#POSITIONS
def start_position():
	while get_pos_x() != 0:
		move(West)
	while get_pos_y() != 0:
		move(South)

def position(x, y):
	w = get_world_size()
	x = max(0, min(x, w-1))
	y = max(0, min(y, w-1)) 
	while True:
		if get_pos_x() > x:
			move(West)
		elif get_pos_x() < x:
			move(East)
		else:
			break
	while True:
		if get_pos_y() > y:
			move(South)
		elif get_pos_y() < y:
			move(North)
		else:
			break

#OLD
# #PUMPKINS
# def set_list_position(list):
# 	x = get_pos_x()
# 	y = get_pos_y()
# 	list[x][y] = get_entity_type()
	
# def list_check(list):
# 	for i in range(len(list)):
# 		if Entities.Dead_Pumpkin in list[i]:
# 			return False
# 		elif None in list[i]:
# 			return False
# 	return True

#CARROTS
def harvest_and_carrots():
	if can_harvest():
		harvest()
	if get_ground_type() == Grounds.Grassland:
		till()
	plant(Entities.Carrot)

#MAZE TREASURE + MOVEMENT
def harvest_treasure():
	#position_list = []
	treasure_x, treasure_y = measure()
	quick_print(treasure_x, treasure_y)
	direction = North
	while get_pos_x() != treasure_x or get_pos_y() != treasure_y:
		#if get_pos_x() and get_pos_y() not in position_list:
			#position_list.append({'x': get_pos_x(), 'y': get_pos_y()})
		left_direction = turn_left(direction)
		if can_move(left_direction):
			move(left_direction)
			direction = left_direction
		elif can_move(direction):
			move(direction)
		else:
			direction = turn_right(direction)
			
	harvest()

def turn_left(direction):
	if direction == North:
		return West
	elif direction == West:
		return South
	elif direction == South:
		return East
	elif direction == East:
		return North
		
def turn_right(direction):
	if direction == North:
		return East
	elif direction == East:
		return South
	elif direction == South:
		return West
	elif direction == West:
		return North

#OLD
# #CACTUS MEASURE + SORT		
# def measure_cactus():
# 	x = measure()
# 	n = measure(North)
# 	w = measure(West)
# 	s = measure(South)
# 	e = measure(East)
# 	quick_print(x, n, w, s, e)
# 	if n != None and x > n:
# 		swap(North)
# 	elif w != None and x < w:
# 		swap(West)
# 	elif s != None and x < s:
# 		swap(South)
# 	elif e != None and x > e:
# 		swap(East)
		
#def cactus():
#	for x in range(5):
#		for y in range(8):
#			position(x + 11, y + 6)
#			m = measure(East)
#			if m != None:
#				if measure() > m:
#					swap(East)
#	for y in range(8):
#		for x in range():
#			position(x + 11, y + 6)
#			n = measure(South)
#			if n != None:
#				if measure() < n:
#					swap(South)

#REVERSED DRONE FUNCTION - I TRIED TO HAVE 2 DRONES LOOKING FOR TREASURE IN THE SAME TIME
def reverse_maze_drone():
	#position_list = []
	change_hat(Hats.Green_Hat)
	treasure_x, treasure_y = measure()
	quick_print(treasure_x, treasure_y)
	direction = North
	while get_pos_x() != treasure_x or get_pos_y() != treasure_y:
		#if get_pos_x() and get_pos_y() not in position_list:
			#position_list.append({'x': get_pos_x(), 'y': get_pos_y()})
		right_direction = turn_right(direction)
		if can_move(right_direction):
			move(right_direction)
			direction = right_direction
		elif can_move(direction):
			move(direction)
		else:
			direction = turn_left(direction)
			
	harvest()

#DRONE MAZE - JUST UNLOCKED MORE DRONES SO I CAN MULTITASK NOW
#x = position x, y = position y, size = n x n
def maze_drone(x, y, size):
	def inner():
		change_hat(Hats.Purple_Hat)
		
		while True:
			position(x, y)
			harvest()
			plant(Entities.Bush)
			use_item(Items.Weird_Substance, 8* size)
			harvest_treasure()
			#do_a_flip()
	return inner

#DRONE CACTUS
#x2 = position x, y = position y, c = number of cacti in column, r = number of cacti in row
def cactus_drone(x2, y, c, r):
	def inner2():
		change_hat(Hats.Cactus_Hat)
		
		while True:
			for i in range(r):
				for j in range(c):
					position(x2 + i, y + j)
					harvest()
					if get_ground_type() == Grounds.Grassland:
						till()
					plant(Entities.Cactus)
			for i in range(c + r - 1):
				cactus(x2, y, c, r, i)
			do_a_flip()
	return inner2
			
def cactus(start_x, start_y, c, r, i):
	for x in range(r):
		for y in range(c):
			position(x + start_x, y + start_y)
			m = measure()
			if y < c - 1:
				n = measure(North)
			else:
				n = 999
				
			if x < r - 1:
				e = measure(East)
			else:
				e = 999
				
			if m > n and n <= e:
				swap(North)
			elif m > e:
				swap(East)
				
			if x + y >= c + r - i:
				break


#DRONE PUMPKIN
#start_x = position x, start_y = position y, c = number of plants in column, r = number of plants in row
# def pumpkin_drone(start_x, start_y, c, r):
# 	def inner():
# 		pumpkin_list = init_pumpkin_list(c, r)
# 		change_hat(Hats.Pumpkin_Hat)
# 		while True:
# 			x = start_x
# 			#x = 11
# 			position(start_x, y)
# 			for i in range(r):
# 				for j in range(c):
# 					harvest()
# 					if get_ground_type() == Grounds.Grassland:
# 						till()
# 					plant(Entities.Pumpkin)
# 					move(North)
# 				x += 1
# 				position(x, y)
			
# 	return inner	

# def init_pumpkin_list(c, r):
# 	pumpkin_list = []
# 	for i in range(r):
# 		row = [0] * c
# 		pumpkin_list.append(row)
# 	return pumpkin_list

def pumpkin_drone2(start_x, start_y, c, r):
	def inner():
		change_hat(Hats.Pumpkin_Hat)
		while True:
			pumpkin_list = []
			for i in range(r):
				for j in range(c):
					if i % 2 == 0:
						position(start_x + i, start_y + j)
					else:
						position(start_x + i, start_y + (c - 1 - j))
					pumpkin_list.append(get_entity_type())
					harvest()
					if get_ground_type() == Grounds.Grassland:
						till()
					plant(Entities.Pumpkin)
					use_item(Items.Water)

			position(start_x, start_y)
			
			is_done = False
			while not is_done:
				for i in range(r):
					for j in range(c):
						if i % 2 == 0:
							position(start_x + i, start_y + j)
						else:
							position(start_x + i, start_y + (c - 1 - j))
						pumpkin_list.append(get_entity_type())
						plant(Entities.Pumpkin)
					
				position(start_x, start_y)
					
				if Entities.Dead_Pumpkin not in pumpkin_list and Entities.Grass not in pumpkin_list:
					is_done = True
				
				pumpkin_list = []
					
			harvest()
	return inner

#DRONE SUNFLOWERS
#start_x = position x, start_y = position y, c = number of plants in column, r = number of plants in row
def sunflower_drone(start_x, start_y, c, r):
	def inner():
		change_hat(Hats.Sunflower_Hat)
		sunflower_list = []
		list_len = c * r
		while True:
			while len(sunflower_list) != list_len:
				for i in range(r):
					for j in range(c):
						position(start_x + i, start_y + j)
						if get_entity_type() != Entities.Sunflower:
							harvest()
						if get_ground_type() == Grounds.Grassland:
							till()
						if get_entity_type() == None:
							plant(Entities.Sunflower)
							use_item(Items.Water)
						set_sunflower_list(sunflower_list)
			while len(sunflower_list) > 0:
				harvest_sunflower(sunflower_list)
			sunflower_list = []
	return inner

def set_sunflower_list(sunflower_list):
	x = get_pos_x()
	y = get_pos_y()
	sunflower_list.append({'x': get_pos_x(), 'y': get_pos_y(), "petals": measure()})
	#quick_print(sunflower_list)
		
def sunflower_list_check(sunflower_list):
	max_petals = sunflower_list[0]
	for i in sunflower_list:
		if i['petals'] > max_petals['petals']:
			max_petals = i
	return max_petals
	
#def harvest_sunflower(sunflower_list):
#	max_petals = sunflower_list_check(sunflower_list)
#	position(max_petals['x'], max_petals['y'])
#	harvest()
#	sunflower_list.remove(max_petals)

#spawn multiple drones to harvest sunflowers
def harvest_sunflower(sunflower_list):
	max_petals = sunflower_list_check(sunflower_list)
	spawn_drone(i_am_speed(max_petals['x'], max_petals['y']))
	sunflower_list.remove(max_petals)

def i_am_speed(x, y):
	def inner():
		position(x, y)
		harvest()
	return inner
	
#DRONE FERTILIZER
#start_x = position x, start_y = position y, c = number of plants in column, r = number of plants in row
def fertilize_drone(start_x, start_y, c, r):
	def inner():
		change_hat(Hats.Wizard_Hat)
		while True:
			x = start_x
			position(start_x, start_y)
			for i in range(r):
				for j in range(c):
					position(x, start_y + j)
					harvest()
					plant(Entities.Grass)
					use_item(Items.Fertilizer)
				x += 1

	return inner
	
#DRONE CARROTS
#start_x = position x, start_y = position y, c = number of plants in column, r = number of plants in row
def carrots_drone(start_x, start_y, c, r):
	def inner():
		change_hat(Hats.Carrot_Hat)
		while True:
			x = start_x
			position(start_x, start_y)
			for i in range(r):
				for j in range(c):
					position(x, start_y + j)
					if can_harvest():
						harvest()
					if get_ground_type() == Grounds.Grassland:
						till()
					plant(Entities.Carrot)
				x += 1	
	return inner

#FLIP DRONE - achievement
def flip_drone(start_x, start_y):
	def inner():
		change_hat(Hats.Traffic_Cone)
		position(start_x, start_y)
		while True:
			do_a_flip()
	return inner
	
#TREES DRONE
#start_x = position x, start_y = position y, c = number of plants in column, r = number of plants in row
def trees_drone(start_x, start_y, c, r, subst = False):
	def inner():
		change_hat(Hats.Tree_Hat)
		while True:
			x = start_x
			position(start_x, start_y)
			for i in range(r):
				for j in range(c):
					position(x, start_y + j)
					if (get_pos_x() + get_pos_y()) % 2 == 0:
						harvest()
						plant(Entities.Tree)
						use_item(Items.Water)
					elif (get_pos_x() + get_pos_y()) % 2 != 0:
						harvest()
						if subst == True:
							use_item(Items.Fertilizer)
				x += 1	
	return inner

#DINO DRONE
def dino_drone():
	change_hat(Hats.Dinosaur_Hat)
	while True:
		next_x, next_y = measure()
		quick_print(next_x, next_y)
		if position(next_x, next_y) == False:
			break
	change_hat(Hats.Brown_Hat)
	
#HAY DRONE
#start_x = position x, start_y = position y, c = number of plants in column, r = number of plants in row
def hay_drone(start_x, start_y, c, r):
	def inner():
		change_hat(Hats.Straw_Hat)
		while True:
			for i in range(r):
				for j in range(c):
					position(start_x + i, start_y + j)
					if can_harvest():
						harvest()
					plant(Entities.Grass)
	return inner

#SUNFLOWERS DRONE MULTI DRONE PLANT
#start_x = position x, start_y = position y, c = number of plants in column, r = number of plants in row, n = number of drones
def sunflower_drone_main(start_x, start_y, c, r, n = 1):
	def inner():
		change_hat(Hats.Sunflower_Hat)
		position(start_x, start_y)
		while True:
			sunflower_list = []
			divide_field = r // n
			modulo = r % n
			#n = 4 r = 22 positions = 0(+ modulo) 7 12 17
			#spawn new planting drones
			for i in range(n - 1):
				x = start_x + modulo + (i + 1) * divide_field
				spawn_drone(plant_sunflowers(x, start_y, c, divide_field))
			
			#main drone plant
			plant_sunflowers(start_x, start_y, c, divide_field + modulo)()
			
			#main drone make list
			for i in range(r):
				for j in range(c):
					if i % 2 == 0:
						position(start_x + i, start_y + j)
					else:
						position(start_x + i, start_y + (c - 1 - j))
					set_sunflower_list(sunflower_list)
					
			position(start_x, start_y)
			while len(sunflower_list) > 0:
				harvest_sunflower(sunflower_list)
			sunflower_list = []
			do_a_flip()
		
	return inner
	
def plant_sunflowers(start_x, start_y, c, r):
	def inner():
		for i in range(r):
			for j in range(c):
				position(start_x + i, start_y + j)
				if get_entity_type() != Entities.Sunflower:
					harvest()
				if get_ground_type() == Grounds.Grassland:
					till()
				if get_entity_type() == None:
					plant(Entities.Sunflower)
					use_item(Items.Water)
	return inner
