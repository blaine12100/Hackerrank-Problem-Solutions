"""This code is a good refresher for Class Based programming in Python.Covers all the important
basics needed. Link for reference https://realpython.com/python3-object-oriented-programming/
"""


class Dog:

    # Class Attributes
    species = "mammals"

    # Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    # Get the max age of from all dogs
    def get_biggest_no(self, *args):
        max_age = max(*args)

        print(f"The oldest dog is {max_age} years old")

    # Class Method
    def description(self):
        print(f"{self.name} is {self.age} years old")

    # Class Method
    def speak(self, sound):
        print(f"{self.name} says {sound}")

    def eat(self, status):
        self.is_hungry = status

    def walk(self):
        print(f"{self.name} is walking")


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


class Pets:
    def __init__(self, other_instances):
        self.other_instances = other_instances

    def walk(self):
        print("method Called")
        for item in self.other_instances:
            item.walk()

    def show_results(self):
        no_pets = len(self.other_instances)
        print(f"I have {no_pets} pets")

        for item in self.other_instances:
            if item.is_hungry:
                item.eat(False)
            else:
                pass

            print(f"{item.name} is {item.age} yrs old")

        print(f"And they are all {item.species} of course")

        if all(item.is_hungry == False for item in self.other_instances):
            print("My Dogs are not hungry")

        else:
            print("My Dogs are hungry.Please Feed them")


first_dog = Dog("philo", 5)
second_dog = Dog("milo", 15)
third_dog = Dog("lilo", 30)

# first_dog.get_biggest_no(first_dog.age,second_dog.age,third_dog.age)

second_dog.description()

third_dog.speak("Bow Wow")

all_pets = Pets([first_dog, second_dog, third_dog])

all_pets.show_results()

all_pets.walk()

# first_dog.run("fast")

# new_dog=Bulldog("Bull",12)

# print(new_dog.run("fast"))

# Used to check if an object is an instance of a particular class

# print(isinstance(new_dog,Bulldog))
