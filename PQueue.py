'''Implementation of Priority Queue using Queue
Sử dụng thư viện heapq.py trong Python
Source: https://stackoverflow.com/questions/407734/a-generic-priority-queue-for-python
Tại vì theo người ta bảo trong Stackoverflow:
Cái thư viện Queue.PriorityQueue nó không có được dùng như là một kiểu cấu trúc dữ liệu thuần, mà nó dùng trong Multi
Threading hơn.
Và một cái nữa là cái hàm có sẵn của họ không cho phép tìm kiếm item trong PriorityQueue đó tới.

Link tham khảo: https://stackoverflow.com/questions/23729690/finding-value-in-a-priority-queue-in-python


'''
import heapq


class PriorityQueue(object):
    '''
    Combined priority queue and set data structure

    Nó hoạt động như priority queue, trừ việc là items của nó được đảm bảo là duy nhất. O(1) membership test, O(nlogn)
    insertion và removal of the smallest item

    Important: items of this data structure must be both comparable and hastable (phải implement __cmp__ và __hash__).
    Điều này là cần trong Python built-in objects, nhưng ta cần phải implement method cho mấy cái ni nếu như chúng ta
    sử dụng được cái data structure trong custom object này.
    '''

    def __init__(self, items=None):
        '''Create a new PriorityQueue set, the data structure will be created in O(N)'''
        if items is None:
            items = []
        self.set = dict((item, True) for item in items)
        self.heap = self.set.keys()
        heapq.heapify(self.heap)

    def has_item(self, item):
        '''Check if item exists in the queue'''
        return item in self.set

    def pop_smallest(self):
        '''Remove and return the smallest item from the queue'''
        smallest = heapq.heappop(self.heap)
        del self.set[smallest]
        return smallest

    def add(self, item):
        """Add item into the queue if it doesnt already exist"""
        if item not in self.set:
            self.set[item] = True
            heapq.heappush(self.heap, item)

