import string

original_dictionary = {item: i for i, item in enumerate(string.ascii_letters)}
# print(original_dictionary)

original_list = string.ascii_letters

new_dictionary = {
    key: string.ascii_letters[(value + 3) % 26]
    for key, value in original_dictionary.items()
}

new_list = "".join(
    x
    for x in [
        string.ascii_letters[(value + 2) % 26]
        for key, value in original_dictionary.items()
    ]
)

# print(new_dictionary, new_list, original_list)

translation_table = str.maketrans(original_list, new_list)
test_str = "middle-Outz"

traanslation = test_str.translate(translation_table)
print(traanslation)

res = ""
for i in s:
    if i.isalpha():
        # For adding or Subtracting the Appropriate value(Accounting for the Shift between
        # Uppercase and lowercase.This is what I was missing in my earlier solution above)
        a = "A" if i.isupper() else "a"
        res += chr(ord(a) + (ord(i) - ord(a) + k) % 26)
    else:
        res += i
return res
