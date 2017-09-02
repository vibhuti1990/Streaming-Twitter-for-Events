# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 12:56:47 2017

@author: Vibhuti
"""
#Counting terms
import re
 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

import json
with open('stream_HoustonFloods.json', 'r') as f:
    for line in f:
#        print(line)
        tweet = json.loads(line)
        tokens = preprocess(tweet['text'])
        print(tokens)


#Remove stopwords
from nltk.corpus import stopwords
import string
 
punctuation = list(string.punctuation)  #creates a list of punctation
stop = stopwords.words('english') + punctuation + ['rt','RT' 'via','…']
#create a list of stop words
terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]

import operator 
import json
from collections import Counter
 
fname = 'stream_HoustonFloods.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with stop words
        terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
        # Update the counter
        count_all.update(terms_stop)
    # Print the first 5 most frequent words
    print(count_all.most_common(5))


#######Get the specific terms#############################  
#Create the list of all terms  
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        terms_all = [term for term in preprocess(tweet['text'])]
        terms_single = set(terms_all) 
        # Update the counter
        count_all.update(terms_all)
    # Print the first 5 most frequent words
    print(count_all.most_common(5))
# Count terms only once, equivalent to Document Frequency
terms_single = set(terms_all)
    
    
# Count hashtags only
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
#        terms_all = [term for term in preprocess(tweet['text'])]
        terms_hash = [term for term in preprocess(tweet['text']) 
              if term.startswith('#')]
        # Update the counter
        count_all.update(terms_hash)
    # Print the first 5 most frequent words
    print(count_all.most_common(5))

# Count terms only (no hashtags, no mentions)
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
#        terms_all = [term for term in preprocess(tweet['text'])]
        terms_only = [term for term in preprocess(tweet['text']) 
              if term not in stop and
              not term.startswith(('#', '@'))] 
        # Update the counter
        count_all.update(terms_only)
    # Print the first 5 most frequent words
    print(count_all.most_common(5))


#Sequence of two terms
from nltk import bigrams 
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with stop words
        terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
        terms_bigram = bigrams(terms_stop)
        # Update the counter
        count_all.update(terms_bigram)
    # Print the first 5 most frequent words
    print(count_all.most_common(5))
              
              
              




