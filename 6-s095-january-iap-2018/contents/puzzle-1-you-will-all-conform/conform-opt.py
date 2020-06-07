# Programming for the Puzzled -- Srini Devadas
# You Will All Conform
# Input is a vector of F's and B's, in terms of forwards and backwards caps
# Output is a set of commands (printed out) to get either all F's or all B's
# Fewest commands are the goal

caps = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "B", "F"]
cap2 = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "F", "F"]


def pleaseConformOpt(caps):
    # Initialization
    start = 0
    forward = 0
    backward = 0
    intervals = []

    # Here we add a different element to remove the step of adding a manual element at the end
    # Since it will be different from the last element,we always ensure that we will not miss that
    # element
    caps = caps + ["END"]

    # Determine intervals where caps are on in the same direction
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            # each interval is a tuple with 3 elements (start, end, type)
            intervals.append((start, i - 1, caps[start]))

            if caps[start] == "F":
                forward += 1
            else:
                backward += 1
            start = i

    if forward < backward:
        flip = "F"
    else:
        flip = "B"
    for t in intervals:
        if t[2] == flip:
            # Exercise: if t[0] == t[1] change the printing!
            print("People in positions", t[0], "through", t[1], "flip your caps!")


def pleaseConformOnepass(caps):
    # Same Step as above(As we shall be skipping the first interval(Can have many or zero ele
    # ments))
    if caps:
        beg_index = 0
        caps = caps + [caps[0]]
        for i in range(1, len(caps)):
            # Current Index is not the same as previous
            if caps[i] != caps[i - 1]:
                # Not if it is different,but not the same as the first one.
                # So how this printing works is that whenever you have the start of the interval(When the in
                # terval begins,we print the initial index).Then once the interval ends,it will be simillar to the
                # first element and then we print the other part that is the part when the index is finished
                # Example consider the sequence B B B F F B.When we get to the first f,the previous is B and we print People in
                # positions statement.Then once we get to the second case when we have b in I and f in i-1,in that they both
                # are equal so the next statement is printed.This logic follows for both F/B in the first position

                if caps[i] != caps[0]:
                    print("People in positions", i, end="")
                else:
                    print(" through", i - 1, "flip your caps!")


# pleaseConformOpt(caps)
pleaseConformOnepass(caps)
