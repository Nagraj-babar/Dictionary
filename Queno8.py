# Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.
l1=[101,102,103]
l2=["Ram","Laxman","Bharath"]
d1={k:d for k in l1 for d in l2}
print(d1)