import modules
modules.start_position()
while True:
	harvest()
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	#drone = spawn_drone(modules.reverse_maze_drone)
	modules.harvest_treasure()

	