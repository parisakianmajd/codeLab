import heapq
from Queue import PriorityQueue

class priority_queue:
    def __init__(self):
        self._queue = []
        # index is used to sort the items in order they were inserted
        self._index = 0

    def put(self, item, priority):
        #heappq implements a min heap, i.e. heappop return the smallest item 
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def get(self):
        # get the next task
        return heapq.heappop(self._queue)[-1]

pq = priority_queue()
pq.put('task1', 2)
pq.put('task2', 1)
pq.put('task3', 3)
pq.put('task4', 1)
print pq.get()
print pq.get()
print pq.get()
print pq.get()
print "Python PQ:"
newPQ = PriorityQueue()
newPQ.put((2, 'task1'))
newPQ.put((1, 'task2'))
newPQ.put((3, 'task3'))
newPQ.put((1, 'task4'))
while not newPQ.empty():
    print newPQ.get()[1]
