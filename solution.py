assignments = []

from values import *

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values


def naked_twins(_values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    values = _values.copy()

    # Find all instances of naked twins
    for unit in unitlist:
        invd = set()
        for box in unit:
            if len(values[box]) == 2:
                if values[box] in invd:
                    remove_from_peers(values[box], unit, values)

                invd.add(values[box])


    return values


def remove_from_peers(twin_val, unit, values):
    for peer in unit:
        if values[peer] != twin_val:
            for val in twin_val:
                values[peer] = values[peer].replace(val, '')


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    di = dict(zip(boxes, chars))
    values = dict()
    for k in di:
        assign_value(values, k, di[k])

    return values

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print
    pass

def eliminate(values):
    """
       Remove values that cant not be used in a box because they were used as solution in other peers of that box
       Args:
           values(dict): The sudoku in dictionary form
       """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            assign_value(values, peer, values[peer].replace(digit,''))
    return values

def only_choice(values):
    """
          Given several boxes with different possible values in a unit, if there is a number that appears in only one of
          those boxes then that box is the only choice for that number
          Args:
              values(dict): The sudoku in dictionary form
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                assign_value(values, dplaces[0], digit)
    return values

def reduce_puzzle(values):
    """
          Remove values that cant not be used in a box because they were used as solution in other peers of that box
          Args:
              values(dict): The sudoku in dictionary form
    """
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Use the Eliminate Strategy
        values = eliminate(values)
        # Use the Only Choice Strategy
        values = only_choice(values)

        #Applying Naked Twins
        values = naked_twins(values)

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)

    if values == False:
        return False

    # Choose one of the unfilled squares with the fewest possibilities
    min = 100
    minbox = None
    for box in values:
        if len(values[box]) > 1 and len(values[box]) < min:
            min = len(values[box])
            minbox = box

    if minbox == None:
        return values

    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for v in values[minbox]:
        values_copy = values.copy()
        values_copy[minbox] = v
        values_res = search(values_copy)
        if values_res != False:
            return values_res

    return False

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """

    return search(grid_values(grid))

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        #visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
