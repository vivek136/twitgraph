#!/usr/bin/env python

from google.appengine.ext import db

class Tweet(db.Model):
  text = db.StringProperty(multiline=True)
  sentiment = db.StringProperty() # one of pos/neg/neu
