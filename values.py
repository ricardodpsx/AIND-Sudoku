def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s + t for s in A for t in B]


rows = 'ABCDEFGHI'
cols = '123456789'

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonal_1_units = [[a + str(i + 1) for i, a in enumerate(rows)]]
diagonal_2_units = [[a + str(len(rows) - i) for i, a in enumerate(rows)]]
unitlist = row_units + column_units + square_units + diagonal_1_units + diagonal_2_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
