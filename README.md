# The Farmer Was Replaced
My collection of drone scripts, experiments, and automation ideas for the game **The Farmer Was Replaced**.


## About the Game  
**The Farmer Was Replaced** is a simulation/automation game where you program a drone to manage a farm — planting, harvesting, watering, and upgrading technology.  
The in-game language is Python-like (but not full Python). You unlock more functions and resources as you progress.


## Project Overview

### 'modules.py'
A bunch of **utility and movement functions** i wrote for the game.  
It defines reusable functions for positioning, scanning, sorting, and resource-specific logic.

**Main categories:**
- **Positioning**
  - `start_position()` – moves the drone to (0, 0)  
  - `position(x, y)` – safely moves to any coordinates (I unlocked this later in the game - that's why 2 different functions)
- **Pumpkins**
  - `set_list_position()` and `list_check()` – track pumpkin growth states  
- **Carrots**
  - `harvest_and_carrots()` – auto-harvest and replant routine  
- **Sunflowers**
  - Tracks sunflowers and selects the largest by petal count for harvesting  
- **Cacti**
  - `cactus()` and `measure_cactus()` – compare and swap cacti based on size measurements  
- **Maze & Treasure**
  - Pathfinding algorithms for maze treasure hunts  
  - Experimental **multi-drone** setup (`maze_drone()`, `reverse_maze_drone()`)  
- **Drone Logic**
  - Functions for multi-drone farming and multitasking automation 


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
- Rewrite `main.py` to fully support **multi-drone farming**.  
- Move all drone-related functions into `modules.py`, making them **coordinate-independent** and reusable in any context.  
- Unlock and integrate **bones** as a new gameplay mechanic or resource.
