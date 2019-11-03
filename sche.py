
import draw


def read_tasks(algo_map_input):
    task_list = []
    algo_num = 0
    with open('a_out.txt', 'r') as f:
        algo = f.readline().rstrip()
        try:
            algo_num = algo_map_input[algo]
        except:
            algo_num = 0
        tasks = f.readline().rstrip()
        tasks = tasks.replace(")", ',')
        tasks = tasks.replace("(", '')

    task_list = tasks.split(',')
    new_list = []
    for task in task_list:
        if len(task) > 0:
            new_list.append(task)
    task_list = new_list

    new_list = []
    for val in task_list:
        new_list.append(int(val))
    task_list = new_list

    i = 0
    cache = []
    task_tuple_list = []
    for val in task_list:
        if i % 3 == 2:
            cache.append(val)
            task_tuple_list.append(tuple(cache))
            cache.clear()
        else:
            cache.append(val)
        i += 1

    return algo_num, task_tuple_list


def fifo(task_list):
    sched_tasks = []
    tick = 0
    for task in task_list:
        arrive_time = task[1]
        task_length = task[0]

        diff = arrive_time - tick

        sched_start = 0
        sched_end = 0

        if diff >= 0:
            sched_start = arrive_time
            sched_end = arrive_time+task_length
            tick = sched_end
        else:
            sched_start = arrive_time - diff
            sched_end = arrive_time + task_length - diff
            tick = sched_end
        sched_tasks.append(tuple([sched_start, sched_end]))
    return sched_tasks


def rr(task_list):
    print(task_list)
    sched_tasks = []
    max_fac_time = 8

    tick = 0

    time_left = []
    arr_time = []

    for task in task_list:
        time_left.append(task[0])
        arr_time.append(task[1])

    i_max = len(task_list)
    print(i_max)

    while True:
        print("ion whiel")

        finished = False

        runned = False
        for i in range(i_max):
            if time_left[i] > 0:
                if arr_time[i] <= tick:
                    runned = True
                    # can schedule
                    if time_left[i] < max_fac_time:
                        sched_tasks.append(tuple([tick, tick+time_left[i]]))
                        time_left[i] = 0
                        tick += time_left[i]
                    else:
                        sched_tasks.append(tuple([tick, tick+max_fac_time]))
                        time_left[i] -= max_fac_time
                        tick += time_left[i]

        if runned == False:
            for i in range(i_max):
                if tick < arr_time[i]:
                    tick = arr_time[i]
                    break

            if sum(time_left) == 0:
                break

        runned = False

    print(sched_tasks)

    return sched_tasks


algo_map = {"First Come First Serve": 0, "Round Robin": 1}


algo_num, task_list = read_tasks(algo_map)


print('algo_num', algo_num)

task_list.sort(key=lambda tup: tup[1])


sched_tasks = []

if algo_num == 0:
    sched_tasks = fifo(task_list)
if algo_num == 1:
    sched_tasks = rr(task_list)
    # sched_tasks = fifo(task_list)

print(sched_tasks)

sche = []
for index, task in enumerate(sched_tasks):
    sche.append(tuple([index, task[0], task[1], 0]))
    # print(tuple([index,task[0],task[1],0]))


cont = {}
for i in range(len(sche)):
    cont[i] = {i}


draw.draw_canvas(sche, cont, 'a.png')
