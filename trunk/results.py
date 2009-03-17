#!/usr/bin/env python

import os
import wsgiref.handlers
import logging as log
import cProfile, pstats, StringIO
from datetime import datetime
from django.utils import simplejson as json
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import twitgraph_base_servlet
from biz.twitter_fetcher import TwitterFetcher
from biz.tweets_analyzer import TweetsAnalyzer

class ResultsHandler(twitgraph_base_servlet.BaseHandler):

  SEARCH_URL = 'http://search.twitter.com/search.json'

  def get(self):
    template_values = self.get_template_values()
    fetcher = TwitterFetcher()
    all_results = fetcher.fetch_results(self.get_q(), self.get_start(), self.get_end())
    ret = {}
    if all_results is None:
      status = 500
    else:
      status = 200
      analyzer = TweetsAnalyzer()
      classified_results = analyzer.classify(all_results)
      stats, aggregate_results = analyzer.aggregate(classified_results)
      ret = {"stats": stats, "aggregate": aggregate_results}
      if self.get_show_text():
        ret['results'] = classified_results
    ret['status'] = status;
    template_values['json_results'] = json.dumps(ret)
    jsonp_callback = self.get_jsonp_callback()
    if jsonp_callback:
      template_values['callback'] = jsonp_callback
    path = os.path.join(os.path.dirname(__file__), 'results.json')
    self.response.out.write(template.render(path, template_values))

  def get_jsonp_callback(self):
    return self.request.get('callback')

def real_main():
  application = webapp.WSGIApplication([('/results.json', ResultsHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)

def profile_main():
  # This is the main function for profiling
  # We've renamed our original main() above to real_main()
  prof = cProfile.Profile()
  prof = prof.runctx("real_main()", globals(), locals())
  stream = StringIO.StringIO()
  stats = pstats.Stats(prof, stream=stream)
  stats.sort_stats("time")  # Or cumulative
  stats.print_stats(5)  # 80 = how many to print
  # The rest is optional.
  # stats.print_callees()
  # stats.print_callers()
  log.info("Profile data:\n%s", stream.getvalue())

if __name__ == '__main__':
  real_main()
