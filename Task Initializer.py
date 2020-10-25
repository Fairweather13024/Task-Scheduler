#This code has been adapted from session 5.1

def add_tasks_pqueue(pqueue, rtsks):
    """
    Implements step 2 of the scheduler
    Input: list of tasks
    Output: priority queue (created using the heapq module)
    """
    if rtsks:
        if not pqueue:  # If the priority queue is empty
            pqueue = rtsks
            pqueue = MinHeapq(pqueue)
            MinHeapq.heapify(pqueue)
        else:
            for t in rtsks:
                ### your code here
                MinHeapq.heappush( pqueue, t )
    return pqueue