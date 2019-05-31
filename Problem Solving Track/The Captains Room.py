"""Although this question is supposed to be solved with sets.I Found it much easier to solve
with dictionatries as opposed to sets since whenever counting in some form is involved i prefer
to user dictionaries for this purpose"""

no_of_groups = int(input())

sample_dict = {}

tourists = map(int, input().split())

for item in tourists:
    sample_dict[item] = sample_dict.get(item, 0) + 1

for key, value in sample_dict.items():
    if value != no_of_groups:
        print(key)
