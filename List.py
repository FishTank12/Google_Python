# The below examples are ways we can display strings 
# mylist = ["a", "b", "c", "d", "e"]
# print(mylist[1])


# The below examples are ways we can "change" or manipulate lists
# mylist = ["a", "b", "c", "d", "e"]
# mylist[1] = 7
# print(mylist)

# my_list = ["a", "b", "c", "d", "e"]
# my_list[2:5] = [1, 3, 5]
# print(my_list)

# We can also insert new data into a list 
# mylist = ["a", "b", "c", "d", "e"]
# my_list.insert(2, 7)
# print(my_list) 

# We can also remove data from a list
# mylist = ["a", "b", "c", "d", "e"]
# my_list.remove("a") 
# print(my_list)


# Exercise 1:
# Create a list of your favorite fruits, then print the third item from the list.
my_favorite_fruits = ["apples", "bananas", "strawberry", "pineapples", "lemon"]
print(my_favorite_fruits[2])  # Corrected to get the third item


# Exercise 2:
# Create a list of numbers from 1 to 5, change the second item to 10, and print the list.
list_of_numbers = [1, 2, 3, 4, 5]
list_of_numbers[1] = 10
print(list_of_numbers)


# Exercise 3:
# Create a list of 5 numbers and replace the last two elements with a string of your choice. Print the result.
list_of_Five = [1, 2, 3, 4, 5]
list_of_Five[3:5] = ["your_string_here", "another_string"]
print(list_of_Five)


# Exercise 4:
# Create a list of animals and insert a new animal name in the middle of the list. Print the updated list.
list_of_animals = ["cat", "dog", "elephant", "lion", "tiger"]
list_of_animals.insert(2, "giraffe")  # Inserting in the middle (index 2)
print(list_of_animals)


# Exercise 5:
# Create a list of numbers and remove the largest number from the list. Print the list afterward.
list_of_numbers = [3, 5, 2, 8, 1, 9]
list_of_numbers.remove(max(list_of_numbers))  # Remove the largest number
print(list_of_numbers)
