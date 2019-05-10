no_of_cases = int(input())

currentString = ""
previous_state = []

for i in range(no_of_cases):

    list_values = input().strip().split(' ')

    #Append Given value
    if list_values[0] == '1':

        previous_state.append(currentString)

        currentString += list_values[1]

    #Delete Element at kth value
    elif list_values[0] == '2':
        previous_state.append(currentString)
        del_index = int(list_values[1])
        pos_val = len(currentString) - del_index
        currentString = currentString[0:pos_val]

    #Print K'th element
    elif list_values[0] == '3':
        pos_val = int(list_values[1]) - 1
        print(currentString[pos_val])

    #Undo Operation
    else:
        currentString = previous_state.pop()
