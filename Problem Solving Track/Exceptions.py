'''In this question,we will learn about exceeptions in python and how to use exceptions in order to become
a better python developer.Check this link for more information

https://docs.python.org/2/library/exceptions.html#module-exceptions
'''

no_of_cases=int(input())

for _ in range(no_of_cases):
    first,second=map(str,input().split())

    try:
        print(int(first)//int(second))

    except (ZeroDivisionError,ValueError) as e:
        print(f'Error Code: {e}')
    
    # except ValueError as f:
    #     print(f)


