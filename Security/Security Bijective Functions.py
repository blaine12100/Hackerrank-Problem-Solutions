
''' set() returns a list with only the unique entries in the list. 
so if the length of unique items == the length of the list itself 
then it contains no duplicates, otherwise it does contain duplicates. '''

n = input()  # Not really that useful to us.
inputs = input().strip().split()  # Create a list with the numbers

if len(set(inputs)) == len(inputs):
    print("YES")
else:
    print("NO")
