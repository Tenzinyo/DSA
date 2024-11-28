#Source:https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/

def printMaxActivities(s, f):
    n=len(f)
    i = 0
    for j in range(1, n):
        if s[j] >= f[i]:
            i = j
if __name__ == '__main__':
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]
    printMaxActivities(s, f)
