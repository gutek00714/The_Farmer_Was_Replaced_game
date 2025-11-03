
while get_pos_x() != 0:
	move(West)
while get_pos_y() != 0:
	move(South)
list = [[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0]]

def harvest_and_carrots():
	if can_harvest():
		harvest()
	if get_ground_type() == Grounds.Grassland:
		till()
	plant(Entities.Carrot)
	
def list_check():
	for i in range(len(list)):
		if Entities.Dead_Pumpkin in list[i]:
			return False
		elif None in list[i]:
			return False
	return True
		
def set_list_position():
	x = get_pos_x()
	y = get_pos_y()
	list[x][y] = get_entity_type()
	
def init_list():
	list = [[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0]]
	
while True:
	while True: #plant
		while True:
			if get_pos_x() < 6 and get_pos_y() < 6:
				set_list_position()
				if get_ground_type() == Grounds.Grassland:
					till()
				plant(Entities.Pumpkin)
			else:
				harvest_and_carrots()
			if get_pos_y() == get_world_size() -1:
				break
			move(North)
		if get_pos_x() == get_world_size() -1:
			break
		move(North)
		move(East)
	move(North)
	move(East)
	if list_check():
		quick_print(list)
		harvest()
		init_list()
	