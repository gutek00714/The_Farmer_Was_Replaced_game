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

#PUMPKINS
def set_list_position(list):
	x = get_pos_x()
	y = get_pos_y()
	list[x][y] = get_entity_type()
	
def list_check(list):
	for i in range(len(list)):
		if Entities.Dead_Pumpkin in list[i]:
			return False
		elif None in list[i]:
			return False
	return True

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

#CACTUS MEASURE + SORT		
def measure_cactus():
	x = measure()
	n = measure(North)
	w = measure(West)
	s = measure(South)
	e = measure(East)
	quick_print(x, n, w, s, e)
	if n != None and x > n:
		swap(North)
	elif w != None and x < w:
		swap(West)
	elif s != None and x < s:
		swap(South)
	elif e != None and x > e:
		swap(East)
		
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

def cactus():
	for x in range (5):
		for y in range(8):
			position(x+11, y + 6)
			m = measure()
			if y < 7:
				n = measure(North)
			else:
				n = 999
				
			if x < 4:
				e = measure(East)
			else:
				e = 999
				
			if m > n and n <= e:
				swap(North)
			elif m > e:
				swap(East)

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
def cactus_drone():
	change_hat(Hats.Cactus_Hat)
	while True:
		x = 11
		position(x, 6)
		for i in range(5):
			for j in range(8):
				harvest()
				if get_ground_type() == Grounds.Grassland:
					till()
				plant(Entities.Cactus)
				move(North)
			x += 1
			position(x, 6)
		position(x, 6)
		for i in range(7):
			cactus()