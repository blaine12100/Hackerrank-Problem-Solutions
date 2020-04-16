main_list = list(range(99))

split_list = int(input())

# My Solutions

new_list = []

index = split_list

prev_index = 0

for item in range(1, len(main_list)):
    new_list.append(main_list[prev_index:index])
    prev_index += split_list
    index += split_list

    if index > len(main_list):
        new_list.append(main_list[prev_index:])
        break

print(new_list)

# Latest Solution(Why Did not think of this yesterday)
new_list = [main_list[item : item + split_list] for item in main_list[::split_list]]
print(new_list)


# A Little Unsure about this one since it's a long time since I have used Signed
# or Unsigned Integers

signed_int = -1
unsigned_int = signed_int + 2 ** 32

print(unsigned_int)
