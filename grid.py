'''
Implement trạng thái, là một node của trò chơi.
Mình tham khảo tại trang:

https://github.com/andavies/n-puzzle/blob/master/grid.py
'''
import math
import copy


class Grid:
    '''
    Biểu diễn trạng thái của lưới: state, path_history, và heuristic score.
    '''

    def __init__(self, input_state):
        # Đừng phụ thuộc vào input_state, ta muốn object có thuộc tính State của riêng nó
        self.state = copy.deepcopy(input_state)

        self.path_history = list()

        self.n = len(input_state[0])

        # defined by mahattan heuristic
        self.score = 0

    def __repr__(self):
        string = ''
        for _ in self.state:
            string += str(_)
        return string + '  '

    def move(self, direction):
        '''
        Trượt mảnh theo một trong 4 hướng
        Trả ra True nếu như thành cồng ()
        Trả ra sai nếu như hướng đi đó là không thể
        '''

        zero_coords = self.locate_tile(0, self.state)

        # Tìm mảnh trống vì chỗ đó mới có thể di chuyển được
        if direction == 'up':
            y, x = 1, 0
        elif direction == 'down':
            y, x = -1, 0
        elif direction == 'left':
            y, x = 0, 1
        elif direction == 'right':
            y, x = 0, -1
        else:
            raise ValueError('Invalid direction: must be \'up\', \'down\', \
                \'left\' or \'right\'')

        # Trả ra giá trị false nếu như move đó không thể thực hiện được
        if zero_coords[0] + y not in range(0, self.n):
            return False
        if zero_coords[1] + x not in range(0, self.n):
            return False

        # Nếu thấy hợp lý thì bắt đầu di chuyển thôi
        tile_to_move = self.state[zero_coords[0] + y][zero_coords[1] + x]
        self.state[zero_coords[0]][zero_coords[1]] = tile_to_move
        self.state[zero_coords[0] + y][zero_coords[1] + x] = 0

        return True

    def locate_tile(self, tile, grid_state):
        '''
        Trả lại tọa độ của mảnh được cho, dưới dạng tuple
        :param tile:
        :param grid_state:
        :return:
        '''
        for (y, row) in enumerate(grid_state):
            for (x, value) in enumerate(row):
                if value == tile:
                    return (y, x)

    # Phần ni dùng để tính toán một số thứ trong thuật toán A*
    def manhattan_score(self, goal_state):
        '''
        Trả lại tổng khoảng cách manhattan của mỗi mảnh so với vị trí đích của nó
        :param goal_state:
        :return:
        '''
        sum = 0
        for (y, row) in enumerate(self.state):
            for (x, tile) in enumerate(row):
                if tile == 0:
                    continue
                sum += self.manhattan_distance(tile, (y, x), goal_state)

        return sum

    def manhattan_distance(self, tile, tile_position, goal_state):
        '''
        Tính khoảng cách Manhattan giữa position của tile và positon của nó trong goal_state
        :param title:
        :param title_position:
        :param goal_state:
        :return:
        '''
        goal_position = self.locate_tile(tile, goal_state)
        distance = (abs(goal_position[0] - tile_position[0])) + abs(goal_position[1] - tile_position[1])
        return distance


