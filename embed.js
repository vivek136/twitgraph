document.write('<script type="text/javascript" src="http://www.google.com/jsapi"></sc'+'ript>');
document.write('<script type="text/javascript" src="{{base_url}}/s/js/app.js"></sc'+'ript>');

function twg_onAppJsLoad() {
  google.load('visualization', '1', {packages: ['linechart']});
  window.query_state = new QueryState('{{q|escape}}',
      {% if dynamic_date %}true{% else %}false{% endif%},
      Date.parse('{{start|escape}}'),
      Date.parse('{{end|escape}}'),
      {{duration|escape}},
      {% if show_text %}true{% else %}false{% endif%});
  $('twit-graph').innerHTML = '<div id="twg-graph"></div><div id="twg-resultsText"></div>';
  google.setOnLoadCallback(twgInit);
}

document.write('<style id="style">' +
    '#twg-graph{width:600px;height:300px;}' +
    '#twg-resultsText{font-size:10pt;padding:20px;font-family:Arial;}' +
    '.twg-user{color:green;width:150px;display:block;float:left;}' +
    '.twg-text{display:block;float:left;}' +
    '.twg-tableRow{clear:both;padding:4px;}' +
    '</style>');

