# Write a python program to get the key of lowest value from the dictionary.sample_dict = {'C': 92,'Java': 66,'Python': 85}
sample_dict = {'C': 92,'Java': 66,'Python': 85}
a=(min(sample_dict.values()))
for b in sample_dict:
    c=sample_dict[b]
    if a==c:
        print("Key value of",a ,"is",b)

