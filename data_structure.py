'''
Trong phần dữ liệu này mình custom lại 3 kiểu dữ liệu Queue, Stack và Priority_Queue

'''
from collections import deque
from PQueue import PriorityQueue


class Frontier:
    '''Là cái queue, theo nguyên tắc FIFO chứa các nodes được tìm thấy trong cây tìm kiếm search tree.'''

    def __init__(self):
        self.queue = deque()

    def __contains__(self, item):
        '''Custom method, chỉ search theo thuộc tính state của một cái grid'''
        for element in self.queue:
            if item.state == element.state:
                return True

        return False


class Explored:
    '''Là một STACK theo nguyên tắc LIFO'''

    def __init__(self):
        self.set = set()

    def __contains__(self, item):
        '''Tìm kiếm trạng thái trong cái Stack có hay không'''
        for element in self.set:
            if item.state == element.state:
                return True
        return False


class Priority_Frontier:
    '''Priority Queue. Đặt các phần tử tuân theo thứ tự heuristic của nó'''

    def __init__(self):
        self.pQueue = PriorityQueue()

    def __contains__(self, item):
        return self.pQueue.has_item(item)

