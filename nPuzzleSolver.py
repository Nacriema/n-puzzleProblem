import sys
import grid
import solver

# validate command line input
if len(sys.argv) != 3:
    sys.stderr.write('Error: must be 3 command line arguments of the form: \npython nPuzzleSolver.py <method> <board>\n')
    sys.exit()

if sys.argv[1] not in ['bfs', 'dfs', 'ast']:
    sys.stderr.write('Error: <method> argument must be one of bfs, dfs, ast\n')
    sys.exit()

# Convert input string to a list of ints
input_list = sys.argv[2].split(',')
input_list = map(int, input_list)
input_list = list(input_list)

if len(input_list) not in [4, 9, 16, 25]:
    sys.stderr.write('Error: input grid must be nxn square where n is 2, 3, 4 or 5 \n')
    sys.exit()

ordered_list = sorted(input_list)
for index, number in enumerate(ordered_list):
    if number != index:
        sys.stderr.write('Error: input list must contain all numbers from 0 to n^2 - 1 \n')
        sys.exit()

try:
    solver = solver.Solver(input_list)
except ValueError:
    print('No solution exits')
    sys.exit()

search_method = sys.argv[1]
if search_method == 'ast':
    pass
else:
    solver.uniformed_search(search_method)
