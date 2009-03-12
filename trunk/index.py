#!/usr/bin/env python

import os
import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.api import urlfetch
from google.appengine.ext.webapp import template


class MainHandler(webapp.RequestHandler):

  def get(self):
    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, self.get_template_values()))

  def get_template_values(self):
    r = self.request

    q = r.get('q')
    if not q:
      q = 'youtube annotations'

    if r.get('dynamic_date') == '0':
      dynamic_date = False
    else:
      dynamic_date = True

    duration = r.get('duration')
    if not duration:
      duration = 7

    template_values = {
      'q': q,
      'dynamic_date': dynamic_date,
      'show_text': r.get('show_text') == '1',
      'duration': duration or 0,
      'start': r.get('start'),
      'end': r.get('end'),
      'version': os.environ['CURRENT_VERSION_ID'],
      'base_url': 'http://%s' % self.get_host_name(),
    }
    return template_values


  def get_host_name(self):
    if os.environ.get('HTTP_HOST'):
      url = os.environ['HTTP_HOST']
    else:
      url = os.environ['SERVER_NAME']
    return url


def main():
  application = webapp.WSGIApplication([('/', MainHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
