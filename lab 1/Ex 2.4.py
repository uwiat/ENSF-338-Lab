# EX 2.4
import timeit
file = open('pg2701.txt', encoding="utf8")


content = file.readlines()
#Loads the file in an array with each element representing one line.
lines= content[40:22313]
#joins all the words into a large string
str =  ' '.join(lines)
#split the large string into seperate characters in the list
words= str.split()
str =  ' '.join(words)
letters= list(str)



#states the different possible vowels that are being counted
vowels = "aAeEiIoOuUyY"

#Finds the total number of vowels in the text by iterating over the array of characters
vcount = sum(word.count(vowel) for word in words for vowel in vowels)
print('The time it take to compute the average number of vowels',timeit.timeit(lambda:vcount ))
print('The average time it take to compute the average number of vowels in 100 runs',timeit.timeit(lambda:vcount ,number=100 ))

#Finds the average number of vowels per word from the text
avg = vcount / len(words)

# Prints out the statements
print('Total Number of words in the text: ',len(words))

print ("The Total number of vowels in each word is:",vcount)

print("The Average number of vowels per word in the text is ",avg)
