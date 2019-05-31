no_of_stamps = int(input())

stamp_collection = set()

for _ in range(no_of_stamps):
    stamp_collection.add(input())

print(f"{len(stamp_collection)}")

