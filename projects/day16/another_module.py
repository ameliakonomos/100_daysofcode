#search for a package in python packages pypi.org
#PrettyTable

#adds external object
import prettytable

from prettytable import PrettyTable
table = PrettyTable()
#new object called table

table.add_column("Name", ["Amelia", "Sidney"])
table.add_column("Age", [21, 21])

table.align = "r" #access to align attribute


print(table)