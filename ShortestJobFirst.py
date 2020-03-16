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
    DATA = []
    for i in range(n):
        a,b = map(int, input().split())
        DATA.append(Data( i+1, a, b))
    
    #Declare neccessary things
    q, CT, time, pastProcess = PriorityQueue(), [0]*n, 0, 1
    q.put(DATA[0])

    #Calculate Completion Time
    while not q.empty():
        recentProcess = q.get()
        time += recentProcess.bt
        CT[recentProcess.num - 1] = time  
        #New Process Added To Queue
        while pastProcess < n and DATA[pastProcess].at < time :
            q.put(DATA[pastProcess])
            pastProcess += 1
    
    #Evaluate Turn around time and Waiting time
    TAT = [CT[i]-DATA[i].at for i in range(n)]
    WT = [TAT[i]-DATA[i].bt for i in range(n)]

    #Calculate Average turn around and waiting time and print the solutions
    averageTAT = sum(TAT) / n
    averageWT = sum(WT) / n
    print("\n\nSolution: \nAverage Total arrival time: {}\nAverage Waiting time: {}".format(averageTAT, averageWT))
    print("\nP\tAT\tBT\tCT\tTAT\tWT\t\n-------------------------------------------\n")
    for i in range(n):
        print("{}\t{}\t{}\t{}\t{}\t{}".format(i+1, DATA[i].at, DATA[i].bt, CT[i], TAT[i], WT[i]))

    