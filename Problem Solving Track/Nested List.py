score_array=[]
nameandscore=[]

for _ in range(int(input())):
    name = input()
    score = float(input())
    score_array.append(score)
    nameandscore.append([name,score])

#To Remove Duplicate Entries in Scores
scorelist = list(dict.fromkeys(score_array))

#Get Second Highest from our list of values
second_highest=sorted(scorelist)[1] 

# print(scorelist,second_highest)

#Loop over our nested list structure
for name,score in sorted(nameandscore):
    #If our score is the second highest,then print the corresponding name
    if score==second_highest:
        print(name)