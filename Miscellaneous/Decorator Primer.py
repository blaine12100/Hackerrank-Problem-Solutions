"""In this section,a small example for a decorator shall be demonstrated.This is asked quite often
in interviews as it is an advanced Python Concept.Will also check conditional decorators nd stuff

https://realpython.com/primer-on-python-decorators/

Inner Functions:These are functions which are defined inside other Functions.Simillar to hwo
we can define a Node class inside a Linked list class as its inner representation

"""


def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()


# parent()

"""Decorator:

A Decorator is basically a tag which is used on top of functions normally.It's use is that when a 
decorator is used,the function on top of which the decorator is used is called first and then 
the function for which the decorator is defined is called.This makes it extremely useful for cases
when you always need to call like a parent function before the child function is called.

In our example,we have defined a function called validate_func function which needs 2 arguments.These args
are then passed on to our new function decorator which in turn receives the arguments passed to the
valdiate_func function as its parameters.

The decorator name and the decorated function name have to be the same else we get a value undefined error
"""


sample_input = [1, 2, 3, 4, 5, 6, 33, 66, 99]


def execute_something(validate_func):
    def working_function(abcd, other):

        print("Decorator Called", other)

        """This is done so that we can return a value from the decorated function.
        This value can then be accessed as apart of the values received when this function
        is called with a variable assigned to it so that it can use this return value.


        Is it possible to return the value of a decorator function to be used in the function
        which has been decorated?"""

        return validate_func(abcd, other), other

    return working_function


@execute_something
def validate_func(first, second):
    print("parent Called", first, second)

    return True


abc = validate_func(sample_input, "2")

print(abc)
