# import turtle
import turtle
# from turtle import Turtle, Screen
#
# timmy = Turtle()
#
# print(timmy)
#
# timmy.shape("turtle")
# timmy.color("SeaGreen")
#
# timmy.position()
#
# timmy.forward(100)
#
# my_screen = Screen()
#
# print(my_screen.canvheight)
#
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ['Staryu', 'Starmie', 'Houndour'])
table.add_column("Type ", ['Water', 'Water', 'Fire'])

table.align = 'l'

print(table)
