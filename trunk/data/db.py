#!/usr/bin/env python
import logging as log
from data.model import Tweet

def fetch_all_tweets():
  tweets = Tweet.all()
  log.info('All tweets: %s' % tweets)
  return tweets

def add_tweet(tweet):
  log.info('Adding tweet: %s' % tweet)
  tweet.put()
