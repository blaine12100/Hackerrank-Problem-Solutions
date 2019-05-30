import cmath

complex_input=complex(input())

polar_cooridnates=cmath.polar(complex_input)

print(polar_cooridnates[0],polar_cooridnates[1],sep="\n")

