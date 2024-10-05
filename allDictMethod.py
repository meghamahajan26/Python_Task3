#get - Returns the value of the specified key

person = {'name': 'Priya', 'age': 30}
print(person.get('age'))  # Output: 30
print(person.get('address', 'Rajkot')) 

#keys - Returns a list containing the dictionary's keys

car = {'brand': 'Toyota', 'model': 'Camry', 'year': 2020}
print(car.keys())  

#values - Returns a list of all the values in the dictionary

book = {'title': '1984', 'author': 'George Orwell', 'pages': 328}
print(book.values())  

#items - Returns a list containing a tuple for each key value pair

product = {'name': 'Laptop', 'price': 1000, 'stock': 50}
print(product.items()) 

#update - Updates the dictionary with the specified key-value pairs

user = {'name': 'Bob', 'age': 25}
additional_info = {'city': 'New York', 'email': 'bob@example.com'}
user.update(additional_info)
print(user)  

# pop - Removes the element with the specified key

employee = {'name': 'Sara', 'department': 'HR', 'salary': 50000}
salary = employee.pop('salary')
print(salary)  
print(employee) 

# popitem - Removes the last inserted key-value pair

fruit = {'apple': 10, 'banana': 5, 'orange': 8}
last_item = fruit.popitem()
print(last_item)  
print(fruit)  

# setDefaukt - eturns the value of the specified key. If the key does not exist: insert the key, with the specified value

student = {'name': 'Emily'}
age = student.setdefault('age', 20)
print(age) 
print(student) 

# clear - Remove all items from the dictionary

inventory = {'apple': 10, 'banana': 5}
inventory.clear()
print(inventory) 

#copy - Returns a copy of the dictionary

phone = {'brand': 'Samsung', 'model': 'Galaxy S21'}
new_phone = phone.copy()
print(new_phone)  
