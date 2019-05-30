'''In order to evaluate expression with variables,best to define the variables above
and then the eval takes care of subsituting our variables in the string expression.abs

Good for math stuff and maybe some other cases.
'''

x,k=map(int,input().split())

print(eval(input()) == k)
