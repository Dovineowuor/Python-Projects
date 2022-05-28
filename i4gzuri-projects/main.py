# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
# [assignment] Add your code here

# Prompt user for input
        str1 = input(str())
        str2 = input(str())

        # convert both the strings into lowercase
        str1 = str1.lower()
        str2 = str2.lower()

        # check if length is same
        if(len(str1) == len(str2)):

            # sort the strings
            sorted_str1 = sorted(str1)
            sorted_str2 = sorted(str2)

            # if sorted char arrays are same
            if(sorted_str1 == sorted_str2):
                print(str1 + " and " + str2 + " are anagram.")
            else:
                print(str1 + " and " + str2 + " are not anagram.")

        else:
            print(str1 + " and " + str2 + " are not anagram.")

        return True
print("Enter your string below:")
print("This shows that it is ", find_anagram("", "") )