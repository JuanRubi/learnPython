#---------------------------------------------------------------------------------------------------                         Lists - an ordered sequence of objects of any type
#---------------------------------------------------------------------------------------------------
numbers = [1,2,3,4,5]
letters = ['a','b','c']
mixed = [1,2,'a',True]

# Data Structure - a specific way to store/contain data

shopping_cart = ['notebooks','pens']
print(shopping_cart[0])

#-----------------------------------------------------------
#                   List Slicing
#-----------------------------------------------------------

cart = ['textbooks','notebooks','pens','pencils']
print(cart[0::2])

# Lists are mutable, values can be changed.
print(cart)
cart[1] = 'laptop'
print(cart)
new_cart = cart[0:3]    # List slicing creates a new list separate from existing one.
print(new_cart)

# Copying a list
# Wrong way
orig_list = [1,2,3,4]
copy_list = orig_list   # This creates a second reference to the list. 
copy_list[0] = 5        # Any changes to the list affects both variables.
print(copy_list)
print(orig_list)

# Correct way
new_list = [1,2,3,4]
right_way = new_list[:]     # Need to use slicing!
right_way[0] = 5
print(right_way)
print(new_list)



