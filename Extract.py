# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 16:48:28 2017

@author: Vibhuti
"""
#This is streaming API that keeps the connection open to extract upcoming tweets of an event 
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import argparse
#create below file with twitter data
import string
import config     #Authorises our app to access Twitter on our behalf, we need to use the OAuth 
import json
def get_parser():
    """Get parser for command line arguments."""
    parser = argparse.ArgumentParser(description="Twitter Downloader")
    parser.add_argument("-q",
                        "--query",
                        dest="query",
                        help="Query/Filter",
                        default='-')
    parser.add_argument("-d",
                        "--data-dir",
                        dest="data_dir",
                        help="Output/Data Directory")
    return parser

class MyListener(StreamListener):
    """Custom StreamListener for streaming data."""

#create the file where data will streaming data will be stored in JSON format
    def __init__(self, data_dir, query):
        query_fname = format_filename(query)
        self.outfile = "%s/stream_%s.json" % (data_dir, query_fname)

#Write the data into the JSON file
    def on_data(self, data):
        try:
            with open(self.outfile, 'a') as f:
                f.write(data)
                print(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True
#Display error in case of file error
    def on_error(self, status):
        print(status)
        return True


def format_filename(fname):
    """Convert file name into a safe string.
    Arguments:
        fname -- the file name to convert
    Return:
        String -- converted file name
    """
    return ''.join(convert_valid(one_char) for one_char in fname)


def convert_valid(one_char):
    """Convert a character into '_' if invalid.
    Arguments:
        one_char -- the char to convert
    Return:
        Character -- converted char
    """
    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
    if one_char in valid_chars:
        return one_char
    else:
        return '_'

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)
    api = tweepy.API(auth)
# run from command prommp ||||||python twitter_stream_download.py -q cricket(replace this with any term you want to search) -d data
    twitter_stream = Stream(auth, MyListener(args.data_dir, args.query))
    twitter_stream.filter(track=[args.query])







