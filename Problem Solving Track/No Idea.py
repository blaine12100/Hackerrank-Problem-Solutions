"""We cannot do this with the intersections approach as if we do that,we missout on the duplicate
values which can exist in the main input list."""

array_size, set_size = map(int, input().split())

array_elements = map(int, input().split())

setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

happiness_count = 0

for item in array_elements:
    if item in setA:
        happiness_count += 1

    elif item in setB:
        happiness_count -= 1

print(happiness_count)
