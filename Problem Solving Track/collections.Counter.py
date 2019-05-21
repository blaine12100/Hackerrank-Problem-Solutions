# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

no_of_shoes=int(input())

shoes_collection=list(map(int,input().split()))

no_of_customers=int(input())

shoes_mapped=Counter(shoes_collection)

money_made=0

for i in range(no_of_customers):
    shoe_size,payMoney=map(int,input().split())

    # print(shoe_size,payMoney)

    if shoes_mapped[shoe_size]!=0:
       money_made+=payMoney
       shoes_mapped[shoe_size]-=1 

print(money_made)
