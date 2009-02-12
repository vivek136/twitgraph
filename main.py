#!/usr/bin/env python

import os
import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.api import urlfetch
from google.appengine.ext.webapp import template


class MainHandler(webapp.RequestHandler):

	def get(self):
		r = self.request

		q = r.get('q')
		if not q:
			q = 'youtube annotations'

		if r.get('date_dynamic') == '0':
			date_dynamic = False
		else:
			date_dynamic = True

		duration = r.get('duration')
		if not duration:
			duration = 7

		template_values = {
			'show_inputs': r.get('show_inputs') == '1',
			'q': q,
			'date_dynamic': date_dynamic,
			'show_text': r.get('show_text') == '1',
			'duration': duration,
			'start': r.get('start'),
			'end': r.get('end'),

		}
		path = os.path.join(os.path.dirname(__file__), 'index.html')
		self.response.out.write(template.render(path, template_values))


def main():
  application = webapp.WSGIApplication([('/', MainHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
