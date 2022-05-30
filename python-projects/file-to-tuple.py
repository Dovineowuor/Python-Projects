#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys
import json

class Question:
    def __init__( self, question, answers, correctAnswer ):
        self.question = question
        self.answers  = answers
        self.correct  = correctAnswer

def askQuestion( self ):
    print( self.question )

    for i in range( len( self.answers ) ):
        print( '\t{}){}'.format( i, self.answers[i] ) )

    while True:
        try:
            answer = int( input( '\nChoose your answer!>>> ' ) )
            break
        except ValueError:
            print( 'Please type a number' )
    return True if answer == self.correct else False

def score_func():
    global score
    final_score = score / 1.0 * 100.0
    if final_score >= 75:
        print( 'You\'re killin it!' )
        print( "Your score is %d percent!" % final_score )
    elif final_score >= 51:
        print( 'You passed but you could do better!' )
        print( "Your score is %d percent!" % final_score )
    elif final_score < 50:
        print( 'You failed, really you need to study bro...' )
        print( "Your score is %d percent!" % final_score )
    else:
        print( 'Something went wrong with the calculation of your score.' )

score = 0

with open( "C:\\Users\\Users\\Desktop\\python-projects\\road_sample.txt", 'rt' ) as finput:
    questions = [Question( **args ) for args in json.load( finput )]


for q in questions:
    if( q.askQuestion() ):
        print( 'great job"!' )
        score += 1
    else:
        print( 'You\'re wrong! Please paraphrase!!' )

score_func()
quit()