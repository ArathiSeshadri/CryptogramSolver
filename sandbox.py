#code snippet to find possible substitutions
import re
cipher=input("Enter a cipher")

#delete this when the whole program is merged

#adictionary is an empty dictionary to store letters and the number of times each letter appears
adictionary=dict()

for c in cipher:                                         #c corresponds to characters in the cipher
    if c in adictionary:
        adictionary[c]=adictionary[c]+1
    else:
        adictionary[c]=1
print(adictionary)
import operator
sorted_adictionary = sorted(adictionary.items(), key=operator.itemgetter(1))
sorted_adictionary = dict(sorted(adictionary.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_adictionary)

keys=list(sorted_adictionary)             #stores the key from the dictionary as a list
while(" " in keys) :
    keys.remove(" ")                      #removes single spaces
fre = ["e","t","a","o","i","n","s","h","r","d","l","c","u","m","w","f","g","y","p","b","v","k","j","x","q","z"]
#fre is the list of letters which are arranged in the descending order of most to least used english alphabets in general
print("Before Updation...")
print(keys)
print("Printing the updated frequency list")
#keys=list(fre)
count_keys=len(keys)
keys1=fre[:count_keys]
print(keys1)
possible_solution1 = {keys[i] : keys1[i] for i in range(len(keys))}
print(possible_solution1)
