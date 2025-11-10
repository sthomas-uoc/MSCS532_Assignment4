# Tests the implementations

import random
import time

import psutil
import os
import gc

from merge_sort import merge_sort
from quick_sort import quick_sort
from heap_sort import heap_sort
from priority_queue import PriorityQueue, Task

def test_runner():

    nums = [2, 3, 5, 1, 4, 7]

    result = [1, 2, 3, 4, 5, 7]

    print("Starting heap sort")
    hs_nums = heap_sort(nums)

    print(f"Heap sorted: {hs_nums}")

    assert hs_nums == result

    # Compare HeapSort vs MergeSort
    
    # Input sizes
    sizes = [100, 1000, 10000, 100000, 1000000]

    # Data sort options
    input_opts = ["rand", "sorted", "rev_sorted"]

    # Get PID for capturing stats
    pid = os.getpid()

    # Disable global garbage collection
    gc.disable()

    for size in sizes:
        nums = gen_random_numbers(size, 0, 5000000)

        # Use library sort to verify results
        result = nums[:len(nums)]
        result.sort()
        # print(f"Lib sort {result}")
    
        # print(f"Nums: {nums}")

        for input_opt in input_opts:
            if input_opt == "rand":
                nums = nums
            elif input_opt == "sorted":
                nums.sort()
            else:
                nums.sort()
                nums.reverse()
    
            # print("Starting merge sort")
            print(f"Test {size} {input_opt} numbers")

            # Run garbage collection before running merge sort
            gc.collect()

            memory_usage_before = psutil.Process(pid).memory_info().rss
            
            # Capture time
            start_time = time.time()
            
            ms_nums = merge_sort(nums)
            
            end_time = time.time()
        
            memory_usage_after = psutil.Process(pid).memory_info().rss
            
            # print(f"Merge sorted: {ms_nums}")
            
            print(f"Merge sorted {size} {input_opt} nums in {(end_time - start_time):.6f} seconds using {(memory_usage_after - memory_usage_before)/ (1024 * 1024)} MB memory")
        
            assert ms_nums == result
        
            # print("Starting heap sort")
    
            # Run garbage collection before running heap sort
            gc.collect()

            mem_usage_before = psutil.Process(pid).memory_info().rss
            
            # Capture time
            start_time = time.time()
            
            hs_nums = heap_sort(nums)
            
            end_time = time.time()
        
            mem_usage_after = psutil.Process(pid).memory_info().rss
            
            # print(f"Heap sorted: {ms_nums}")
            
            print(f"Heap sorted {size} {input_opt} nums in {(end_time - start_time):6f} seconds using {(memory_usage_after - memory_usage_before)/ (1024 * 1024)} MB memory")
        
            assert hs_nums == result

            # print("Starting quick sort")
    
            # Run garbage collection before running quick sort
            gc.collect()

            mem_usage_before = psutil.Process(pid).memory_info().rss
            
            # Capture time
            start_time = time.time()
            
            qs_nums = quick_sort(nums)
            
            end_time = time.time()
        
            mem_usage_after = psutil.Process(pid).memory_info().rss
            
            # print(f"Quick sorted: {ms_nums}")
            
            print(f"Quick sorted {size} {input_opt} nums in {(end_time - start_time):6f} seconds using {(memory_usage_after - memory_usage_before)/ (1024 * 1024)} MB memory")
        
            assert qs_nums == result


    print("Running PriorityQueue tests...")

    # Test 1: Basic Priority Ordering
    print("Test 1: Basic Priority Ordering...")
    pq = PriorityQueue()
    pq.insert(Task("Task A (P=10)", 10))
    pq.insert(Task("Task B (P=5)", 5))
    pq.insert(Task("Task C (P=20)", 20))

    t1 = pq.extract_max()
    assert t1.id == "Task C (P=20)"
    t2 = pq.extract_max()
    assert t2.id == "Task A (P=10)"
    t3 = pq.extract_max()
    assert t3.id == "Task B (P=5)"

    # Test 2: Empty Queue Handling
    print("Test 2: Empty Queue Handling...")
    pq = PriorityQueue()
    assert pq.is_empty() == True
    t_empty = pq.extract_max()
    assert t_empty is None
    pq.insert(Task("Task D", 1))
    assert pq.is_empty() == False
    pq.extract_max()
    assert pq.is_empty() == True

    # Test 3: Stability (Tie-Breaker)
    print("Test 3: Stability (Tie-Breaker)...")
    pq = PriorityQueue()
    
    # Create tasks with controlled arrival times
    task_first_in = Task("First In (P=10)", 10, a_time=1.0)
    task_second_in = Task("Second In (P=10)", 10, a_time=2.0)
    task_third_in = Task("Third In (P=10)", 10, a_time=3.0)

    # Insert them out of order
    pq.insert(task_second_in)
    pq.insert(task_third_in)
    pq.insert(task_first_in)

    # Extract them and check they come out in FIRST-IN, FIRST-OUT order
    t1 = pq.extract_max()
    assert t1.id == "First In (P=10)"
    t2 = pq.extract_max()
    assert t2.id == "Second In (P=10)"
    t3 = pq.extract_max()
    assert t3.id == "Third In (P=10)"

    # Test 4: `increase_key`
    print("Test 4: increase_key...")
    pq = PriorityQueue()
    task_low = Task("Low", 2)
    task_mid = Task("Mid", 5)
    task_high = Task("High", 10)
    
    pq.insert(task_low)
    pq.insert(task_mid)
    pq.insert(task_high)

    # Increase "Low" task to be the highest priority
    pq.increase_key(task_low, 20)
    
    # Check new order
    t1 = pq.extract_max()
    assert t1.id == "Low" and t1.priority == 20
    t2 = pq.extract_max()
    assert t2.id == "High"
    t3 = pq.extract_max()
    assert t3.id == "Mid"

    # Test 5: `decrease_key`
    print("Test 5: decrease_key...")
    pq = PriorityQueue()
    task_low = Task("Low", 2)
    task_mid = Task("Mid", 5)
    task_high = Task("High", 10)
    
    pq.insert(task_low)
    pq.insert(task_mid)
    pq.insert(task_high)

    # Decrease "High" task to be the lowest priority
    pq.decrease_key(task_high, 1)

    # Check new order
    t1 = pq.extract_max()
    assert t1.id == "Mid"
    t2 = pq.extract_max()
    assert t2.id == "Low"
    t3 = pq.extract_max()
    assert t3.id == "High" and t3.priority == 1

    print(f"Ok")

# Function that returns requested number of random numbers in a range
def gen_random_numbers(count, min, max):
    return [random.randint(min, max) for _ in range(count)]

if __name__ == "__main__":
    test_runner()
