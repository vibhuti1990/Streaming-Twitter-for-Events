# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 12:53:41 2017

@author: Vibhuti
"""
#Read Json file into a text file
import json 
with open('stream_trump.json', 'r') as f:
    line = f.readline() # read only the first tweet/line
    tweet = json.loads(line) # load it as Python dict
    with open('python.txt', 'w') as f:
                f.write(json.dumps(tweet,indent=4))
    print(json.dumps(tweet, indent=4)) # pretty-print