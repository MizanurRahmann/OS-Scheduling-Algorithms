# OS-Scheduling-Algorithms

## 1. First Come First Serve:
In this algorithm, jobs are always executed on a first-come, first-serve basis. As the process enters the ready queue, its Process Control Block is linked with the tail of the queue. So, when CPU becomes free, it should be assigned to the process at the beginning of the queue.

| Process | ArrivalTime | BurstTime | CompletionTime | TurnAroundTime | WaitingTime |
|---------|-------------|-----------|----------------|----------------|-------------|
|1|0|3|3|3|0|
|2|2|3|6|4|1|
|3|8|4|12|4|0|
|4|9|4|16|7|3|

However, this method is poor in performance, and the general wait time is quite high. The FirstComeFirstServe.py program may be run like this
```
Enter number of process: 4       
Enter Arrival time and Burst time with space: 
0 3
2 3
8 4
9 4

Solution: 
Average Total arrival time: 4.5
Average Waiting time: 1.0

P       AT      BT      TAT     WT

1       0       3       3       0
2       2       3       4       1
3       8       4       4       0
4       9       4       7       3
```