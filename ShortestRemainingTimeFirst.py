from queue import PriorityQueue

class Data(object):
    def __init__(self, num, at, bt):
        self.num = num
        self.at = at
        self.bt = bt

    def __lt__(self, other):
        return (self.bt < other.bt)

if __name__ == "__main__":
    n = int(input("Enter number of process: "))

    #Get ArrivalTime and BurstTime
    DATA, BT = [], []
    for i in range(n):
        a,b = map(int, input().split())
        DATA.append(Data( i+1, a, b))
        BT.append(b)
    
    #Declare neccessary things
    q, CT, RT, time = PriorityQueue(), [0]*n, [-1]*n, 0
    nextProcess, processTermination = DATA[1], 0
    q.put(DATA[0])
    RT[0] = DATA[0].at

    #Calculate Completion Time
    while processTermination != n:
        time += 1
        if not q.empty():
            recentProcess = q.get()
            if RT[recentProcess.num - 1]==-1 and recentProcess.num!=1:
                RT[recentProcess.num-1] = time - recentProcess.at - 1
            recentProcess.bt -= 1
        
            if recentProcess.bt > 0:
                q.put(recentProcess)
            else:
                CT[recentProcess.num - 1] = time
                processTermination += 1
        
        if nextProcess.at == time:
            q.put(nextProcess)
            if nextProcess.num < n:
                nextProcess = DATA[nextProcess.num]
    #Evaluate Turn around time and Waiting time
    TAT = [CT[i]-DATA[i].at for i in range(n)]
    WT = [TAT[i]-BT[i] for i in range(n)]

    #Calculate Average turn around and waiting time and print the solutions
    averageTAT = sum(TAT) / n
    averageWT = sum(WT) / n
    print("\n\nSolution: \nAverage Total arrival time: {}\nAverage Waiting time: {}".format(averageTAT, averageWT))
    print("\nP\tAT\tBT\tCT\tTAT\tWT\tRT\n---------------------------------------------------\n")
    for i in range(n):
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(i+1, DATA[i].at, BT[i], CT[i], TAT[i], WT[i], RT[i]))
