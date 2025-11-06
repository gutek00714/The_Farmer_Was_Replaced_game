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

#SUNFLOWERS
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
	
def harvest_sunflower(sunflower_list):
	max_petals = sunflower_list_check(sunflower_list)
	position(max_petals['x'], max_petals['y'])
	harvest()
	sunflower_list.remove(max_petals)
	#start_position()
		
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
			position(x, y) #13 3 6
			harvest()
			plant(Entities.Bush)
			use_item(Items.Weird_Substance, size)
			harvest_treasure()
	return inner

#DRONE CACTUS
#x2 = position x, y = position y, c = number of cacti in column, r = number of cacti in row
def cactus_drone(x2, y, c, r):
	def inner2():
		#nonlocal x, y
		change_hat(Hats.Cactus_Hat)
		
		while True:
			x = x2
			#x = 11
			position(x2, y)
			for i in range(r):
				for j in range(c):
					harvest()
					if get_ground_type() == Grounds.Grassland:
						till()
					plant(Entities.Cactus)
					move(North)
				x += 1
				position(x, y)
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
#x = position x, y = position y, c = number of pumpkins in column, r = number of pumpkins in row
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
			x = start_x
			position(start_x, start_y)
			for i in range(r):
				for j in range(c):
					pumpkin_list.append(get_entity_type())
					harvest()
					if get_ground_type() == Grounds.Grassland:
						till()
					plant(Entities.Pumpkin)
					use_item(Items.Water)
					move(North)
				x += 1
				position(x, start_y)

			position(start_x, start_y)
			
			is_done = False
			while not is_done:
			
				x = start_x
				for i in range(r):
					for j in range(c):
						pumpkin_list.append(get_entity_type())
						plant(Entities.Pumpkin)
						move(North)
					x += 1
					position(x, start_y)
					
				position(start_x, start_y)
					
				if Entities.Dead_Pumpkin not in pumpkin_list and Entities.Grass not in pumpkin_list:
					is_done = True
				
				pumpkin_list = []
					
			harvest()
			do_a_flip()
	return inner
