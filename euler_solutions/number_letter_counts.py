number_dictionary = {
    "ones": {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
    },
    "tens": {
        "10": "ten",
        "11": "eleven",
        "12": "twelve",
        "13": "thirteen",
        "14": "fourteen",
        "15": "fifteen",
        "16": "sixteen",
        "17": "seventeen",
        "18": "eighteen",
        "19": "nineteen",
        "2": "twenty",
        "3": "thirty",
        "4": "forty",
        "5": "fifty",
        "6": "sixty",
        "7": "seventy",
        "8": "eighty",
        "9": "ninety",
    },
}

word_count = 0
tens_list = ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]

for number in range(1, 1001):
    str_number = str(number)

    # Ones Case
    if len(str_number) == 1:
        print(number_dictionary["ones"][str_number], str_number)
        word_count += len(number_dictionary["ones"][str_number])

    # Tens Case
    elif len(str_number) == 2:
        if str_number in tens_list:
            print(number_dictionary["tens"][str_number], str_number)
            word_count += len(number_dictionary["tens"][str_number])

        else:
            # Twenty/Thirty etc case
            if str_number[1] == "0":
                if str_number[0] == "2":
                    print("Twenty", str_number)
                    word_count += len("Twenty")
                elif str_number[0] == "3":
                    print("Thirty", str_number)
                    word_count += len("Thirty")
                if str_number[0] == "4":
                    print("Forty", str_number)
                    word_count += len("Forty")
                if str_number[0] == "5":
                    print("Fifty", str_number)
                    word_count += len("Fifty")
                if str_number[0] == "6":
                    print("Sixty", str_number)
                    word_count += len("Sixty")
                if str_number[0] == "7":
                    print("Seventy", str_number)
                    word_count += len("Seventy")
                if str_number[0] == "8":
                    print("Eighty", str_number)
                    word_count += len("Eighty")
                if str_number[0] == "9":
                    print("Ninety", str_number)
                    word_count += len("Ninety")

            else:
                # Normal Case
                print(
                    number_dictionary["tens"][str_number[0]]
                    + number_dictionary["ones"][str_number[1]],
                    str_number,
                )
                word_count += len(
                    number_dictionary["tens"][str_number[0]]
                    + number_dictionary["ones"][str_number[1]]
                )
    # Hundreds Case
    elif len(str_number) == 3:
        if str_number[1] == "0" and str_number[2] == "0":
            print(number_dictionary["ones"][str_number[0]] + "Hundred", str_number)
            word_count += len(number_dictionary["ones"][str_number[0]] + "Hundred")

        elif str_number[1] == "0":
            print(
                number_dictionary["ones"][str_number[0]]
                + "Hundredand"
                + number_dictionary["ones"][str_number[2]],
                str_number,
            )
            word_count += len(
                number_dictionary["ones"][str_number[0]]
                + "Hundredand"
                + number_dictionary["ones"][str_number[2]]
            )
        # Tens Case
        elif str_number[1:] in tens_list:
            print(
                number_dictionary["ones"][str_number[0]]
                + "Hundredand"
                + number_dictionary["tens"][str_number[1:]],
                str_number,
            )

            word_count += len(
                number_dictionary["ones"][str_number[0]]
                + "Hundredand"
                + number_dictionary["tens"][str_number[1:]]
            )

        elif str_number[2] == "0":
            print(
                number_dictionary["ones"][str_number[0]]
                + "Hundredand"
                + number_dictionary["tens"][str_number[1]],
                str_number,
            )

            word_count += len(
                number_dictionary["ones"][str_number[0]]
                + "Hundredand"
                + number_dictionary["tens"][str_number[1]]
            )
        # Normal Case
        else:

            print(
                number_dictionary["ones"][str_number[0]]
                + "Hundredand"
                + number_dictionary["tens"][str_number[1]]
                + number_dictionary["ones"][str_number[2]],
                str_number,
            )

            word_count += len(
                number_dictionary["ones"][str_number[0]]
                + "Hundredand"
                + number_dictionary["tens"][str_number[1]]
                + number_dictionary["ones"][str_number[2]]
            )

    else:
        print("OneThousand", str_number)
        word_count += len("OneThousand")
print(word_count)
