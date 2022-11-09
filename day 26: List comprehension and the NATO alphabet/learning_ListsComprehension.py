#create lists using list comprehension
#create a new list from a previous list without using for loop = comprehension

#syntax
#new_list = [new_item for item in list]

# numbers = [1,2,3]
# new_list = [n+1 for n in numbers]
numbers = [1,2,3,4,5,6,7]
new_numbers = [n-1 for n in numbers]

name = "Amelia"
new_listt = [letter for letter in name]
print(new_listt)

range_list = [n *2 for n in range(1,5)]
print(range_list)

#conditional list comprehension
# new_list = [new_item for item in list if test]
names = ["Amelia", "Sidney", "Tanya", "Joe", "Konomos"]
new_names = [name for name in names if len(name) < 4]
capital_names = [name.upper() for name in names if len(name) > 5]

