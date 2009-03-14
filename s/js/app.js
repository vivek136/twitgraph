try {
google.load('visualization', '1', {packages: ['linechart']});
} catch(e){}

// Create a Namespace mechanism to prevent javascript name clashes.
var Namespace =
{
  Register : function(_Name) {
    var chk = false;
    var cob = "";
    var spc = _Name.split(".");
    for(var i = 0; i<spc.length; i++) {
      if(cob!=""){cob+=".";}
      cob+=spc[i];
      chk = this.Exists(cob);
      if(!chk) {
        this.Create(cob);
      }
    }
    if(chk) {
      throw "Namespace: " + _Name + " is already defined.";
    }
  },

  Create : function(_Src) {
    eval("window." + _Src + " = new Object();");
  },

  Exists : function(_Src) {
    eval("var NE = false; try{if(" + _Src + "){NE = true;}else{NE = false;}}catch(err){NE=false;}");
    return NE;
  }
}

// All our JS code will be under twitgraph.*
// Javascript namespace mechanism is copied from http://www.codeproject.com/KB/scripting/jsnamespaces.aspx
Namespace.Register("twitgraph");

// Global package holds some (very few) global javascript variables.
twitgraph.Globals = {
  searchers: null,
};

// The Utils class is the general container for all non-specific useful methods.
// The class contains only static methods.
twitgraph.Utils = {

/**
 * Adds a script to the <head> section of the page.
 * @param url {String} the script url.
 **/
addScript: function(url) {
  var script = document.createElement("script");
  script.setAttribute("src", url);
  script.setAttribute("type", "text/javascript");
  document.body.appendChild(script);
},

/**
 * Creates and sends a jsonp call.
 * @param url {String} urls of the jsonp call.
 * @param callbackName
 **/
jsonp: function(url, callbackName) {
  url += '&callback=' + callbackName;
  this.addScript(url);
},

/**
 * Initializes the page.
 **/
init: function() {
  twitgraph.Utils.log('start');
  twitgraph.Utils.log(query_state);
  if (query_state.dynamic_date) {
    var today = new Date();
    var yday = new Date(today.getFullYear(), today.getMonth(), today.getDate() - 1);
    query_state.end = yday;
    var aWeekAgo = new Date(today.getFullYear(), today.getMonth(), today.getDate() - 8);
    query_state.start = aWeekAgo;
    var date_start = twitgraph.Utils.$('dateStart');
    if (date_start) {
      date_start.value =  query_state.start.toDateString();
    }
    var date_end = twitgraph.Utils.$('dateEnd');
    if (date_end) {
      date_end.value =  query_state.end.toDateString();
    }
  }
  this.refresh();
},

/**
 * The on-submit handler for the inputs form.
 * Reads all data in the form fields and refreshes the page (graph and everything)
 **/
onSubmit: function() {
  // Gather input.
  var dynamic_date = twitgraph.Utils.$('dateDynamic1').checked;
  var start, end;
  var duration = parseInt(twitgraph.Utils.$('duration').value);
  if (dynamic_date) {
    if (isNaN(duration)) {
      alert("Uncool duration, dang!");
      return;
    }
    var today = new Date();
    var yday = new Date(today.getFullYear(), today.getMonth(), today.getDate() - 1);
    end = yday;
    start = new Date(yday.getFullYear(), yday.getMonth(), yday.getDate() - duration);
  } else {
    start = new Date(twitgraph.Utils.$('dateStart').value);
    end = new Date(twitgraph.Utils.$('dateEnd').value);
    if (isNaN(start) || isNaN(end)) {
      alert("Uncool dates, dude!");
      return;
    }
  }
  var q = twitgraph.Utils.$('q').value;
  var show_text = twitgraph.Utils.$('showText').checked;
  query_state = new twitgraph.QueryState(q, dynamic_date, start, end, duration, show_text);
  twitgraph.Utils.log(query_state);
  this.refresh();
},

/**
 * Refreshes the page elements.
 * The page most current state is preserved in the query_state variable.
 * This function reads the state from query_state and updates the various page elemetns by it.
 **/
refresh: function() {
  twitgraph.Utils.log(query_state);
  this.query(query_state.q, query_state.start, query_state.end, query_state.show_text);
  var title = twitgraph.Utils.$('twg-title');
  if (title) {
    title.innerHTML = query_state.q;
  }
  var embed_code = twitgraph.Utils.$('embed-code');
  if (embed_code) {
    embed_code.value = this.getEmbedCode();
  }
},

/**
 * Queries the twitter search service.
 *
 * @param q {String} the query string.
 * @param start {Date} start date.
 * @param end {Date} end date.
 * @param showText {bool} Show text results from the query.
 **/
query: function(q, start, end, showText) {
  twitgraph.Utils.time('query');
  var search = new twitgraph.SearchMaster(q, start, end, showText);
  search.run();
},

/**
 * A convenience for document.getElementById()
 *
 * @return {Object} A dom element by the el ID. null or undefined if that object doesn't exist.
 **/
$: function(el) {
  return document.getElementById(el);
},

/**
 * Gets embed code for the current query_state.
 *
 * @return {String} The embedded code string.
 **/
getEmbedCode: function() {
  var a = [];
  var urlBase = this.getBaseUrl();
  a.push('<h3>TwitGraph for ');
  a.push(query_state.q);
  a.push('</h3>\n');
  a.push('<div id="twit-graph"></div>\n');
  a.push('<script type="text/javascript" src="');
  a.push(urlBase);
  a.push('embed?');
  a.push('&q=');
  a.push(encodeURIComponent(query_state.q));
  a.push('&dynamic_date=');
  if (query_state.dynamic_date) {
    a.push('1');
    a.push('&duration=');
    a.push(encodeURIComponent(query_state.duration));
  } else {
    a.push('0');
    a.push('&start=');
    a.push(encodeURIComponent(query_state.start.toDateString()));
    a.push('&end=');
    a.push(encodeURIComponent(query_state.end.toDateString()));
  }
  a.push('&show_text=');
  a.push(query_state.show_text ? '1' : '0');
  a.push('"> </sc');
  a.push('ript>');
  return a.join('');
},

getBaseUrl: function() {
  var hostEnd = document.location.href.indexOf("?");
  if (hostEnd < 0) {
    hostEnd = document.location.href.length;
  }
  var urlBase = document.location.href.substr(0, hostEnd);
  return urlBase;
},

/**
 * Creates a function delegate.
 * That's very useful for creating callbackes on specific object scopes.
 *
 * @param scope {Object} The scope of the created delegate. Usually this is an instance of an object enclosing the callback.
 * @param callback {Function} A member function in scope.
 * @para data {Object} an optional additional data object to be passed to the callback when called.
 * @return {Function} A callback function bound to scope.
 **/
createDelegate: function(scope, callback, data) {
  var func = function() {
    if (data != undefined) {
      arguments.push(data);
    }
    return callback.apply(scope, arguments);
  }
  return func;
},

/**
 * Compares dates.
 *
 * @param a {Date}
 * @param b {Date}
 * @return {int} a number greater than 0 if a > b, smaller then 0 if a < b and 0 if they equal.
 **/
compareDates: function(a, b) {
  return Date.parse(a.date) > Date.parse(b.date) ? 1 : -1;
},

/**
 * Logs the message to firebug
 **/
log: function(msg) {
  if (window.console && window.console.log) {
    window.console.log(msg);
  }
},

/**
 * Logs the error to firebug
 **/
error: function(msg) {
  if (window.console && window.console.error) {
    window.console.error(msg);
  }
},

time: function(name) {
  if (window.console && window.console.time) {
    window.console.time(name);
  }
},

timeEnd: function(name) {
  if (window.console && window.console.timeEnd) {
    window.console.timeEnd(name);
  }
},

};

/**
 * Class: SearchMaster.
 * This is the controller of all twitter searches.
 **/
/**
 * SearchMaster constructor.
 *
 * @param q {String} The search query.
 * @param start {Date} Start date.
 * @param end {Date} End date.
 * @param showText {bool} Show the text results.
 **/
twitgraph.SearchMaster = function(q, start, end, showText) {
  var HAPPY = ' :)';
  var SAD = ' :(';
  this.searchers = [];
  this.doneCount = 0;
  var i = 0;
  this.searchers.push(new twitgraph.Searcher(q, start, end, showText, i++));
  this.searchers.push(new twitgraph.Searcher(q + HAPPY, start, end, showText, i++));
  this.searchers.push(new twitgraph.Searcher(q + SAD, start, end, showText, i++));
  twitgraph.Globals.searchers = this.searchers;
}

twitgraph.SearchMaster.prototype.run = function () {
  twitgraph.Utils.log("starting search");
  twitgraph.Utils.$('twg-resultsText').innerHTML = '';
  twitgraph.Utils.$('twg-graph').innerHTML = '<img src="' + TWITGRAPH_BASE_URL + '/s/img/loading.gif" alt="Loading..." tooltip="Loading..." style="display:block;margin:auto;"/>';
  this.doneCount = 0;
  for (var i = 0; i < this.searchers.length; ++i) {
    this.searchers[i].run(twitgraph.Utils.createDelegate(this, this.onSearchDone));
  }
}

twitgraph.SearchMaster.prototype.onSearchDone = function (searcher) {
  twitgraph.Utils.log("Searcher done " + searcher);
  this.doneCount++;
  if (this.doneCount == this.searchers.length) {
    twitgraph.Utils.timeEnd('query');
    // All searches are ready
    this.drawGraph(this.getAggregateResults());
  }
}

twitgraph.SearchMaster.prototype.getAggregateResults = function() {
  var aggregate = {};
  for (var s = 0; s < this.searchers.length; ++s) {
    var results = this.searchers[s].getAggregateResults();
    for (var date in results) {
      if (!aggregate[date]) {
        aggregate[date] = {};
      }
      aggregate[date][s] = results[date];
    }
  }
  var arr = [];
  for (var date in aggregate) {
    var dateCell = new twitgraph.DateData(date);
    for (var i = 0; i < this.searchers.length; ++i) {
      dateCell[i] = aggregate[date][i];
    }
    arr.push(dateCell);
  }
  arr.sort(twitgraph.Utils.compareDates);
  twitgraph.Utils.log(arr);
  return arr;
}

twitgraph.SearchMaster.prototype.drawGraph = function(dates) {
  // Create and populate the data table.
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Date');
  data.addColumn('number', 'All');
  data.addColumn('number', 'Happy');
  data.addColumn('number', 'Sad');
  data.addRows(dates.length);
  for (var i = 0; i < dates.length; ++i) {
    data.setCell(i, 0, dates[i].date);
    data.setCell(i, 1, dates[i].getAll());
    data.setCell(i, 2, dates[i].getHappy());
    data.setCell(i, 3, dates[i].getSad());
  }

  // Create and draw the visualization.
  twitgraph.Utils.$('twg-graph').innerHTML = '';
  new google.visualization.LineChart(twitgraph.Utils.$('twg-graph')).
    draw(data, null);
}


/**
 * Class: DateData
 * This is a simple struct-style class for holding date specific tweet stats.
 **/
twitgraph.DateData = function(date) {
  this.date = date;
}

twitgraph.DateData.prototype.getAll = function() {
  return this[0];
}

twitgraph.DateData.prototype.getHappy = function() {
  return this[1];
}

twitgraph.DateData.prototype.getSad = function() {
  return this[2];
}

twitgraph.DateData.prototype.toString = function() {
  var str = [this.date];
  if (this.getAll() != undefined) {
    str.push(' :-|');
    str.push(this.getAll());
  }
  if (this.getHappy() != undefined) {
    str.push(' :-)');
    str.push(this.getHappy());
  }
  if (this.getSad() != undefined) {
    str.push(' :-(');
    str.push(this.getSad());
  }
  return str.join('');
}

/**
 * Class: Searcher.
 * This class implements the basic search algorithm per a single twitter query.
 **/
twitgraph.Searcher = function (q, start, end, showText, id) {
  this.SEARCH_URL = 'http://search.twitter.com/search.json';
  this.q = q;
  this.start = start;
  this.end = end;
  this.showText = showText;
  this.results = [];
  this.doneCallback = null;
  this.aggregateResults = null;
  this.id = id;
}


twitgraph.Searcher.prototype.run = function (onDone) {
  this.doneCallback = onDone;
  var searchUrl = this.SEARCH_URL;
  var query = this.q + " since:" + this.buildDate(this.start) + " until:" + this.buildDate(this.end);
  searchUrl += "?q=" + encodeURIComponent(query);
  searchUrl += '&rpp=100';
  twitgraph.Utils.log("Search URL: " + searchUrl);
  twitgraph.Utils.jsonp(searchUrl, 'twitgraph.Globals.searchers[' + this.id + '].onSearchResult');
}

twitgraph.Searcher.prototype.getAggregateResults = function () {
  return this.aggregateResults;
}

twitgraph.Searcher.prototype.buildDate = function(date) {
  return "" + date.getFullYear() + "-" + this.pad(date.getMonth() + 1) + "-" + this.pad(date.getDate());
}

twitgraph.Searcher.prototype.pad = function(n) {
  return (n < 10) ? "0" + n : "" + n;
}

twitgraph.Searcher.prototype.onSearchResult = function(o) {
  if (o.max_id == -1) {
    // That's an error. No mas para hoy
    twitgraph.Utils.error("There were errors in the search");
  }
  this.results = this.results.concat(o.results);
  if (o.next_page) {
    var searchUrl = this.SEARCH_URL;
    searchUrl += o.next_page;
    twitgraph.Utils.log("Recursive Search: " + searchUrl);
    twitgraph.Utils.jsonp(searchUrl, 'twitgraph.Globals.searchers[' + this.id + '].onSearchResult');

  } else {
    this.searchDone();
  }
  if (this.showText) {
    twitgraph.Utils.$('twg-resultsText').innerHTML += this.formatTexts(o.results);
  }
}

twitgraph.Searcher.prototype.formatTexts = function(results) {
  var html = [];
  for (var i = 0; i < results.length; ++i) {
    html.push('<div class="twg-tableRow">');
    html.push('<span class="twg-user">');
    html.push(results[i].from_user);
    html.push(": ");
    html.push("</span>");
    html.push('<span class="twg-text">');
    html.push(results[i].text);
    html.push('</span>');
    html.push('</div>');
  }
  return html.join("");
}

twitgraph.Searcher.prototype.searchDone = function () {
  var dates = {};
  for (var i = 0; i < this.results.length; ++i) {
    var date = new Date(this.results[i].created_at);
    //Extract only the short format which includes the date only
    date = date.toDateString();
    if (!dates[date]) {
      dates[date] = 0;
    }
    ++dates[date];
  }
  this.aggregateResults = dates;
  this.doneCallback(this);
}

twitgraph.Searcher.prototype.toString = function () {
  return 'q=' + this.q;
}

// A data structure defining the state of the current query.
twitgraph.QueryState = function(q, dynamic_date, start, end, duration, show_text) {
  this.q = q;
  this.dynamic_date = dynamic_date;
  this.start = start;
  this.end = end;
  this.duration = duration;
  this.show_text = show_text;
  twitgraph.Utils.log(this);
}
twitgraph.QueryState.prototype.toString = function() {
  var a = [];
  a.push(this.q);
  a.push(this.dynamic_date);
  a.push(this.start.toDateString());
  a.push(this.end.toDateString());
  a.push(this.duration);
  a.push(this.show_text);
  return a.join(", ");
}

if (window.twitgraph_onAppJsLoad) {
  twitgraph_onAppJsLoad();
}
