import re

test_str = """11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) """

new_str = re.sub(" && ", "and", test_str)
print(new_str)

other_str = re.sub("||", "or", new_str)

# print(other_str)
