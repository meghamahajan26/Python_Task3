# append()

fruits = ['apple', 'banana']
fruits.append('cherry')
print(fruits)  

# extend()

list1 = [1, 2, 3]
list2 = [4, 5]
list1.extend(list2)
print(list1) 

#insert()

numbers = [1, 3, 4]
numbers.insert(1, 2) #inserting 2 in index1
print(numbers) 

#remove()

animals = ['cat', 'dog', 'fish', 'dog']
animals.remove('dog')  
print(animals)  
---#removes first dog
        
#pop() 

colors = ['red', 'green', 'blue', 'yellow']
popped_color = colors.pop(2)  # removes blue
print(popped_color) 
print(colors)  

#sort

scores = [88, 95, 72, 100]
scores.sort(reverse=True)  #sort list in descending order
print(scores)  

 #reverse
 
letters = ['a', 'b', 'c', 'd']
letters.reverse()
print(letters)  

#index

nums = [10, 20, 30, 40, 50]
idx = nums.index(30)
print(idx) 

#count

letters = ['a', 'b', 'a', 'c', 'a']
count_a = letters.count('a')
print(count_a)  

#clear

items = ['pen', 'pencil', 'eraser']
items.clear()
print(items) 
