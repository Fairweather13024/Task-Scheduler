while unscheduled_tasks(tasks) or pqueue.heap:

    # STEP 1: Extract tasks ready to execute (those without dependencies)
    rtsks = get_ready_tsks(tasks)

    # STEP 2: Push the tasks onto the priority queue
    pqueue = add_tasks_pqueue(pqueue, rtsks)

    if pqueue:  # STEP 3: Check for tasks in the priority queue.

        # STEP 4: get the tasks on top of the priority queue
        ### your code here
        (tid, rtime) = MinHeapq.heappop(pqueue)

        print(f"Simple Scheduler executing task {tid}; remaining time to complete this task {rtime} min")
        tstep = step_sz  # tstep is the scheduler's time step
        if rtime < step_sz:  # If it is less than the step_size take a smaller time step
            tstep = rtime

        # STEP 5: adjust the tasks remaining time
        rtime -= tstep
        c_time += tstep  # update the schedulers clock
        print(f"Time: {c_time // 60}h{c_time % 60:02}")

        # STEP 7: Task has been completed
        if rtime == 0:
            print(f"✅ Completed Task {tid} - '{tasks[tid][1]}' at time {c_time // 60}h{c_time % 60:02}")
            ####### your code here
            remove_dependency(tasks, tid)
        else:
            ####### your code here
            MinHeapq.heappush(pqueue, (tid, rtime))

print("🏁 Completed all planned tasks")