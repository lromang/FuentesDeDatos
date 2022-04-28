import re
import pandas as pd
import numpy as np


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
    bigrams =  # YOUR CODE GOES HERE
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

    words = # YOUR CODE GOES HERE

    return words

