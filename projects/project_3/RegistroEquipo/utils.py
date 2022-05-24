# -*- coding: utf-8 -*-
"""
Created on Mon May  9 18:27:53 2022

@author: santi
"""

import re
import pandas as pd
import numpy as np
import string
from bs4 import BeautifulSoup


def get_bigrams(words):
    '''

    :param words: a list of words
    :return: a list of bigrams

    This function returns a list of bigrams (sets of two words) from a given list of words. For example:
    ['this', 'is', 'a', '.', 'very', 'simple', 'example', '.']
    ->
    [['this', 'is'], ['is', 'a'], ['a', '.'], ['.', 'very'], ['very', 'simple'], ['simple', 'example'], ['example', '.']]

    TODO

    Implement get_bigrams

    [10 points]
    '''
    bigrams = [list(big) for big in zip(words[:-1],words[1:])]
    
    return bigrams

def prefix_neg(words):
    '''

    :param words: a list of words to process.
    :return: a list of words with the 'neg_' suffix.

    This function receives a list of words and appends a 'neg_' suffix to every word following a negation (no, not, nor)
    and up to the next punctuation mark (., !, ?). For example:
    ['not', 'complex', 'example', '.', 'could', 'not', 'simpler', '!']
    ->
    ['not', 'neg_complex', 'neg_example', '.', 'could', 'not', 'neg_simpler', '!']

    TODO

    Implement prefix_neg

    HINT: you might find the statment 'continue' useful in your implementation, althought it is not neceessary.

    [15 points]
    '''
    after_neg = False
    proc_words = []
    for word in words:
        # YOUR CODE GOES HERE
        if word in ['not','no','nor']:
            after_neg = True
            proc_words.append(word)
            continue
        
        if word in ['.','!','?']:
            after_neg = False
            proc_words.append(word)
            continue
        
        if after_neg:
            proc_words.append('neg_'+word)
        else:
            proc_words.append(word)
    return proc_words


def filter_voc(words, voc):
    mask = np.ma.masked_array(words, ~np.in1d(words, voc))
    return mask[~mask.mask].data


def proc_text(text, sw):
    '''
        This function takes as input a non processed string and returns a list
        with the clean words.

        :param text: The text to be processed
        :param sw: A list of stop words
        :return: a list containing the words of the clean text.

        TODO

        Implement the following transformations:
        1.- Set the text to lowercase.
        2.- Make explicit negations:
              - don't -> do not
              - shouldn't -> should not
              - can't -> ca not (it's ok to leave 'ca' like that making it otherwise will need extra fine tunning)
        3.- Clean html and non characters (except for '.', '?' and '!')
        4.- Add spacing between punctuation and letters, for example:
                - .hello -> . hello
                - goodbye. -> goodbye
        5.- Truncaters punctuation and characters with multiple repetitions into three repetitions.
            Punctuation marks are consider 'multiple' with at least **two** consecutive instances: ??, !!, ..
            Characters are considre 'multiple' with at least **three**  consecutive instances: goood, baaad.
            for example:
                - very gooooooood! -> very goood
                - awesome !!!!!! -> awesome !!!
                - nooooooo !!!!!! -> nooo !!!
                - how are you ?? -> how are you ???
            NOTE: Think about the logic behind this transformation.
        6.- Remove whitespace from start and end of string
        7.- Return a list with the clean words after removing stopwords (DO NOT REMOVE NEGATIONS!) and
            **character** (letters) strings of length 2 or less. for example:
               - ll, ss
        8.- Removes any single letter: 'z', 'w', 'b', ...

    This is the most important function and the only one that will include a test case:

    input = 'this...... .is a!! .somewhat??????,, # % & messy 234234 astring... noooo.asd HELLLLOOOOOO!!! what is thiiiiiiissssss?? <an> <HTML/> <tag>tagg</tag>final. test! z z w w y y t t'

    expected_output = ['...', '.', '!!!', '.', 'somewhat', '???', 'messy', 'astring', '...', 'nooo', '.', 'asd', 'helllooo', '!!!', 'thiiisss', '???', 'tagg', 'final', '.', 'test', '!']

    [40 points]
    '''
        
    text = pd.Series(text)
    
    text = (text
                .str.join(' ')
                .str.lower()
                .str.replace(r'([0-9]+)+',r' ')
                .str.replace(r'(<[^>]*>)',r' ')
                .str.replace(r'([.?!]+)',r' \1')
                .str.replace(r'([.?!])(\w+)',r'\1 \2')
                .str.replace(r'([ ]+)', r' ')
                .str.replace(r"(\D+)(n't)",r'\1 not')
                .str.replace(r'([!,?,.])\1+', r'\1\1\1')
                .str.replace(r'([a-z])\1\1+', r'\1\1\1')
                .str.replace(r'( [a-z] \w)','')
                .str.replace(r'([^\w\s?.!]+)',r' ')
                .str.replace(r'([ ]+)', r' ')
                .apply(lambda t: [word for word in t.split() if word not in sw])
                )
    texto_procesado = text
    
    
    return texto_procesado
