
def get_movement(direction):

    direction_vectors = {
        "N": [0, 1],
        "S": [0, -1],
        "E": [1, 0],
        "W": [-1, 0]
    }
    return direction_vectors[direction]


def get_move_symbol(direction):

    symbol_direction = {
        "N": '↑',
        "S": '↓',
        "E": '→',
        "W": '←'
    }
    return symbol_direction[direction]


def print_legend():

    print("__LEGEND__")
    legend = [["North:", '↑'],
              ["South:", '↓'],
              ["East:", '→'],
              ["West:", '←'],
              ["R1Start:", 'a'],
              ["R2Start:", 'b'],
              ["R1End:", "A"],
              ["R2End:", "B"],
              ["Intersection:", "X"],
              ]

    print(legend)


def get_rover_path(start, instructions):

    path = [start]
    pos_x = start[0]
    pos_y = start[1]
    movements = []
    for n in instructions:
        m = get_movement(n)
        movements.append(m)
        pos_x = pos_x + m[0]
        pos_y = pos_y + m[1]
        path.append([pos_x, pos_y])

    return movements, path


def run_rovers(grid_size, rover1_start, rover2_start, rover1_instruction_set, rover2_instruction_set):

    # Get rover paths as a list of coordinates movements optional
    rover1_movements, rover1_path = get_rover_path(rover1_start, rover1_instruction_set)
    rover2_movements, rover2_path = get_rover_path(rover2_start, rover2_instruction_set)

    # print("rover 1 Move: " + rover1_movements.__str__())
    # print("Rover 1 Path: " + rover1_path.__str__())
    # print("rover 2 Move: " + rover2_movements.__str__())
    # print("Rover 2 Path: " + rover2_path.__str__())

    # Check for intersections and print cell coordinates
    print("__INTERSECTIONS__")
    count_intersection = 0
    for rover1_position in rover1_path:
        for rover2_position in rover2_path:
            if rover1_position == rover2_position:
                count_intersection += 1
                print("Intersection " + count_intersection.__str__() + ": " + rover1_position.__str__())

    # Visualize movement optional
    print("__GRID__")
    draw_grid(grid_size, rover1_start, rover1_path, rover1_instruction_set,
              rover2_start, rover2_path, rover2_instruction_set)

    print_legend()


def draw_grid(grid_size, rover1_start, rover1_path, rover1_instruction_set,
              rover2_start, rover2_path, rover2_instruction_set):

    # Iterate through the grid from [0,0] to grid_size to build map
    grid = []
    for y in range(grid_size[1]):
        row = []
        for x in range(grid_size[0]):

            # determine from coordinates which symbol to use with default ' '
            symbol = ' '
            # If intersect
            if ([x, y] in rover2_path) and ([x, y] in rover1_path):
                symbol = "X"
            else:
                # If Rover 1 in cell
                if [x, y] in rover1_path:
                    index = rover1_path.index([x, y])
                    # If Rover 1 end of Path
                    if index >= rover1_instruction_set.__len__():
                        symbol = 'A'
                    else:
                        symbol = get_move_symbol(rover1_instruction_set[index])

                # If Rover 2 in cell
                if [x, y] in rover2_path:
                    index = rover2_path.index([x, y])
                    # If Rover 2 end of Path
                    if index >= rover2_instruction_set.__len__():
                        symbol = 'B'
                    else:
                        symbol = get_move_symbol(rover2_instruction_set[index])
                # If rover # Start
                if [x, y] == rover1_start:
                    symbol = 'a'
                elif [x, y] == rover2_start:
                    symbol = "b"
            # Append to row list
            row.append(symbol)
        # Add as new row to grid
        grid.append(row)

    # To print the grid top to bottom it should be reversed
    for rows in reversed(grid):
        print(rows)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Set initial conditions
    input_grid_size = [5, 5]
    input_rover1_start = [0, 2]
    input_rover2_start = [4, 1]
    input_rover1_instruction_set = "NEESSS"
    input_rover2_instruction_set = "WWWNNNEEE"

    run_rovers(input_grid_size, input_rover1_start, input_rover2_start, input_rover1_instruction_set,
               input_rover2_instruction_set)
