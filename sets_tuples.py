#sets and tupules examples
#sets examples
set1 = {1,2,3,4,5}
print(set1) #{1,2,3,4,5}
print(type(set1)) # {1,2,3,4,5}
set1.add(6)
print(set1)
set1.remove(2)
print(set1)

set2 = {"apple", "banana", "cherry", "cherry"}
print(set2) #{apple', 'banana', 'cherry'}

#tuples example
tuple1 = (1,2,3,4,5)
print(tuple1)
print(type(tuple1))
#tuples are immutable, meaning they cannot be changed after creation, this makes tuples useful for storing data that shouldnt be modifed
social_secruity_number = (123444,4444445,5676789)
print(social_secruity_number)      #(123444,4444445,5676789)