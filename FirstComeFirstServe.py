if __name__ == '__main__':
    n = int(input("Enter number of process: "))
    
    #After getting arraival time and burst time, sort them on the basis of arrival time
    DATA = []
    print("Enter Arrival time and Burst time with space: ")
    for i in range(n):
        DATA.append(list( map(int, input().split()) ))   
    DATA.sort(key = lambda x: x[0])
    
    #Calculate Completion time
    CT = []
    CT.append(DATA[0][1])
    for i in range(1,n):
        if DATA[i][0] < CT[i-1]:
            CT.append(CT[i-1]+DATA[i][1])
        else:
            CT.append(DATA[i][0]+DATA[i][1])
    #Evaluate Turn around time and Waiting time
    TAT = [CT[i]-DATA[i][0] for i in range(n)]
    WT = [TAT[i]-DATA[i][1] for i in range(n)]

    #Calculate Average turn around and waiting time and print the solutions
    averageTAT = sum(TAT) / n
    averageWT = sum(WT) / n
    print("\n\nSolution: \nAverage Total arrival time: {}\nAverage Waiting time: {}".format(averageTAT, averageWT))
    print("\nP\tAT\tBT\tTAT\tWT\t\n")
    for i in range(n):
        print("{}\t{}\t{}\t{}\t{}".format(i+1, DATA[i][0], DATA[i][1], TAT[i], WT[i]))