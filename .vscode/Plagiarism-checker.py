#pip install -U scikit-learn
#Creating JSON to Train the Model

# Importing essential packages

import pandas as pd
import numpy as np
import re
import json
import os

# Geiting the path of the current working directory.
PATH = os.path.dirname(os.path.realpath(__file__))

# Creating a function that cleans data from yhe CSV file
def cleanText(Text):
    # Remove new lines within message
    cleanedText = Text.replace('\n',' ').lower()
    # Deal with some weird tokens
    cleanedText = cleanedText.replace("\xc2\xa0", "")
    # Remove punctuation
    cleanedText = re.sub('([,])','', cleanedText)
    # Remove multiple spaces in message
    cleanedText = re.sub(' +',' ', cleanedText)
    cleanedText = cleanedText.encode('ascii', 'ignore').decode('ascii')
    return cleanedText

# Function to collect data from the CSV file

def getData():
    df = pd.read_csv(PATH + '\\plagcheckfile.csv')
    listTexts = df['Text'].values.tolist()
    finallist=[]
    print(listTexts)
    for i in range (0,4):
        textDictionary = {"tag":i}
        listTexts_i = cleanText(listTexts[i])
        print(listTexts_i)
        textDictionary.update(texts = listTexts_i)
        finallist.append(textDictionary)
    finalDictionary={"intents":finallist}       
    return finalDictionary

#  A function to get the data and save it as Dictionary

combinedDictionary = dict()
print ('Getting Text Data')
combinedDictionary.update(getData())
print ('Total len of dictionary', len(combinedDictionary))

print ('Saving text data dictionary')
np.save(PATH + '\\textDictionary.npy', combinedDictionary)

with open(PATH + '\\file.txt', 'w') as file:
     file.write(json.dumps(combinedDictionary))

# 
#  Creating a machine learning model
# 

import nltk
from nltk.stem.lancaster import LancasterStemmer 
import numpy
import tflearn
import json
import os

# A function that stems the data

stemmer = LancasterStemmer()

# Innitializing the path

PATH = os.path.dirname(os.path.realpath(__file__))

#  Openning the created dictionary file]

with open(PATH + "\\file.txt") as file:
    dataset = json.load(file)

# Lists of essence

list_words = []
labels = []
docs_x = [] #List of all the question_patterns.
docs_y = [] #List of all the tags for specific Texts.

# Stemming and tokenisation of the data

for intent in dataset["intents"]:
    for pattern in intent["texts"]: #Stems the words. Finds the root of the word. Removes extra characters and symbols to find the root word. 
        split_words = nltk.word_tokenize(pattern) #Tokenizes the words. Breakes the words in the places of spaces and returns a list of all the words in it.
        list_words.extend(split_words) #Using instead of looping and adding one word at a time in the list. It just extends the list untill all the words are in it.
        docs_x.append(split_words) #Adding the pattern of words inside docs_x list.
        docs_y.append(intent["tag"]) #For each pattern, it says what Tag it is a part of.

    if intent["tag"] not in labels:
        labels.append(intent["tag"]) #Adds all the tags in the labels list.

list_words = [stemmer.stem(w.lower()) for w in list_words if w != "?"] #Lower cases all the words in the list_words list. 
list_words = sorted(list(set(list_words))) #Makes a set of the words to remove duplicate. This gives us the actual vocabulary size of the intent. Then converts it back to list and sorts it. 

labels = sorted(labels) #Sorts the labels where the tags are stored.

training = [] #contains the bag of words.
output = [] #The output list to choose the right tag for the output.

out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = [] #Makes a list of all the words and tells if those words are occuring to find a pattern.
    #We are representing each sentence with a list the length of the amount of words in our models vocabulary. 
    #Each position in the list will represent a word from our vocabulary. 
    #If the position in the list is a 1 then that will mean that the word exists in our sentence, if it is a 0 then the word is nor present. 

    split_words = [stemmer.stem(w.lower()) for w in doc] #Stems all the words inside docs_x list.

    for w in list_words:
        if w in split_words:
            bag.append(1) #we are putting 1 in the bag of words list for the word (already present in the vocabulary list_words) present in the pattern and 0 if it is not.
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1 #We are looking in the labels list to find were the tag is in that list. We are making that value 1 in the output row. 
    #We will create output lists which are the length of the amount of labels/tags we have in our dataset. 
    #Each position in the list will represent one distinct label/tag, a 1 in any of those positions will show which label/tag is represented.

    training.append(bag) #We are putting the bag of words in the training list. 
    output.append(output_row) #We are putting the output_row list in the output list.

    # Building a Bag of words

    def bag_of_words(s, list_words): #bag_of_words function will transform our string input to a bag of words using our created words list
        bag = [0 for _ in range(len(list_words))]

        inp_str_words = nltk.word_tokenize(s)
        inp_str_words = [stemmer.stem(word.lower()) for word in inp_str_words]

        for search_element in inp_str_words:
            for i, w in enumerate(list_words):
                if w == search_element:
                    bag[i] = 1 
                
        return numpy.array(bag)

    # Building Neural Networks

    training = numpy.array(training) #we will convert our training data and output to numpy arrays.
output = numpy.array(output)
#tensorflow.reset_default_graph() #Resetting all the previous stuffs in the graph.

net = tflearn.input_data(shape=[None, len(training[0])]) #This finds the input shape that we are expecting for the model. Each training input is gonna be of the same length, so, 0.
net = tflearn.fully_connected(net, 8) #Hidden layer with 8 neurons.
net = tflearn.fully_connected(net, 8) #Another hidden layer with 8 neurons.
net = tflearn.fully_connected(net, 8) #Another hidden layer with 8 neurons.
net = tflearn.fully_connected(net, len(output[0]), activation="softmax") #length will be how many labels (how many tags) we have. Give us probability for each neuron in the network. The higest probability will be the output.
net = tflearn.regression(net)

model = tflearn.DNN(net) #Model gets trained.

try:
    model.predict(PATH + "\\model.tflearn")
    model.load()
except:
    model.fit(training, output, n_epoch=2000, batch_size=8, show_metric=True) #Fitting our data to the model. The number of epochs we set is the amount of times that the model will see the same information while training.
    model.save(PATH + "\\model.tflearn") #we can save it to the file model.tflearn for use in other scripts.

# Plagiarism Checker Function

def check():
     
    print("Type an answer (Enter 'quit' to stop)")
    while True:
        inp = input("You: ")
        inp=inp.lower()
        if inp == "quit":
            break

        results = model.predict([bag_of_words(inp, list_words)]) #we predict the most matching text from the training dataset that matches with the input text.
        results_index = numpy.argmax(results) #we get thr index of the result.
        tag = labels[results_index] #we get the tag of the most matching text with the input text.
        
        for tg in dataset["intents"]:
            if tg['tag'] == tag:
                response = tg['texts']
        print("Most similar text to the input: ")
        print(response) #we show the most matching text with the input text. 
        split_sent_resp = nltk.sent_tokenize(response) #we divide the response text (the most matching text with the input text)
        list_sents=split_sent_resp #we put the sentenses in a different list for future work.

        split_sent_inp = nltk.sent_tokenize(inp) #we split the input text into sentenses
        len_inp=len(split_sent_inp) #number of sentenses in the input text.
        list_sents.extend(split_sent_inp)
        total_len=len(list_sents) #we get the total number of sentenses in input and response text, including the duplicate sentenses.
        set_sents=set(list_sents) #we are making the list a set, so that duplicate sentenses get deleted.
        set_len=len(set_sents)
        len_difference=total_len-set_len #this gives us the number of duplicate sentenses, i.e, the copied or plaigarized sentenses.
        plag_percent=(1-((len_inp-len_difference)/len_inp))*100
        print("The percent of plagarism in the document is: ",plag_percent)

#  After compiling the above programm for functionality you have to call the fore defined plagiarism checker function to give the appropriate findings.

ckeck()   