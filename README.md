# RoverOlympics
Traxsense Assignment

Steps to run program:
- Clone from repo
- Open in IDE (I used Pycharm)
- Go to 'if __name__ == '__main__':'
- Change input parameters if desired
- Run program

Input Example:

if __name__ == '__main__':

    # Set initial conditions
    input_grid_size = [5, 5]
    input_rover1_start = [0, 2]
    input_rover2_start = [4, 1]
    input_rover1_instruction_set = "NEESSS"
    input_rover2_instruction_set = "WWWNNNEEE"
    
Output Example:

__INTERSECTIONS__
Intersection 1: [1, 3]
Intersection 2: [2, 1]
__GRID__
[' ', '→', '→', '→', 'B']
['→', 'X', '↓', ' ', ' ']
['a', '↑', '↓', ' ', ' ']
[' ', '↑', 'X', '←', 'b']
[' ', ' ', 'A', ' ', ' ']
__LEGEND__
[['North:', '↑'], ['South:', '↓'], ['East:', '→'], ['West:', '←'], ['R1Start:', 'a'], ['R2Start:', 'b'], ['R1End:', 'A'], ['R2End:', 'B'], ['Intersection:', 'X']]
