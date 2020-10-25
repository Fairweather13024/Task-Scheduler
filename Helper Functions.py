"""
A Simple Daily Task Scheduler Using Priority Queues
"""


def print_input_tasks(tsks):
    """
    Input: list of tasks
    Task Status:
    - 'N' : Not yet in priority queue (default status)
    - 'I' : In priority queue
    - 'C' : Completed
    Output: print statement with all the tasks to be included in the scheduler
    """
    print('Input List of Tasks')
    for t in tsks:
        print(f"task:{t[0]} \t {t[1]} \t duration:{t[3]} \t depends on: {t[5]} \t Status: {t[8]}")


def initialize_tasks(tsks):
    """
    Input: list of tasks
    Output: initializes all tasks with default status (not yet in the priority queue).
    """
    for i in range(ntasks):
        tasks[i].append('N')


def unscheduled_tasks(tsks):
    """
    Input: list of tasks
    Output: boolean (checks the status of all tasks and returns `True` if at least one task has status = 'N')
    """
    for t in tsks:
        if t[-1] == 'N':
            return True

    return False


def remove_dependency(tsks, tid):
    """
    Input: list of tasks and task_id of the task just completed
    Output: lists of tasks with t_id removed
    """
    for t in range(ntasks):
        if tsks[t][0] != tid and tid in tsks[t][5]:
            tsks[t][5].remove(tid)


def get_ready_tsks(tsks):
    """
    Implements step 1 of the scheduler
    Input: list of tasks
    Output: list of tasks that are ready to execute (i.e. tasks with no pendending task dependencies)
    """
    rtsks = []
    for i in range(ntasks):
        if tsks[i][-1] == 'N' and not tsks[i][5]:  # If tasks has no dependencies and is not yet in queue
            tsks[i][-1] = 'I'  # Change status of the task
            rtsks.append((tsks[i][0], tsks[i][4]))  # add (task_id, duration) to the list of tasks
            # to be pushed onto the priority queue
    return rtsks


# Task scheduler main iteration loop (steps 1 - 7 in the diagram)

# Inputs Parameters to the Scheduler


step_sz = 10  # step size of scheduler in minutes
c_time = 480  # current time is set to the initial time in minutes (8:00 AM = 8x60)

# Defining my tasks
tasks = [[0, 'Take class in the mezzanine', 30, 100, 90, [1, 2, 3], False, False],
         [1, 'get up at 8:00 AM', 10, 0, 10, [], False, 0],
         [2, 'get dressed and ready', 10, 20, 10, [], False, 0],
         [3, 'eat healthy breakfast', 10, 30, 20, [], False, 0],
         [4, 'Go to the farmers market', 75, 250, 30, [5, 6, 7], True, False],
         [5, 'Talk to someone new', 15, 250, 30, [], True, 4],
         [6, 'Organize my tote bags', 10, 230, 10, [], True, 4],
         [7, 'Water my plants', 50, 220, 20, [], True, 4],
         [8, 'Attend Exploration day', 30, 1000, 1000, [9, 10, 11], True, False],
         [9, 'Prepare my camera', 10, 900, 10, [], True, 8],
         [10, 'Download Vibemap', 10, 910, 10, [], True, 8],
         [11, 'Select a new mode of transport', 10, 930, 20, [], True, 8],
         [12, 'Do work study', 30, 2100, 60, [13, 14, 15], False, False],
         [13, 'Collect personal photos', 10, 2090, 10, [], True, 12],
         [14, 'Search for medium article template', 10, 2080, 10, [], False, 12],
         [15, 'Reread the work study task email for guidance', 10, 2070, 10, [], False, 12],
         [16, 'Attend the Canadian virtual 1001', 130, 3000, 90, [17, 18, 19], True, False],
         [17, 'Finish my laundry', 50, 2970, 10, [], True, 16],
         [18, 'Eat supper', 30, 2980, 10, [], True, 16],
         [19, ' Find the meeting link for the 1001', 50, 2990, 10, [], True, 16],
         [20, 'Go to the Barbers collective', 250, 4000, 120, [21, 22, 23], True, False],
         [21, 'Book appointment', 100, 3970, 10, [], False, 20],
         [22, ' Get ready', 100, 3980, 10, [], False, 20],
         [23, 'Commute to the Barbers collective', 50, 3990, 10, [], True, 20],
         [24, 'Go to the Filmore district', 300, 5000, 240, [25, 26, 27], True, False],
         [25, 'Commute to the Filmore', 100, 4950, 20, [], True, 24],
         [26, 'Get Panda express', 100, 4970, 10, [], True, 24],
         [27, 'Eat Panda express', 100, 4980, 20, [], True, 24],
         [28, 'Apply for internships', 90, 5500, 120, [29, 30, 31], False, False],
         [29, 'Review my resume', 30, 5450, 30, [], False, 28],
         [30, 'Tailor my resume for the job application', 30, 5480, 10, [], False, 28],
         [31, 'Update my job application spreadsheet', 30, 5490, 10, [], False, 28]
         ]

ntasks = len(tasks)  # Number of tasks
pqueue = []  # Priority Queue

# STEP 0: Initialize the status of all tasks in the input list
initialize_tasks(tasks)
print_input_tasks(tasks)