
# Conway's Game of Life Simulation

This repository contains a Python implementation of Conway's Game of Life using Pygame for visualization and basic game logic functions.

### Part 1: Game of Life Simulation Using Pygame

This script simulates Conway's Game of Life, a cellular automaton devised by the mathematician John Conway. It utilizes Pygame for graphical display and user interaction. The game grid is displayed on an 800x800 pixel window, with each cell represented as a square tile. Users can interact with the grid by clicking to toggle cells on and off, and can control the simulation using spacebar to play/pause and 'c' to clear the grid. Additionally, pressing 'g' generates a random initial configuration.

### Part 2: Game of Life Simulation Logic

This part provides the core logic behind the Game of Life simulation. It includes functions to count live neighbors around each cell and determine the next state of cells based on the rules of the game. Two evolution methods are implemented: one with fixed boundaries and another without boundaries, allowing for different simulation behaviors.

### Usage

1. **Setup**: Ensure you have Python and Pygame installed on your system.
   
2. **Running the Simulation**:
   - Run `main.py` to start the Pygame window and initialize the simulation.
   - Click on cells to toggle them on/off.
   - Press spacebar to start/pause the simulation.
   - Press 'c' to clear the grid.
   - Press 'g' to generate a random initial configuration.

3. **Simulation Logic**:
   - The logic in `evolve_with_boundary` and `evolve_without_boundary` functions governs the rules of the Game of Life and can be modified for custom simulations.

### About Conway's Game of Life

Conway's Game of Life is a classic example of cellular automaton, where simple rules lead to complex behaviors and patterns. It is widely studied in the fields of mathematics and computer science for its emergence of patterns resembling biological systems.

