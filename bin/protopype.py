#!/usr/bin/env python3
from bottle import static_file, route, run


@route('/')
def serve_html():
  return static_file('index.html', root='')

@route('/<filename:path>')
def serve(filename):
  return static_file(filename, root='')

if __name__ == '__main__':
  run(host='0.0.0.0', port=3000, debug=True, reload=True)


