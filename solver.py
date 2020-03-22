'''
Trong này nó chứa các hướng giải cho bài toán của mình
Bao gồm:
* BFS
* DFS
(2 cái trên được gọi là uniform search - Tức là chỉ biết điểm bắt đầu và điểm kết thúc
* A Star

Với BFS: Sudocode in Python

frontier = Queue() # Chứa các node trong quá trình duyêt
frontier.dequeue(start) : đưa vào trong queue node bắt đầu

camefrom = {} # Kiểu dữ liệu key value
camefrom[start] = None # Root node
while (!frontier.isEmpty()):
    current = frontier.enqueue()
    for neighbor in graph.getNeighbors(current):
        # Nếu như node đó chưa được duyệt thì ta thêm nó vào trong
        if neighbor not in camefrom:
            # Thêm cái neighbor vào trong hàng đợi
            frontier.dequeue(neighbor)
            # Đánh dấu source của cái neigbor này là từ cái current
            camefrom[neighbor] = current



current = []
'''

'''Hạn chế đặt tên module trùng với tên các thành phân bên trong cái module đó'''
import math
import copy
import data_structure
import grid
import sys


def set_goal_state(input_list):
    # Dựa vào cái input_list cho ra cái goal_state
    # Goal_state theo thứ tự đúng nhất
    n = int(math.sqrt(len(input_list)))
    goal_state = [['-' for x in range(n)] for y in range(n)]

    # populate the goal grid with ordered tiles
    i = 0
    j = 0
    count = 1

    while i < n:
        if count == n * n:
            count = 0
        goal_state[i][j] = count
        count += 1
        j += 1
        if j == n:
            j = 0
            i += 1

    return goal_state


class Solver:
    '''Controler class.
    Trong class này chứa tất cả các hàm xử lý cần thiết
    '''

    def __init__(self, input_list):
        # Kiểm tra điều kiện ban đầu có thỏa mãn để giải bài toán hay không ???
        # Phần code riêng nữa nhưng mình chưa làm ở đây đâu

        self.initial_state = copy.deepcopy(self.list_to_grid(input_list))
        self.goal_state = set_goal_state(input_list)

        # Sử dụng các kiểu dữ liệu để cài đặt 3 loại thuật toán của chúng ta
        # 1. BFS, frontier chứa dữ liệu kiểu Grid
        self.frontier = data_structure.Frontier()
        self.came_from = {}

    def uniformed_search(self, search_method):
        '''Mở rộng không gian tìm kiếm sử dụng breath-first search hoặc depth-first search'''
        # Trong code của người ta có đoạn sử dụng metric để đo đạc các khoảng cách, cái nớ mình sẽ làm sau
        initial_grid = grid.Grid(self.initial_state)
        self.frontier.queue.append(initial_grid)

        # Thêm một cái dict lưu lại path
        self.came_from[initial_grid] = None

        # TODO:
        # TODO: Uniformed_search
        # while queue is not empty
        while self.frontier.queue:
            if search_method == 'bfs':
                current = self.frontier.queue.popleft()
            elif search_method == 'dfs':
                current = self.frontier.queue.pop()

            if self.goal_test(current):
                # Nếu như cái trạng thái hiện tại là trạng thái cuối
                # Minh build lại cái chỗ ni mới được
                print(self.build_path(current, self.came_from))
                return 0

            # TODO: Nếu như không phải trạng thái dừng lại thì ta tiếp tục thuật toán, cả phần sau đổ vào trong expand
            else:
                self.expand_nodes(current, search_method)

    def expand_nodes(self, start_grid, search_method):
        '''Đầu vào là giá trị hiện tại của grid, thêm các giá trị có thể có tiếp vào trong frontier'''
        directions = ['up', 'down', 'left', 'right']

        # Có thực sự mình chỉ cần thay đổi thứ tự duyệt thì nó sẽ thay đổi cả cái format của mình hay không vậy ???
        if search_method == 'dfs':
            node_order = reversed(directions)
        for direction in directions:
            #imagined_grid = copy.copy(start_grid)
            imagined_grid = grid.Grid(start_grid.state)

            if imagined_grid.move(direction):  # Return false nếu không di chuyển được, còn nếu được thì nó sẽ move luôn
                if imagined_grid not in self.came_from:
                    self.frontier.queue.append(imagined_grid)
                    self.came_from[imagined_grid] = start_grid

    def list_to_grid(self, tile_list):
        '''Nhận vào list n^2, và trả ra lại cái n*n 2d list'''
        n = int(math.sqrt(len(tile_list)))

        # Khoi tao luoi rong
        input_grid = [['-' for x in range(n)] for y in range(n)]

        # populate grid with tile
        i = 0
        j = 0
        for tile in tile_list:
            input_grid[i][j] = tile
            j += 1
            if j == n:
                j = 0
                i += 1

        return input_grid

    def goal_test(self, state):
        '''Compare a given state to the goal state'''
        # TODO: confusing names. state here is not a Grid.state but a Grid
        if state.state == self.goal_state:
            return True
        else:
            return False

    def build_path(self, final_node, came_from):
        '''Từ cái trạng thái grid đi cuối truy ngược lại cái nguồn của nó'''
        path = list()
        previous = came_from[final_node]
        path.append(final_node)
        while previous is not None:
            path.append(previous)
            previous = came_from[previous]

        path.reverse()
        return path

