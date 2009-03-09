google.load('visualization', '1', {packages: ['linechart']});
var search;

function addScript(url) {                
	var script = document.createElement("script");        
	script.setAttribute("src", url);
	script.setAttribute("type", "text/javascript");                
	document.body.appendChild(script);
}

function jsonp(url, callbackName) {                
	url += '&callback=' + callbackName;
	addScript(url);
}

function twgInit() {
	log('start');
	log(query_state);
	if (query_state.dynamic_date) {
				var today = new Date();
				var yday = new Date(today.getFullYear(), today.getMonth(), today.getDate() - 1);
				query_state.end = yday;
				var aWeekAgo = new Date(today.getFullYear(), today.getMonth(), today.getDate() - 8);
				query_state.start = aWeekAgo;
	}
	twgRefresh();
}

function onSubmit() {
	// Gather input.
	var dynamic_date = $('dateDynamic1').checked;
	var start, end;
	var duration = parseInt($('duration').value);
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
		start = Date.parse($('dateStart').value);
		end = Date.parse($('dateEnd').value);
		if (isNaN(start) || isNaN(end)) {
			alert("Uncool dates, dude!");
			return;
		}
	}
	var q = $('q').value;
	var show_text = $('showText').checked;
	query_state = new QueryState(q, dynamic_date, start, end, duration, show_text);
	log(query_state);
	twgRefresh();
}

function twgRefresh() {
	log(query_state);
	query(query_state.q, query_state.start, query_state.end, query_state.show_text);
	$('twg-title').innerHTML = query_state.q;
	var embed_code = 	$('embed-code');
	if (embed_code) {
					embed_code.value = serialize();
  }
}

function query(q, start, end, showText) {
	search = new SearchMaster(q, start, end, showText);
	search.run();
}

function $(el) {
	return document.getElementById(el);
}

function serialize() {
	var a = [];
	var urlBase = document.location.href.substr(0, document.location.href.indexOf("?"));
	a.push('<h3>Twitter Graph For: <span id="twg-title"/></h3>');
  a.push('<div id="twg-graph"></div>');
	a.push('<div id="twg-resultsText"></div>');
	a.push('<style>');
	a.push($('style').innerHTML);
	a.push('</style>');
	a.push('<script type="text/javascript" src="http://www.google.com/jsapi"></sc');
	a.push('ript>');
	a.push('<script type="text/javascript" src="');
	a.push(urlBase);
	a.push('/s/js/app.js"></sc');
	a.push('ript>');
	a.push('<script type="text/javascript">');
	a.push('var query_state = new QueryState("');
	a.push(query_state.q); // query
	a.push('",');
	a.push(query_state.date_dynamic? 'true,' : 'false,'); // date dynamic?
	a.push('new Date("');
	a.push(query_state.start.toDateString());
	a.push('"),');
	a.push('new Date("');
	a.push(query_state.end.toDateString());
	a.push('"),');
	a.push(query_state.duration);
	a.push(',');
	a.push(query_state.show_text ? 'true' : 'false');
	a.push(');');
	a.push('twgInit();');
	a.push('</sc');
	a.push('ript>');
	return a.join('');
}

function createDelegate(scope, callback, data) {
	var func = function() {
		if (data != undefined) {
						arguments.push(data);
					}
					return callback.apply(scope, arguments);
			}	
			return func;
}


function compareDates(a, b) {
	return Date.parse(a.date) > Date.parse(b.date) ? 1 : -1;
}

function log(msg) {
	if (window.console && window.console.log) {
		window.console.log(msg);
	}
}
function error(msg) {
	if (window.console && window.console.error) {
		window.console.error(msg);
	}
}
//////////////////////////////////////////////////
var HAPPY = ' :)';
var SAD = ' :(';
var globalSearchers;
function SearchMaster(q, start, end, showText) {
	this.searchers = [];
	this.doneCount = 0;
	var i = 0;
	this.searchers.push(new Searcher(q, start, end, showText, i++));
	this.searchers.push(new Searcher(q + HAPPY, start, end, showText, i++));
	this.searchers.push(new Searcher(q + SAD, start, end, showText, i++));
	globalSearchers = this.searchers;
}

SearchMaster.prototype.run = function () {
  log("starting search");
	$('twg-resultsText').innerHTML = '';
	$('twg-graph').innerHTML = 'Loading Graph...';
	this.doneCount = 0;
	for (var i = 0; i < this.searchers.length; ++i) {
		this.searchers[i].run(createDelegate(this, this.onSearchDone));
	}
}

SearchMaster.prototype.onSearchDone = function (searcher) {
	log("Searcher done " + searcher);
	this.doneCount++;
	if (this.doneCount == this.searchers.length) {
		// All searches are ready
		this.drawGraph(this.getAggregateResults());
	}
}

SearchMaster.prototype.getAggregateResults = function() {
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
		var dateCell = new DateData(date);
		for (var i = 0; i < this.searchers.length; ++i) {
			dateCell[i] = aggregate[date][i];
		}
		arr.push(dateCell);
	}
	arr.sort(compareDates);
	log(arr);
	return arr;
}

SearchMaster.prototype.drawGraph = function(dates) {
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
	$('twg-graph').innerHTML = '';
        new google.visualization.LineChart($('twg-graph')).
            draw(data, null);  
}


////////////////////////////////////////////

function DateData(date) {
	this.date = date;
}

DateData.prototype.getAll = function() {
	return this[0];
}

DateData.prototype.getHappy = function() {
	return this[1];
}

DateData.prototype.getSad = function() {
	return this[2];
}

DateData.prototype.toString = function() {
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

/////////////////////////////////////////////
var ACCUMULATE = true;
var SEARCH_URL = 'http://search.twitter.com/search.json';
function Searcher(q, start, end, showText, id) {
	this.q = q;
	this.start = start;
	this.end = end;
	this.showText = showText;
	this.results = [];
	this.doneCallback = null;
	this.aggregateResults = null;
	this.id = id;
}


Searcher.prototype.run = function (onDone) {
	this.doneCallback = onDone;
	var searchUrl = SEARCH_URL;
	var query = this.q + " since:" + this.buildDate(this.start) + " until:" + this.buildDate(this.end);
	searchUrl += "?q=" + encodeURIComponent(query);
	searchUrl += '&rpp=100';
	log("Search URL: " + searchUrl);
	jsonp(searchUrl, 'globalSearchers[' + this.id + '].onSearchResult');
}

Searcher.prototype.getAggregateResults = function () {
	return this.aggregateResults;
}

Searcher.prototype.buildDate = function(date) {
	return "" + date.getFullYear() + "-" + this.pad(date.getMonth() + 1) + "-" + this.pad(date.getDate());
}

Searcher.prototype.pad = function(n) {
	return (n < 10) ? "0" + n : "" + n;
}

Searcher.prototype.onSearchResult = function(o) {
	if (o.max_id == -1) {
		// That's an error. No mas para hoy
		error("There were errors in the search");
	}
	this.results = this.results.concat(o.results);
	if (ACCUMULATE && o.next_page) {
		var searchUrl = SEARCH_URL;
		searchUrl += o.next_page;
		log("Recursive Search: " + searchUrl);
		jsonp(searchUrl, 'globalSearchers[' + this.id + '].onSearchResult');
		
	} else {
		this.searchDone();
	}
	if (this.showText) {
		$('twg-resultsText').innerHTML += this.formatTexts(o.results);
	}
}

Searcher.prototype.formatTexts = function(results) {
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

Searcher.prototype.searchDone = function () {
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

Searcher.prototype.toString = function () {
	return 'q=' + this.q;
}

// A data structure defining the state of the current query.
function QueryState(q, dynamic_date, start, end, duration, show_text) {
			this.q = q;
			this.dynamic_date = dynamic_date;
			this.start = start;
			this.end = end;
			this.duration = duration;
			this.show_text = show_text;
			log(this);
}
QueryState.prototype.toString = function() {
				var a = [];
				a.push(this.q);
				a.push(this.dynamic_date);
				a.push(this.start.toDateString());
				a.push(this.end.toDateString());
				a.push(this.duration);
				a.push(this.show_text);
				return a.join(", ");
}
