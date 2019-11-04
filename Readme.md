# Scheduling Algorithms Visualization Tool

## What is scheduling algorithms?

> In [computing](https://en.wikipedia.org/wiki/Computing), **scheduling** is the method by which work is assigned to resources that complete the work. The work may be virtual computation elements such as [threads](https://en.wikipedia.org/wiki/Thread_(computer_science)), [processes](https://en.wikipedia.org/wiki/Process_(computing)) or data [flows](https://en.wikipedia.org/wiki/Flow_(computer_networking)), which are in turn scheduled onto hardware resources such as [processors](https://en.wikipedia.org/wiki/Central_processing_unit), [network links](https://en.wikipedia.org/wiki/Telecommunications_link) or [expansion cards](https://en.wikipedia.org/wiki/Expansion_card).
>
> ​		by Wikipedia https://en.wikipedia.org/wiki/Scheduling_(computing)

In a short form, when there are multiple tasks need to be done on a computer, scheduling algorithms decide which task should go first and which one should wait.

## Mainstream scheduling algorithms

- First come, first served
- Priority Scheduling
- Round-robin scheduling
- Shortest Job First
- Etc

## What we focus

Within the app's scope, we want to focus on **Round-robin scheduling** and **First come, first served(FIFO)**.

### Rationals

The reason is that FIFO is the most straght forward algorithm, and Round-robin is a typical algorithm that involves "voluntarily yield"



## Algorithms explanation

###  First come, first served(FIFO)

The pseudo code of FIFO is below

```
pick a task in task_list
while not all task in task_list are finished
		if present_time > task.arrival_time:
				schedule task
		else:
				free cpu untill present_time >= task.arrival_time
				schedule task
		pick next task in task_list
```

Note that becuase at one time cpu can only process one task, if a task arrives but to see the cpu is busy, it will be delayed and it will occupy the cpu later, which may result in delaying other tasks.

More here https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics)

Try these sets of tasks in the visualization app:

```
not piled up:
	(3,1,1), (6,5,1), (2,14,1)

piled up:
	(8,1,1), (6,5,1), (2,14,1)
```



### Round Robin

When scheduling with Round Robin, every task is subject to a "max fragment time". After passing the max fragment time, if the task has not been done, then the CPU will go to do other tasks and after a whole round, the CPU will come back to you and proceed on. The motivation behind this is to avoid one task occupying the CPU for too long time, creating a more fair situation for each task.

More here https://en.wikipedia.org/wiki/Round-robin_scheduling

However, if every task does not execced the max fragment time in this case it's 8, then the scheduling will look nothing like "take turns" and will be the same as the result from FIFO.

Try these sets of tasks in the visualization app:

```
Round Robin Kicks in:
	(15,1,1), (10,6,1), (4,10,1)

Round Robin NOT Kicks in:
	(7,1,1), (8,6,1), (4,10,1)
```



## Explore yourself

In the visualization application, you can save the "overall waiting time" and "average waiting tasks number" and compare these data accross different scheduling algorithms or tasks input.

Do you find some patterns? If so, what is it? If not, can you change the factor to plot and find it?

Hint: First try to find the comparison of different algorithms on the same tasks list. Then do more comparisons across many tasks input. Do you see scattering?