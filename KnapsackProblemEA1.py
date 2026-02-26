def knapsack(W, wt, val, n):
    K = [[0] * (W+1) for i in range (n+1)]
    #print(K)
    for i in range(n+1):
        for w in range(W+1):
            if(i==0 or w == 0):
                K[i][w] = 0
            elif(wt[i-1] <= w):
                K[i][w]= max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    
    for i in K:
        for c in i:
            print(c, end = " ")
        print()
    return K[n][W]

val = [20, 8, 10, 25];
wt = [3, 4, 5, 6];
W = 8
ln = len(val);
profit = knapsack(W, wt, val, ln)
print("Maximum Profit achieve with this knapsack: ")
print(profit)