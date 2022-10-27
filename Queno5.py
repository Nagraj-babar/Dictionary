# Write a python program to print all key names in the dictionary, one by one.
# There are two ways to do that 1) Using for loop 2)using dict object method.
d1={101:'Ram',102:'Laxman',103:'Bharath'}
for k in d1:
    print(k)


print(d1.keys())  # Secound method call dict_keys class object and show result in tuple format 