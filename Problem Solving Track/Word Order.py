from collections import OrderedDict

no_cases = int(input())

word_count = OrderedDict()

for _ in range(no_cases):
    word = input()
    word_count[word] = word_count.get(word, 0) + 1

print(len(word_count), " ".join(str(e) for e in word_count.values()), sep="\n")
