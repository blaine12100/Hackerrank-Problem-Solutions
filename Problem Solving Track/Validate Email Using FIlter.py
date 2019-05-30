import re

def fun(s):

    expression="[\w,-]+@[a-z,A-Z,0-9]+\..{0,3}$"

    compiled_pattern=re.compile(expression)

    return re.match(expression,s)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)