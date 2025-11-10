import time

class Task:

    def __init__(self, id, priority, a_time = None):
        self.id = id
        self.priority = priority

        if a_time == None:
            a_time = time.time()
        self.a_time = a_time

class PriorityQueue:

    def __init__(self):
        self.heap = []

    def make_heap_up(self, idx):
        par_idx = (idx - 1) // 2
        if idx > 0:
            # Check if any of the node has greater priority that the parent
            # If nodes have same priority check the a_time to determine the largest
            # Swap nodes and check the nodes further up

            if self.heap[idx].priority > self.heap[par_idx].priority:
                self.heap[idx], self.heap[par_idx] = self.heap[par_idx], self.heap[idx]
                self.make_heap_up(par_idx)
            elif self.heap[idx].priority == self.heap[par_idx].priority and self.heap[idx].a_time < self.heap[par_idx].a_time:
                self.heap[idx], self.heap[par_idx] = self.heap[par_idx], self.heap[idx]
                self.make_heap_up(par_idx)

        def make_heap_down(self, idx):
            largest = idx
    
        left = (2 * idx) + 1
        right = (2 * idx) + 2

        # Check if any of the child nodes are greater priority that the parent
        # If nodes have same priority check the a_time to determine the largest
        # Swap nodes and check the nodes further down

        if left < len(self.heap):
            if self.heap[left].priority > self.heap[largest].priority:
                largest = left
            elif self.heap[left].priority == self.heap[largest].priority and self.heap[left].a_time < self.heap[largest].a_time:
                largest = left

        if right < len(self.heap):
            if self.heap[right].priority > self.heap[largest].priority:
                largest = right
            elif self.heap[right].priority == self.heap[largest].priority and self.heap[right].a_time < self.heap[largest].a_time:
                largest = right

        if largest != idx:
            self.heap[largest], self.heap[idx] = self.heap[idx], self.heap[largest]
            self.make_heap_down(largest)

    # Insert a task
    def insert(self, task):
        self.heap.append(task)
        # Check the nodes up to the root to ensure heap
        self.make_heap_up(len(self.heap) - 1)

    # Remove the task with the max priority
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # Task with max priority should be at the top
        max = self.heap[0]
        self.heap[0] = self.heap.pop()
        # Rearrange the heap
        self.make_heap_down(0)

        return max

    def increase_key(self, task, n_priority):
        for i in range(len(self.heap)):
            if self.heap[i].id == task.id:
                if n_priority > task.priority:
                    task.priority = n_priority
                    # Priority has increased, check the heap property for the parents
                    self.make_heap_up(i)
                break

    def decrease_key(self, task, n_priority):
        for i in range(len(self.heap)):
            if self.heap[i].id == task.id:
                if n_priority < task.priority:
                    task.priority = n_priority
                    # Priority has decreased, check the heap property for the children
                    self.make_heap_down(i)
                break

    def is_empty(self):
        return 0 == len(self.heap)

