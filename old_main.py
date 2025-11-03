import modules
#harvest()
modules.start_position()

#pumpkin list
list = [[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0]]

def init_list():
	list = [[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0]]

sunflower_list = []
cactus_list = []

while True:
	while True: #plant
		while True:
			#plant pumpkins
			if get_pos_x() < 6 and get_pos_y() < 6:
				modules.set_list_position(list)
				if get_ground_type() == Grounds.Grassland:
					till()
				plant(Entities.Pumpkin)

				#plant trees and grass in grid
			elif get_pos_x() < 6 and get_pos_y() >= 6:

				if (get_pos_x() + get_pos_y()) % 2 == 0:
					harvest()
					plant(Entities.Tree)
					#use_item(Items.Water)
					#move(North)
	
				elif (get_pos_x() + get_pos_y()) % 2 != 0:
					#a = get_entity_type()
					harvest()
					#if get_ground_type() == Grounds.Grassland:
						#till()
					plant(Entities.Grass)
					#move(North)
				
				#plant carrots
			elif get_pos_x() == 6 or get_pos_x() == 7:
				modules.harvest_and_carrots()
				
				#plant and measure sunflowers
			elif get_pos_x() == 8 or get_pos_x() == 9:
				if get_entity_type() != Entities.Sunflower:
						harvest()
				if get_ground_type() == Grounds.Grassland:
					till()
				if get_entity_type() == None:
					plant(Entities.Sunflower)
					#use_item(Items.Water)
				modules.set_sunflower_list(sunflower_list)
				
				#plant and fertilize grass
			elif get_pos_x() >= 10 and get_pos_y() >= 14:
				harvest()
				plant(Entities.Grass)
				use_item(Items.Fertilizer)
				
				#make maze
			elif get_pos_x() == 13 and get_pos_y() == 3:
				harvest()
				plant(Entities.Bush)
				use_item(Items.Weird_Substance, 6)
				modules.harvest_treasure()
				modules.position(13, 4)
				
				#plant cactus
			elif get_pos_x() >= 11 and get_pos_y() >= 6 and get_pos_x() <= 13 and get_pos_y() <= 8:
				if get_ground_type() == Grounds.Grassland:
					till()
				plant(Entities.Cactus)

			else:
				harvest()
				
				

			if get_pos_y() == get_world_size() -1:
				break
			move(North)
		if get_pos_x() == get_world_size() -1:
			break
		move(North)
		move(East)
	move(North)
	move(East)

	#check and harvest pumpkins
	if modules.list_check(list):
		quick_print(list)
		harvest()
		init_list()

	#harvest 10 biggest sunflowers
	while len(sunflower_list) > 10:
		modules.harvest_sunflower(sunflower_list)
	sunflower_list = []

	#swap and harvest cactus
	modules.position(11, 6)
	for i in range(5):
		modules.cactus()
	harvest()
	modules.start_position()
	