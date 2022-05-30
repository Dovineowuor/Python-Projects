from fileinput import filename


file = open(filename, "rt")
data = file.read()
words = data.split()

print('Number of words in text file :', len(words))