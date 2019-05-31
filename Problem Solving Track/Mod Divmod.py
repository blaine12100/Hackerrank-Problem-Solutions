first_number = int(input())
second_number = int(input())

divmod_output = divmod(first_number, second_number)

print(
    f"""{divmod_output[0]}
{divmod_output[1]} 
{divmod_output}"""
)

