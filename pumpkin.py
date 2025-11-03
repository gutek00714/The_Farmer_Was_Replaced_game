
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

while True:
	while True: #plant
		while True:
			plant(Entities.Pumpkin)
			#print(get_pos_x(), get_pos_y())
			if get_pos_y() == get_world_size() -1:
				break
			move(North)
		if get_pos_x() == get_world_size() -1:
			break
		move(North)
		move(East)
	move(North)
	move(East)
	
	while True: #check list
		while True:
			x = get_pos_x()
			y = get_pos_y()
			list[x][y] = get_entity_type()
			if get_entity_type() == Entities.Dead_Pumpkin:
				harvest()
				plant(Entities.Pumpkin)
			#print(get_pos_x(), get_pos_y())
			if get_pos_y() == get_world_size() -1:
				break
			move(North)
		if get_pos_x() == get_world_size() -1:
			break
		move(North)
		move(East)
	move(North)
	move(East)
	quick_print(list)
	if Entities.Dead_Pumpkin not in list:
		harvest()
	