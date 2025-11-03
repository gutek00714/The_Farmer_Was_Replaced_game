while get_pos_x() != 0:
	move(West)
while get_pos_y() != 0:
	move(South)
while True:
	for i in range(get_world_size()):

		if (get_pos_x() + get_pos_y()) % 2 == 0:
			harvest()
			plant(Entities.Tree)
			#use_item(Items.Water)
			move(North)
	
		elif (get_pos_x() + get_pos_y()) % 2 != 0:
			#a = get_entity_type()
			harvest()
			#if get_ground_type() == Grounds.Grassland:
				#till()
			plant(Entities.Grass)
			move(North)
	move(East)
 
		