# class Dog:
#     """A Simple attempt to model a dog."""
#
#     def __init__(self, name, age):
#         """Initialize name and age attributes"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Simulating a dog sitting in response to a command"""
#         print(f"{self.name} is now sitting")
#
#     def roll_over(self):
#         """Simulate rolling over in response to a command"""
#         print(f"{self.name} rolled over!")

### Assignment ####

class Restaurant:
    """Creating a class Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Creating an attributes and initializing the use for the Restaurant class"""
        self.restaurant = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant} Restaurant")
        print(f"This is {self.cuisine_type} Restaurant")

    def open_restaurant(self):
        print(f"The {self.restaurant} is no open for business")

    def set_number_served(self, newNumber):
        self.number_served = newNumber
        return newNumber

    def increment_number_served(self, addNumber):
        if self.number_served <= addNumber:
            self.number_served += addNumber
            print(f"Here is the new customers server {self.number_served} after previous {restaurant.set_number_served(newNumber=self.number_served)}")


class User:
    """Creating a class for User"""

    def __init__(self, first_name, last_name, color, age, sex, likes, dislikes, ambition):
        self.fname = first_name
        self.lname = last_name
        self.color = color
        self.age = age
        self.sex = sex
        self.likes = likes
        self.dislike = dislikes
        self.profession = ambition
        self.number_served = 0
        self.money = [1, 2]

    def describe_user(self):
        print(f"My name is {self.fname} {self.lname} and i am {self.age} years old. I am {self.color} and {self.sex}")
        print(f"I like {self.likes} and dislike to be {self.dislike}")
        print(f"I will like to be {self.profession}")

    def greet_user(self):
        print(f"Hello {self.fname} {self.lname}, how are you doing?")

    def level(self, mylevel):
        if mylevel >= self.category:
            # level(mylevel):
            print(f"Increasing the level by {mylevel}")


restaurant = Restaurant("AHA", "Halal")


restaurant.describe_restaurant()

restaurant.open_restaurant()
print("Before serving any customer")
print(f"You have served this much {restaurant.number_served} customers")

restaurant.set_number_served(4)
print("After serving customers")
print(f"You have served this much {restaurant.number_served} customers")

restaurant.increment_number_served(5)
# print("\n")
#
# your_restaurant = Restaurant("D&D", "Pastry")
#
# your_restaurant.describe_restaurant()
# your_restaurant.open_restaurant()
#
# print("\n")
#
# them_restaurant = Restaurant("Pimp", "Clothing")
#
# them_restaurant.describe_restaurant()
# them_restaurant.open_restaurant()

# myUser = User("Hafeez", "Tukuru", "Black", "35", "Male", "Python Programming", "Broke", "Great Software Developer", )
#
# # myUser.describe_user()
# # print("\n")
# # myUser.greet_user()
# #
# # print("\n")
# #
# # qudus = User("Qudus", "Tukuru", "Black", "33", "Male", "Business", "Broke", "Money Making")
# #
# # qudus.describe_user()
# # print("\n")
# # qudus.greet_user()
# # # myUser.
#
# # count = User()
#
# myUser.level(10)
