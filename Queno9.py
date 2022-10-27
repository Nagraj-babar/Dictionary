# Write a python program to merge two python dictionaries into one dictionary.
d1={101:'Ram',102:'Laxman'}
d2={103:'Bharath'}
for e in d2:
    a=d2[e]
    d1[e]=a
print(d1)    