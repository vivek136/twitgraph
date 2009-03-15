#!/usr/bin/env python

import datetime
import os

from google.appengine.ext import webapp


class BaseHandler(webapp.RequestHandler):
  """A base class for all twitgraph servlets"""

  def get_start(self):
    start = self.request.get('start')
    return start or datetime.date.today().strftime("%Y-%m-%d")

  def get_end(self):
    end = self.request.get('end')
    return end or datetime.date.today().strftime("%Y-%m-%d")

  def get_q(self):
    q = self.request.get('q')
    return q or "youtube annotations"

  def get_template_values(self):
    r = self.request

    if r.get('dynamic_date') == '0':
      dynamic_date = False
    else:
      dynamic_date = True

    duration = r.get('duration')
    if not duration:
      duration = 7

    template_values = {
      'q': self.get_q(),
      'dynamic_date': dynamic_date,
      'show_text': self.get_show_text(),
      'duration': duration or 0,
      'start': r.get('start'),
      'end': r.get('end'),
      'version': os.environ['CURRENT_VERSION_ID'],
      'base_url': 'http://%s' % self.get_host_name(),
    }
    return template_values


  def get_show_text(self):
    return self.request.get('show_text') == "1"

  def get_host_name(self):
    if os.environ.get('HTTP_HOST'):
      url = os.environ['HTTP_HOST']
    else:
      url = os.environ['SERVER_NAME']
    return url
