import statistics as st

n = int(input())
data = list(map(int, input().split()))
freq = list(map(int, input().split()))

new_list = []

for i in range(n):
    new_list += [data[i]] * freq[i]

MiddleValue = sum(freq)

new_list.sort()

if n % 2 != 0:
    FirstQuartile = st.median(new_list[:MiddleValue//2])
    LastQuartile = st.median(new_list[MiddleValue//2+1:])
else:
    FirstQuartile = st.median(new_list[:MiddleValue//2])
    LastQuartile = st.median(new_list[MiddleValue//2:])

op = round(float(LastQuartile-FirstQuartile), 1)
print(op)
