import modules
modules.start_position()
while True:
	for i in range(get_world_size()):
		harvest()
		plant(Entities.Grass)
		#use_item(Items.Fertilizer)
		move(North)
	move(East)
