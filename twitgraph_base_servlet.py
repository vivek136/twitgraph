#!/usr/bin/env python

import datetime
import os

from google.appengine.ext import webapp

DATE_FORMAT = '%Y-%m-%d'

class BaseHandler(webapp.RequestHandler):
  """A base class for all twitgraph servlets"""

  def get_template_values(self):
    template_values = {
      'q': self.get_q(),
      'dynamic_date': self.is_dynamic_date(),
      'show_text': self.get_show_text(),
      'duration': self.get_duration(),
      'start': self.get_start(),
      'end': self.get_end(),
      'version': os.environ['CURRENT_VERSION_ID'],
      'base_url': 'http://%s' % self.get_host_name(),
      'css': self.get_content_css(),
    }
    return template_values

  def get_content_css(self):
    return '<style>' \
           '#twg-graph {' \
            'width: 600px;' \
            'height: 300px;' \
            'vertical-align: middle;' \
            'display:table-cell;' \
            '}' \
            '#twg-graph-pie {' \
            'width: 300px;' \
            'height: 300px;' \
            'vertical-align: middle;' \
            'display:table-cell;' \
            '}' \
            '#twg-resultsText {' \
            'font-size: 10pt;' \
            'padding: 20px;' \
            'font-family: Arial;' \
            '}' \
            '.twg-user {' \
            'color: green;' \
            'width: 150px;' \
            'display: block;' \
            'float: left;' \
            '}' \
            '.twg-learn {' \
            'width: 75px;' \
            'display: block;' \
            'float: left;' \
            '}' \
            '.twg-text {' \
            'display: block;' \
            'float: left;' \
            '}' \
            '.twg-tableRow {' \
            'clear: both;' \
            'padding: 4px;' \
            '}' \
            '.twg-learn a img {' \
            'filter:alpha(opacity=40); -moz-opacity:.4; opacity:.4;'\
            '}' \
            '.twg-learn img {' \
            'border: none;' \
            'padding: 1px;' \
            'margin-left: 2px;' \
            '}' \
            'a.twg-emoticon-selected img {' \
            'filter:alpha(opacity=100); -moz-opacity:1; opacity:1;'\
            '}' \
            'a.twg-emoticon-over img {' \
            'filter:alpha(opacity=70); -moz-opacity:.7; opacity:.7;'\
            '}' \
            '</style>'

  def get_start(self):
    return self.get_start_as_date().strftime(DATE_FORMAT)

  def get_end(self):
    return self.get_end_as_date().strftime(DATE_FORMAT)

  def get_end_as_date(self):
    if self.is_dynamic_date():
      return datetime.date.today()
    end = self.request.get('end')
    if end:
      end = datetime.datetime.strptime(end, DATE_FORMAT)
    return end or datetime.date.today()

  def get_start_as_date(self):
    if self.is_dynamic_date():
      return self.get_end_as_date() - datetime.timedelta(days=self.get_duration())
    start = self.request.get('start')
    if start:
      start = datetime.datetime.strptime(start, DATE_FORMAT)
    return start or datetime.date.today()

  def get_q(self):
    q = self.request.get('q')
    return q or "youtube annotations"

  def is_dynamic_date(self):
    return (self.request.get('dynamic_date') == 0) or True

  def get_duration(self):
    duration = self.request.get('duration')
    if duration:
      return int(duration)
    return 7

  def get_show_text(self):
    return self.request.get('show_text') != "0"

  def get_host_name(self):
    if os.environ.get('HTTP_HOST'):
      url = os.environ['HTTP_HOST']
    else:
      url = os.environ['SERVER_NAME']
    return url
