from fileinput import filename


prophecy = input(filename())

vowel_count = 0

# TODO: set the value of vowel_count to be the number of vowels in prophecy


# :

vowel_count += prophecy.count('a')
vowel_count += prophecy.count('A')
vowel_count += prophecy.count('e')
vowel_count += prophecy.count('E')
vowel_count += prophecy.count('i')
vowel_count += prophecy.count('I')
vowel_count += prophecy.count('o')
vowel_count += prophecy.count('O')
vowel_count += prophecy.count('u')
vowel_count += prophecy.count('U')

'''
Looking at this first attempt, I think I can make it better. Counting 
both lower-case 'a' and upper-case 'A', seems unnecessary. I'll convert 
everything to lower-case, and then I only need to count each vowel once!
'''

vowel_count = 0
lower_prophecy = prophecy.lower()
vowel_count += lower_prophecy.count('a')
vowel_count += lower_prophecy.count('e')
vowel_count += lower_prophecy.count('i')
vowel_count += lower_prophecy.count('o')
vowel_count += lower_prophecy.count('u')
print(vowel_count)
