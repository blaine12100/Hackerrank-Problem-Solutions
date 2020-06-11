def is_multiple(n, m):

    """
    In this function,we need to check if n is a multiple of M.To do so,
    what we can check is that if n%m ==0,that means that the remainder of division
    is zero so the quotient will be number of times n=mi
    """

    # if n % m == 0:
    #     return True
    # else:
    #     return False

    return True if int(n) % int(m) == 0 else False


def is_even(k):

    """
    The challenge here is to check if a number is even or not but multiplication,
    modulo and division cannot be used. 

    https://www.geeksforgeeks.org/check-if-a-number-is-odd-or-even-using-bitwise-operators/
    
    Based on this logic. I tried to use bitwise operators but did not spot the pattern

    What happens is that once we do the number xor with 1,if it's an even number,the final
    output will be n+1 else it will be n-1 for odd numbers
    """

    return True if k ^ 1 == k + 1 else False


def minmax(items):
    """
    We need to return the min and max numbers in the items list without using the min/max
    function
    """

    # Keeping first number so number will get initially initialized from our numbers sequence
    min_number, max_number = items[0], 0

    for item in items:
        if item > max_number:
            max_number = item
        if item < min_number:
            min_number = item
    return min_number, max_number


def sum_squares_naive(n):

    """
    In this,we need to calculate the sum of squares for all integers less than N
    """
    square_sum = 0
    for item in range(n):
        square_sum += pow(item, 2)
    return square_sum


# a, b = input().split()
# print(a, b)
# op = is_multiple(a, b)
# print(op)

# list_numbers = [100, -401, 2, 20, 100, -1, 0.33, 101.234]
op = sum_squares_naive(int(input()))
print(op)
