# The Farmer Was Replaced
My collection of drone scripts, experiments, and automation ideas for the game **The Farmer Was Replaced**.


## About the Game  
**The Farmer Was Replaced** is a simulation/automation game where you program a drone to manage a farm — planting, harvesting, watering, and upgrading technology.  
The in-game language is Python-like (but not full Python). You unlock more functions and resources as you progress.


## Project Overview

### `main.py`
The **central control script** that launches and manages all active drones on the farm.  
It coordinates parallel tasks across different regions, allowing full multi-drone automation.

**Key functions:**
- Initializes the world and returns the drone to the starting position.  
- Spawns multiple specialized drones, each handling a specific area or task:
  - `maze_drone(13, 3, 6)` – explores the maze and collects treasures.  
  - `cactus_drone(10, 6, 8, 6)` – manages cactus planting and sorting.  
  - `sunflower_drone(8, 0, 16, 2)` – handles sunflower measurement and harvesting.  
  - `fertilize_drone(10, 14, 2, 6)` – fertilizes designated grass zones.  
  - `carrots_drone(6, 0, 16, 2)` – plants and harvests carrots.    
  - `trees_drone(0, 6, 10, 6)` – plants and maintains tree rows.  
  - `pumpkin_drone2(0, 0, 6, 6)` – manages pumpkin fields in the starting zone.

All the drone logic is defined inside `modules.py`, making each drone function **fully reusable and coordinate-independent**.


### 'modules.py'
A bunch of **utility and movement functions** i wrote for the game.  
It defines reusable functions for positioning, scanning, sorting, and resource-specific logic.

**Main categories:**
- **Positioning**
  - `start_position()` – moves the drone to (0, 0)  
  - `position(x, y)` – safely moves to any coordinates (I unlocked this later in the game - that's why 2 different functions) 
- **Carrots**
  - `harvest_and_carrots()` – auto-harvest and replant routine
- **Maze & Treasure**
  - Pathfinding algorithms for maze treasure hunts  
  - Experimental **multi-drone** setup (`maze_drone()`, `reverse_maze_drone()`)    
- **Cacti**
  - `cactus_drone(x, y, c, r)` – plants and sorts cacti by measured size in a defined grid.  
  - `cactus(start_x, start_y, c, r, i)` – internal cactus comparison and swap logic.
- **Pumpkins**
  - `pumpkin_drone2(x, y, c, r)` – improved pumpkin-farming drone that tracks growth states, waits for maturity, and re-plants until all are fully grown. 
- **Sunflowers**
  - `sunflower_drone(x, y, c, r)` – plants sunflowers, measures them, and harvests the largest ones.  
  - `set_sunflower_list()` / `harvest_sunflower()` – support functions for tracking and selecting sunflowers by petal count.
- **Fertilizer**
  - `fertilize_drone(x, y, c, r)` – plants grass and applies fertilizer across a defined area.
- **Trees**
  - `trees_drone(x, y, c, r)` – alternates tree planting in a checkerboard pattern.

#### Overview
All drones are designed to be spawned from `main.py` via `spawn_drone()`, allowing for **parallel multitasking** across different areas of the farm.  
The file acts as the **core logic library**: every movement, planting, or harvesting routine is encapsulated and reusable by any drone.


### 'old_main.py'
The **main control script** that manages all farming routines.  
It defines the global farm cycle — planting, harvesting, and resource rotation across multiple crop zones.

**Key features:**
- Initializes and tracks grid-based lists for pumpkins, sunflowers, and cacti  
- Handles full planting loops for different regions of the farm:
  - **Pumpkins** – checks grid completion and harvest conditions  
  - **Trees & Grass** – alternates planting for trees requirements  
  - **Carrots** – uses helper logic from `modules.harvest_and_carrots()`  
  - **Sunflowers** – records and harvests based on measured petal counts  
  - **Cactus area** – runs a sorting routine for efficient swapping  
- Integrates multiple helper modules for movement, measurements, and harvesting  
- Resets the drone to the starting position each cycle


### Rest of the Scripts
These are **experimental scripts**, each performing a **single specific task** (as indicated by their file names) across the entire farm.  
I use them whenever I need to quickly gather or produce a particular resource.


## Ideas & Next Steps
- ~~Rewrite `main.py` to fully support **multi-drone farming**.~~
- ~~Move all drone-related functions into `modules.py`, making them **coordinate-independent** and reusable in any context.~~  
- ~~Unlock and integrate **bones** as a new gameplay mechanic or resource.~~
- Perfect a function to farm bones.
- Add polyculture.
