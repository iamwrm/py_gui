
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


algo_map = {"First Come First Serve": 0}


algo_num, task_list = read_tasks(algo_map)


print('algo_num', algo_num)
print(task_list, len(task_list))

task_list.sort(key=lambda tup: tup[1])


tick = 0

sched_tasks = []
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
    sched_tasks.append(tuple([sched_start,sched_end]))
    

sche = []
for index, task in enumerate(sched_tasks):
    sche.append(tuple([index,task[0],task[1],0]))
    #print(tuple([index,task[0],task[1],0]))



cont = {}
for i in range(len(sche)):
    cont[i]={i}


draw.draw_canvas(sche, cont, 'a.png')



