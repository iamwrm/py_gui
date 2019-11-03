
import draw
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt


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
    for index, task in enumerate(task_list):
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
        sched_tasks.append(tuple([index, sched_start, sched_end]))

    return sched_tasks


def rr(task_list):
    sched_tasks = []
    max_fac_time = 8

    tick = 0

    time_left = []
    arr_time = []

    for task in task_list:
        time_left.append(task[0])
        arr_time.append(task[1])

    i_max = len(task_list)

    while True:
        finished = False
        runned = False

        for i in range(i_max):
            if time_left[i] > 0:
                if arr_time[i] <= tick:
                    runned = True
                    # can schedule
                    if time_left[i] < max_fac_time:
                        sched_tasks.append(
                            tuple([i, tick, tick+time_left[i]]))
                        time_left[i] = 0
                        tick += time_left[i]
                    else:
                        sched_tasks.append(
                            tuple([i, tick, tick+max_fac_time]))
                        time_left[i] -= max_fac_time
                        tick += max_fac_time

        if runned == False:
            for i in range(i_max):
                if tick < arr_time[i]:
                    tick = arr_time[i]
                    break

            if sum(time_left) == 0:
                break

        runned = False

    return sched_tasks


def cal_overall_waiting_time(task, sche):
    latest_end_time = 0
    for v in sche:
        end_time = v[2]
        if end_time > latest_end_time:
            latest_end_time = end_time

    left_time = []
    for v in task:
        left_time.append(v[0])

    wait_time = []
    wait_time_y = []

    tick = 0
    while tick < latest_end_time:
        wait_time_i = 0
        for i, v in enumerate(task):
            if tick >= v[1] and left_time[i] > 0:
                wait_time_i += 1
        for v in sche:
            if left_time[v[0]] > 0:
                if tick >= v[1] and tick <= v[2]:
                    left_time[v[0]] -= 1
        wait_time_y.append(wait_time_i)
        wait_time.append(tick)

        tick += 1

    for i, v in enumerate(wait_time_y):
        if i > 0:
            wait_time_y[i] += wait_time_y[i-1]

    return wait_time, wait_time_y


def cal_overall_tasks_to_finish(task, sche):
    latest_end_time = 0
    for v in sche:
        end_time = v[2]
        if end_time > latest_end_time:
            latest_end_time = end_time

    left_time = []
    for v in task:
        left_time.append(v[0])

    wait_time = []
    wait_time_y = []

    tick = 0
    while tick < latest_end_time:
        wait_time_i = 0
        for i, v in enumerate(task):
            if tick >= v[1] and left_time[i] > 0:
                wait_time_i += 1
        for v in sche:
            if left_time[v[0]] > 0:
                if tick >= v[1] and tick <= v[2]:
                    left_time[v[0]] -= 1
        wait_time_y.append(wait_time_i)
        wait_time.append(tick)

        tick += 1

    return wait_time, wait_time_y


algo_map = {"First Come First Serve": 0, "Round Robin": 1}


algo_num, task_list = read_tasks(algo_map)


print('algo_num', algo_num)

task_list.sort(key=lambda tup: tup[1])


sched_tasks = []

if algo_num == 0:
    sched_tasks = fifo(task_list)
if algo_num == 1:
    sched_tasks = rr(task_list)

sche = []

for i, v in enumerate(sched_tasks):
    sche.append(tuple([i, v[1], v[2], 0]))

cont = defaultdict(list)
for i, task in enumerate(sched_tasks):
    cont[task[0]].append(i)

print(sche)
print(task_list)


waiting_time_x, waiting_time_y = cal_overall_waiting_time(
    task_list, sched_tasks)
plt.figure(0)
plt.plot(waiting_time_x, waiting_time_y, 'b', label='Overall Waiting Time')
plt.legend()
plt.savefig('b.png')


tasks_to_finish_x, tasks_to_finish_y = cal_overall_tasks_to_finish(
    task_list, sched_tasks)
plt.figure(1)
plt.plot(tasks_to_finish_x, tasks_to_finish_y, 'b', label='Tasks to Finish')
plt.legend()
plt.savefig('c.png')


draw.draw_canvas(sche, cont, 'a.png')
