#!/bin/python3

import math


def distance_pts(pts_grid, distance_pt):

    """
    Function to Get distance between 2 points on a grid of possible directions

    pts_grid:Dictionary to accept a List of directions along with it's coordinates

    Distance_pt:Point which is dirty in nature
    """

    new_dict = {}

    for key, value in pts_grid.items():
        distance = math.sqrt(
            ((distance_pt[0] - value[0]) ** 2) + ((distance_pt[1] - value[1]) ** 2)
        )
        new_dict[key] = distance

    min_key = min(new_dict.keys(), key=(lambda x: new_dict[x]))

    return min_key


def nextMove(posr, posc, board):

    """
    Function using which we decide in which  direction do we need to move.
    posr:Row Position of the Bot
    posc:Column position of the Bot
    Board:Grid for Playing 
    """

    for index, item in enumerate(board):

        """
        Getting the Row and column index of the dirty cell
        """

        if "d" in item:

            d_index = item.index("d")
            row_index = index
            break

    """
    Top Row Case
    """

    if (posr - 1) <= -1:

        distance_dict = {}

        if (posc - 1) <= -1:

            """
            First Column Case
            """

            down_direction = (posr + 1, posc)
            right_direction = (posr, posc + 1)
            distance_dict = {"DOWN": down_direction, "RIGHT": right_direction}

        elif (posc + 1) >= 5:

            """
            Last Column Case
            """

            down_direction = (posr + 1, posc)
            left_direction = (posr, posc - 1)
            distance_dict = {"DOWN": down_direction, "LEFT": left_direction}

        else:

            """
            Other Column Case
            """

            down_direction = (posr + 1, posc)
            right_direction = (posr, posc + 1)
            left_direction = (posr, posc - 1)

            distance_dict = {
                "DOWN": down_direction,
                "RIGHT": right_direction,
                "LEFT": left_direction,
            }

    elif (posr + 1) >= 5:

        """
        Bottom Row Case
        """

        distance_dict = {}

        if (posc - 1) <= -1:

            """
            First Column Case
            """

            up_direction = (posr - 1, posc)
            right_direction = (posr, posc + 1)
            distance_dict = {"UP": up_direction, "RIGHT": right_direction}

        elif (posc + 1) >= 5:

            """
            Last Column Case
            """

            up_direction = (posr - 1, posc)
            left_direction = (posr, posc - 1)
            distance_dict = {"UP": up_direction, "LEFT": left_direction}

        else:

            """
            Other Column Case
            """

            up_direction = (posr - 1, posc)
            left_direction = (posr, posc - 1)
            right_direction = (posr, posc + 1)
            distance_dict = {
                "UP": up_direction,
                "RIGHT": right_direction,
                "LEFT": left_direction,
            }

    else:

        """
        All Other Rows cases
        """

        distance_dict = {}

        """
        Column Cases are the same as above
        """

        if (posc - 1) <= -1:

            up_direction = (posr - 1, posc)
            down_direction = (posr + 1, posc)
            right_direction = (posr, posc + 1)
            distance_dict = {
                "UP": up_direction,
                "RIGHT": right_direction,
                "DOWN": down_direction,
            }

        elif (posc + 1) >= 5:

            up_direction = (posr - 1, posc)
            left_direction = (posr, posc - 1)
            down_direction = (posr + 1, posc)
            distance_dict = {
                "UP": up_direction,
                "LEFT": left_direction,
                "DOWN": down_direction,
            }

        else:

            up_direction = (posr - 1, posc)
            right_direction = (posr, posc + 1)
            down_direction = (posr + 1, posc)
            left_direction = (posr, posc - 1)

            distance_dict = {
                "UP": up_direction,
                "LEFT": left_direction,
                "DOWN": down_direction,
                "RIGHT": right_direction,
            }

    # print(distance_dict,(row_index,d_index))
    move_direction = distance_pts(distance_dict, (row_index, d_index))
    # print(move_direction)

    if (row_index, d_index) == (posr, posc):
        print("CLEAN")

    else:
        print(move_direction)


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
