# Enter your code here. Read input from STDIN. Print output to STDOUT


def Ranking(X, n):
    x_rank = dict((x, i+1) for i, x in enumerate(sorted(set(X))))
    return [x_rank[x] for x in X]


items = int(input())
listX = list(map(float, input().split()))
listY = list(map(float, input().split()))


Xrank = Ranking(listX, items)
Yrank = Ranking(listY, items)

rank_diff = 0

for i in range(items):
    rank_diff += (Xrank[i]-Yrank[i])**2

SpearmanCoefficient = 1-(6*(rank_diff)/(items*(items**2)-1))
print(round(SpearmanCoefficient, 3))
