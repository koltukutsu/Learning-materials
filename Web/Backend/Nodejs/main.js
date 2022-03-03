var http = require('http');
var m_dt = require('./firstModule');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.end('Hello World!' + m_dt.myDateTime());
}).listen(8081);
