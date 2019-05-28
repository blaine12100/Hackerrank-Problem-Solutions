def print_formatted(number):

    for i in range(1,number+1):
        decimal=i
        binary=bin(i)
        octal=oct(i)
        hexadecimal=hex(i).upper()

        #Integer bit_length method allows you to query the number of bits required to represent a number's value in binary. 
        
        width = number.bit_length()

        print(f'{decimal:>{width}} {octal[2:]:>{width}} {hexadecimal[2:]:>{width}} {binary[2:]:>{width}}')
        
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

    