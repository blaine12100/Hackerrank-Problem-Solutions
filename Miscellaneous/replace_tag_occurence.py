import re


def tag_replacer(list_tags, sentance, tag):

    """
    In this,we search for the given tag in our sentance and then repalce each occurence of the tag
    with a variable and then append the remaining sentance.

    For the case when we only have a single tag and some data exists after the tag,then we
    need to append it and add it to our main string since when we create the pairs the last 
    element after the pair creation will be left.
    """

    if list_tags and sentance and tag:

        new_separated_string, combined_string = re.split(tag, sentance), ""
        print(list(zip(list_tags, new_separated_string)))
        index_iterator = 0
        for content, data in zip(list_tags, new_separated_string):
            print(content, data)
            combined_string += data + content
            index_iterator += 1
        print(new_separated_string)
        new_string_iterator = new_separated_string[index_iterator:]

        # For Single Tag Element and data after tag is present.This is done so that the data
        # After the pair is also kept.

        if new_string_iterator:
            new_temp_str = " ".join(
                str(x) for x in new_separated_string[index_iterator:]
            )
            combined_string += " " + new_temp_str
        print(combined_string)
        return combined_string

    else:
        return "Data Invalid"


sentance = input()
tag = input()
list_tags = input().split()

print(sentance, tag, list_tags)
tag_replacer(list_tags, sentance, tag)
