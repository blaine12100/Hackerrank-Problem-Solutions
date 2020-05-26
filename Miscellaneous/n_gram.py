"""
In this question what we need to do is generate N-Grams of a Given Sentance upto the number of 
words that this sentance has(Till that gram we need to generate all grams)
"""


def generate_ngrams(data):

    # Split String based on Space
    iniital_sample_list = data.split()
    new_data_list = []
    iniital_sample_list_len = len(iniital_sample_list)
    i_index = 1

    # Initial Index to keep track of Which Gram Are we generating
    while i_index <= iniital_sample_list_len:

        # Initial Index to track the current var from which we are generating the slice
        j_index = 0

        while j_index <= iniital_sample_list_len - 1:
            data_slice = iniital_sample_list[j_index : j_index + i_index]
            if (
                data_slice
                and data_slice not in new_data_list
                and len(data_slice) == i_index
            ):
                new_data_list.append(data_slice)
            j_index += 1
        i_index += 1

    return [" ".join(str(x) for x in item) for item in new_data_list]


sample_data = input()
n_grams_generated = generate_ngrams(sample_data)
print(n_grams_generated)
