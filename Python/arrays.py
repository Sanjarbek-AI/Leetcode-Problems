# Python has so many awesome array methods that can help to solve problems
# This is the list of them

exp_list = ["apple", "banana", "1", "2"]
cars = ['Ford', 'BMW', 'Volvo']

# append => helps to add new element to the array
exp_list.append("grapes")

# insert => helps to add new element in order you gave
exp_list.insert(0, "pear")

# remove => helps to remove element from exist list by name of element
exp_list.remove("apple")

# pop => helps to remove element by it's id
exp_list.pop(-1)

# clear => removes all the elements from the list
# exp_list.clear()

# copy => helps to creat the copy of it
new_list = exp_list.copy()

# count => returns the number of element which is specified in it
count = exp_list.count("banana")

# extent => add to list elements to second one
exp_list.extend(cars)

# index => helps to find the index of specified element
index_of_banana = exp_list.index("banana")

# reverse => helps to return list elements indexes reversing
exp_list.reverse()

# sort => return sort of the list. If elements are string they will sort by alphabet
exp_list.sort()


print(count)
print(index_of_banana)
print(exp_list)

#################################################################################################
import array

arr = array.array('j', ['a', 'b', 'c'])

for j in arr:
    print(j)